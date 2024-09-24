
from typing import List
import pygame
from Elevator import Elevator
from Floor import Floor
import global_vars


class Building():
    def __init__(self, n_floors, n_elevators) -> None:
        self.surface_width = (global_vars.BULDING_WIDTH_PX
                              + n_elevators * global_vars.ELEVATOR_IMG_WIDTH_PX
                              + global_vars.BUILDING_GAP_PX)
        self.surface_height =  n_floors * global_vars.FLOOR_HEIGHT_PX

        self.surface = pygame.Surface((self.surface_width, self.surface_height))
        self.floors: List[Floor] = [Floor(i, self.surface ,self.call_elevator)
                                    for i in range(n_floors)]
        self.elevators: List[Elevator] = [Elevator(i, self.surface, self.update_arrival_status)
                                          for i in range(n_elevators)]

    def _draw(self):
        self.surface.fill('white')
        for floor in self.floors:
            floor.draw()
        for elevator in self.elevators:
            elevator.draw()

    def _update(self):
        for elevator in self.elevators:
            tasks, waiting = elevator.get_updates()
            for task in tasks:
                self.floors[task['floor']].update_eta(task['eta'])
            if waiting:
                self.floors[waiting['floor']].update_holding_elevator(waiting['remaining'])


    def update_and_draw(self):
        self._update()
        self._draw()


    def _determine_flor_y(self, y):
        _y = self.surface_height - y
        floor_number = int(_y // global_vars.FLOOR_HEIGHT_PX)
        if floor_number >= len(self.floors):
            return None, None
        floor = self.floors[floor_number]
        normilzed_y = y - floor.y
        return floor, normilzed_y

    def handle_click_event(self, x,y):
        floor, adjusted_y = self._determine_flor_y(y)
        if floor is not None:
            floor.handle_click(x, adjusted_y)


    def call_elevator(self, floor_number):
        "Manager function for floor, to request an elevator"
        current_eta = 1_000_000
        fastest_elevator = None
        for elevator in self.elevators:
            eta = elevator.estimate_arrival_time(floor_number)
            if eta < current_eta:
                current_eta = eta
                fastest_elevator = elevator
        
        if not fastest_elevator:
            return
        px_target = self.surface_height - (floor_number * global_vars.FLOOR_HEIGHT_PX) - global_vars.ELEVATOR_IMG_HEIGHT_PX
        fastest_elevator.add_stop(floor_number, current_eta, px_target)


    def update_arrival_status(self, floor_number, status):
        "Manager function for elevator, to update when arrived to a floor"
        floor: Floor = self.floors[floor_number]
        match status:
            case 'arrived':
                floor.update_eta(0)
                floor.update_holding_elevator(global_vars.MS_WAIT_IN_FLOOR)
            case 'free':
                floor.update_holding_elevator(0)

    def __repr__(self) -> str:
        return f'n-floors: {len(self.floors)}, n_elevators: {len(self.elevators)}'
