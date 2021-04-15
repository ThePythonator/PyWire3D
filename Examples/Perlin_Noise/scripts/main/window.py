import pygame

from os.path import join

from sys import exit

# from scripts.audio.audio import AudioHandler

from scripts.app.assets import Assets, load_image
from scripts.app.app import App
from scripts.app.settings import Settings

from scripts.input.keyboard import Keyboard
from scripts.input.mouse import Mouse

from scripts.main.constants import Constants

from scripts.UI.text import singleline_text

from scripts.utilities.data import Data
from scripts.utilities import position

class Window:
    def __init__(self, execPath):

        self.CONSTANTS = Constants(execPath)

        self.data = Data(
            clock = pygame.time.Clock(),
            # audio = AudioHandler(maxBackground=self.CONSTANTS.MAX_BACKGROUND_CHANNELS, maxSfx=self.CONSTANTS.MAX_SFX_CHANNELS),
            mouse = Mouse(self.CONSTANTS),
            keyboard = Keyboard(self.CONSTANTS),
            settings = Settings(self.CONSTANTS)
        )

        self.data.keyboard.keybinds = self.data.settings.keybinds

        self.data.actualDisplaySize = self.data.settings.res.copy()

        # self.data.audio.pre_init(44100, -16, 2, 2**12)
        pygame.init()
        # self.data.audio.init()
        
        self.data.display = pygame.display.set_mode(self.data.settings.res)
        pygame.display.set_caption(self.CONSTANTS.APPLICATION_TITLE)

        self.data.displaySurface = pygame.Surface(self.CONSTANTS.DISPLAY_SIZE, 0, self.data.display)
        
        # display loading logo

        self.data.display.fill(self.CONSTANTS.COLOURS.BLACK)
        logo = load_image(join(self.CONSTANTS.PATHS.IMAGES, self.CONSTANTS.FILES.LOGO),scale=8).convert()
        rect = logo.get_rect()
        rect.center = position.divide2D(self.data.actualDisplaySize, [2,2])
        self.data.display.blit(logo, rect)
        pygame.display.flip()

        pygame.time.wait(1000)

        # load audio volumes:
        
        # self.data.audio.set_channel_volume(AudioHandler.BACKGROUND, self.data.settings.audio['music'])
        # self.data.audio.set_channel_volume(AudioHandler.SFX, self.data.settings.audio['sfx'])


        # self.CONSTANTS.FULLSCREEN_SIZE = pygame.display.list_modes()[0]

        # assets requires pygame.mixer to be initialised
        self.assets = Assets(self.CONSTANTS)

        self.data.mouse.change_visibility(True)
        # self.data.mouse.image = self.assets.CURSOR_IMAGE

        self.app = App(self.data, self.assets, self.CONSTANTS)

        self.app.menu()

    def run(self):
        self.data.clock.tick(self.data.settings.maxfps) # start off the clock - stops the first dt being huge
        while True:
            frameGap = self.data.clock.tick(self.data.settings.maxfps) # frameGap is in ms
            self.data.dt = frameGap/1000 # dt is in s
            # self.data.fps = 1000/frameGap

            self.handle_events()

            self.handle_update()

            self.handle_render()

            pygame.display.flip()
    
    def end(self):
        # self.data.settings.save()
        # self.data.userData.save()
        pygame.quit()
        exit()

    def handle_events(self):
        self.data.keyboard.refresh()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end()
            elif event.type == pygame.KEYDOWN:
                self.data.keyboard.add_event(Keyboard.KEY_DOWN, event.key)
                self.data.keyboard.add_unicode(event.unicode)

            elif event.type == pygame.KEYUP:
                self.data.keyboard.add_event(Keyboard.KEY_UP, event.key)

    def handle_update(self):
        self.data.mouse.update(self.app)
        # self.data.keyboard.update()
        self.app.update()
        if self.app.quit:
            self.end()

    def handle_render(self):
        self.app.render()

        # self.data.mouse.render(self.data.displaySurface)

        if getattr(self.data.settings, 'showfps', False):
            if self.app.state == 0:
                pos = [self.CONSTANTS.DISPLAY_SIZE[0]*0.96, self.CONSTANTS.DISPLAY_SIZE[1]*0.05]
            elif self.app.state == 1:
                pos = [self.CONSTANTS.DISPLAY_SIZE[0]*0.96, self.CONSTANTS.DISPLAY_SIZE[1]*0.05]
            else:
                pos = [0,0]
            
            singleline_text(str(int(self.data.clock.get_fps())), self.assets.FONTS[0], pos, self.data.displaySurface, scale=self.CONSTANTS.TEXT_SCALE)
        
        pygame.transform.scale(self.data.displaySurface, self.data.actualDisplaySize, self.data.display)