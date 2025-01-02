import global_vars
import pygame

def round_to_halfs(ms):
    "1.9 -> 2.0, 1.2 -> 1.5"
    remainder = ms%0.5
    return ms + (0.5 - remainder)


class Floor():
    def __init__(self, floor_number, building_surface: pygame.Surface ,mangment_system) -> None:
        self.floor_number = floor_number
        self.building_surface = building_surface
        self.y = self.building_surface.get_height() - (self.floor_number + 1) * global_vars.FLOOR_HEIGHT_PX

        self.mangment_system = mangment_system
        self._eta = 0
        self._holding_elevator = 0
        self.font = pygame.font.SysFont('Arial', 25)
        
        self.floor_img = pygame.image.load(global_vars.FLOOR_BACKGROUND_FILE)
    
    
    
    def draw(self):
        _floor_img = pygame.transform.scale(self.floor_img, (global_vars.BULDING_WIDTH_PX,global_vars.FLOOR_HEIGHT_PX)) 
        # add button
        pygame.draw.rect(_floor_img,
            global_vars.FLORR_BUTTON_COLLOR_WAIT if self._eta > 0 
                else global_vars.FLORR_BUTTON_COLLOR_HOLD if self._holding_elevator > 0 
                else global_vars.FLORR_BUTTON_COLLOR_DEFAULT, (
            global_vars.FLOOR_BUTTON_X, global_vars.FLOOR_BUTTON_Y,
            global_vars.FLOOR_BUTTON_WIDTH, global_vars.FLOOR_BUTTON_HEIGHT
        ))
        # add underline
        pygame.draw.rect(_floor_img, (255,255,255), (
            0, global_vars.FLOOR_HEIGHT_PX - global_vars.FLOOR_UNDERLINE_HEIGHT_PX ,
            global_vars.BULDING_WIDTH_PX, global_vars.FLOOR_UNDERLINE_HEIGHT_PX
        ))
        # add floor number
        _floor_img.blit(self.font.render(f'{self.floor_number}', True, (255,0,0)),
                        (global_vars.FLOOR_TEXT_X, global_vars.FLOOR_TEXT_Y))

        # add timer
        if (self._eta + self._holding_elevator) > 0:
            _floor_img.blit(self.font.render(
                    f'{round_to_halfs((self._eta + self._holding_elevator)/1_000):.1f}', True, (0,0,0), 
                    global_vars.FLORR_BUTTON_COLLOR_WAIT if self._eta > 0 
                    else global_vars.FLORR_BUTTON_COLLOR_HOLD 
                ),
                (global_vars.FLOOR_BUTTON_X+ global_vars.FLOOR_BUTTON_WIDTH, global_vars.FLOOR_BUTTON_Y)
            )
            
        self.building_surface.blit(_floor_img, (0, self.y))
        

    def handle_click(self, x, y):
         # if click was not in button x,y bounds, do nothing
        if not(
            global_vars.FLOOR_BUTTON_X <= x <= (global_vars.FLOOR_BUTTON_X + global_vars.FLOOR_BUTTON_WIDTH)
            and global_vars.FLOOR_BUTTON_Y <= y <= (global_vars.FLOOR_BUTTON_Y + global_vars.FLOOR_BUTTON_HEIGHT)
            ):
            return
        # if allready waiting, do nothing
        if self._eta > 0:
            return
        self.mangment_system(self.floor_number)
    
    def update_eta(self, eta):
        self._eta = eta

    def update_holding_elevator(self, remaining_time):
        self._holding_elevator = remaining_time
