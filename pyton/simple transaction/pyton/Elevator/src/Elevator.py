
from typing import Callable
import global_vars
import pygame
pygame.init()


elevator_img = pygame.image.load(global_vars.ELEVATOR_BACKGROUND_FILE)
elevator_size = (global_vars.ELEVATOR_IMG_WIDTH_PX,global_vars.ELEVATOR_IMG_HEIGHT_PX)
elevator_surface = pygame.transform.scale(elevator_img, elevator_size)

sound = pygame.mixer.Sound(global_vars.ELEVATOR_DING_FILE)

class Elevator():
    def __init__(self, 
            elevator_number : int,
            building_surface: pygame.Surface,
            notify_arrival: Callable) -> None:
        self.queue = []
        self.current_floor = 0
        self.waiting = 0
        self.notify_arrival = notify_arrival

        self.elevator_number = elevator_number
        self.building_surface = building_surface
        self.x = global_vars.BULDING_WIDTH_PX + elevator_number * global_vars.ELEVATOR_IMG_WIDTH_PX
        self.y = building_surface.get_height() - global_vars.ELEVATOR_IMG_HEIGHT_PX


    def draw(self):
        if self.waiting > 0:
            pygame.draw.rect(self.building_surface, 'red', (self.x, self.y, *elevator_size))
        self.building_surface.blit(elevator_surface, (self.x, self.y))


    def estimate_arrival_time(self, floor_number):
        if self.current_floor == floor_number:
            return 0

        if len(self.queue) > 0:
            last_in_queue = self.queue[0]
            return (last_in_queue['eta'] +
                    global_vars.MS_WAIT_IN_FLOOR +
                    abs(last_in_queue['floor'] - floor_number) * global_vars.MS_PER_FLOOR)

        return abs(self.current_floor - floor_number) * global_vars.MS_PER_FLOOR + self.waiting


    def add_stop(self, floor_number, eta, px_target):
        if self.current_floor == floor_number:
            waiting_adjustment = global_vars.MS_WAIT_IN_FLOOR - self.waiting
            for task in self.queue:
                task['eta'] += waiting_adjustment
            self._on_arrival()
        else:
            self.queue.insert(0,{
                'floor': floor_number, 
                'px_target': px_target,
                'eta': eta 
            })


    def _on_arrival(self):
        self.waiting = global_vars.MS_WAIT_IN_FLOOR
        self.notify_arrival(self.current_floor, 'arrived')
        sound.play()


    def _calculate_px_move(self):
        time_fraction = min(1, global_vars.GAME_ITERATION_LAPS_TIME_MS / self.queue[-1]['eta'])
        px_remaining = self.queue[-1]['px_target'] - self.y
        return time_fraction * px_remaining
    

    def _update_times(self):
        for task in self.queue:
                task['eta'] -= global_vars.GAME_ITERATION_LAPS_TIME_MS


    def _handle_wait(self):
        if self.waiting > 0:
            self.waiting = max(0, self.waiting - global_vars.GAME_ITERATION_LAPS_TIME_MS)
            if self.waiting == 0:
                self.notify_arrival(self.current_floor, 'free')

        return self.waiting > 0


    def _handle_movment(self):
        # no more tasks
        if len(self.queue) == 0:
                return

        #  start ride 
        if self.current_floor is not None:
            self.current_floor = None

        #  update position
        self.y += self._calculate_px_move()

        # finish ride
        if self.y == self.queue[-1]['px_target']:
            self.current_floor = self.queue.pop()['floor']
            self._on_arrival()


    def _iteration(self):
        still_wating = self._handle_wait()

        if not still_wating:
            self._handle_movment()

        self._update_times()
            

    def get_updates(self):
        self._iteration()
        _wating =  {'floor': self.current_floor, 'remaining': self.waiting} if self.waiting else None
        return [self.queue, _wating]
    
    def __repr__(self) -> str:
        return f'No. {self.elevator_number} - tasks: {self.queue}'
    