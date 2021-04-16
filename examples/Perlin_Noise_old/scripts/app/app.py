import pygame, math

from random import choice, randint

from os.path import join


# from scripts.audio.audio import AudioHandler

from scripts.UI.button import Button
from scripts.UI.text import Text, singleline_text
# from scripts.UI.textinput import TextInput

# from scripts.UI.hud import Hud

# from scripts.app.sprite import Sprite, load_layers

from PyWire3D.World.World import World
from PyWire3D.Camera.Camera import Camera

from scripts.utilities.data import Data
# from scripts.utilities.position import random2D, multiply2D, add2D
# from scripts.utilities.imgedit import clip
# from scripts.utilities.filehandle import file_prompt

# from scripts.vfx.genericparticle import genericparticle_logic, genericparticle_update, genericparticle_update_without_camera
# from scripts.vfx.transitionoverlay import TransitionOverlayCircleBasic
# from scripts.vfx.squaretransition import SquareTransition
# from scripts.vfx.quartercircletransition import QuarterCircleTransition

class App:
    def __init__(self, data, assets, CONSTANTS):
        self.CONSTANTS = CONSTANTS
        self.data = data
        self.assets = assets

        self.app_data = Data(
            world = None,
            camera = None
        )

        self.state = 0

        self.substate = 0

        self.quit = False

        self.elements = []

        # self.nextKeybind = None

    def update(self):
        # Audio logic

        # if len(self.data.audio.backgroundQueue) == 0:
        #     if self.state == 0:
        #         self.data.audio.queue(choice(self.assets.MENU_MUSIC), AudioHandler.BACKGROUND)
        #     elif self.state == 1:
        #         self.data.audio.queue(choice(self.assets.GAME_MUSIC), AudioHandler.BACKGROUND)

        # self.data.audio.refresh()

        # playClickSound = False

        for element in self.elements:

            if element.element == 'button':
                element.update(self)

                if element.held:
                    if self.state == 0:
                        pass

                if element.pressed:
                    # playClickSound = True

                    # Button pressing logic is below

                    if self.state == 0:
                        if element.id == 'start':
                            # file_name = file_prompt()
                            # if file_name != '':
                            #     self.app_data.sprite = Sprite(load_layers(file_name), self.app_data.sprite.base_rect if self.app_data.sprite is not None else self.CONSTANTS.DEFAULT_SPRITE_RECT)
                            self.start()

            elif element.element == 'image':
                element.update(self)

            elif element.element == 'slider':
                element.update(self)

                if element.newValue:
                    if self.state == 0:
                        pass
                        # if element.id == 'sprite-scale':
                        #     if self.app_data.sprite is not None:
                        #         scale = 2 ** (int(element.get_value()) - 4)
                        #         self.app_data.sprite.transform(scale=scale)

            elif element.element == 'textinput':
                element.update(self)

        # if playClickSound:
            # self.data.audio.play_sfx(self.assets.SELECT_FX)

        if self.state == 0:
            pass

        elif self.state == 1:
            self.app_data.world.update()
            self.app_data.camera.update()

            if self.data.keyboard.just_pressed('escape'):
                self.menu()

            # if self.data.keyboard.get_key('w'):
            #     self.app_data.camera.move([0, 0, 0.1])
                
            # elif self.data.keyboard.get_key('s'):
            #     self.app_data.camera.move([0, 0, -0.1])

            # temp
            if self.data.keyboard.get_key('a'):
                self.app_data.camera.move([-0.1, 0, 0])
            
            if self.data.keyboard.get_key('d'):
                self.app_data.camera.move([0.1, 0, 0])
                
            if self.data.keyboard.get_key('w'):
                self.app_data.camera.move([0, 0, 0.1])
                
            if self.data.keyboard.get_key('s'):
                self.app_data.camera.move([0, 0, -0.1])
                
            if self.data.keyboard.get_key('up'):
                self.app_data.camera.move([0, 0.05, 0])
                
            if self.data.keyboard.get_key('down'):
                self.app_data.camera.move([0, -0.05, 0])

            if (self.data.keyboard.get_key('right')):
                self.app_data.camera.rotate([0, 0.03, 0])
                
            if (self.data.keyboard.get_key('left')):
                self.app_data.camera.rotate([0, -0.03, 0])
                
            if (self.data.keyboard.get_key('delete')):
                self.app_data.camera.rotate([0.03, 0, 0])
                
            if (self.data.keyboard.get_key('backspace')):
                self.app_data.camera.rotate([-0.03, 0, 0])

    def render(self):
        self.data.displaySurface.fill(self.CONSTANTS.COLOURS.GREY)

        if self.state == 0:
            # self.data.displaySurface.blit(self.assets.MENU_BACKGROUNDS[0], (0,0))
            
            for element in self.elements:
                element.render(self.data.displaySurface)

        elif self.state == 1:
            self.app_data.world.render(self.data.displaySurface)

    def menu(self):
        self.data.mouse.change_visibility(True)
        pygame.event.set_grab(False)

        self.state = 0
        self.substate = 0

        self.elements = []

        data = Data(
            position = [self.CONSTANTS.DISPLAY_SIZE[0] * 0.5, self.CONSTANTS.DISPLAY_SIZE[1] * 0.5],
            id = 'start',
            images = Data(
                inactive = self.assets.BLANK_BUTTONS[0],
                active = self.assets.BLANK_BUTTONS[1]
            ),
            shift = True
        )
        data.load(
            text = [
                Text('START', self.assets.FONTS[0], data.position, scale=self.CONSTANTS.TEXT_SCALE, font_y_offset=self.CONSTANTS.FONT0_Y_OFFSET)
            ]
        )

        self.elements.append(Button(data, self.CONSTANTS))

        # title text

        self.elements.append(Text('3D Polygon Projection Demo', self.assets.TITLE_FONT, [self.CONSTANTS.DISPLAY_SIZE[0]*0.5, self.CONSTANTS.DISPLAY_SIZE[1]*0.15], scale=self.CONSTANTS.TITLE_SCALE))

    def start(self):
        self.data.mouse.change_visibility(False)
        pygame.event.set_grab(True)

        self.state = 1
        self.substate = 0

        self.elements = []

        self.app_data.camera = Camera(display_size=self.CONSTANTS.DISPLAY_SIZE, position=[4, 4, 0], clip=[1,32], flip_y=True)
        self.app_data.world = World(self.app_data.camera)