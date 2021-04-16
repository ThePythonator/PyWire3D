from pygame import K_SPACE, K_ESCAPE, K_BACKSPACE, K_DELETE, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m, K_n, K_o, K_p, K_q, K_r, K_s, K_t, K_u, K_v, K_w, K_x, K_y, K_z#, K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9

from pygame import Rect

from os.path import join

from scripts.utilities.data import Data

class Constants:
    def __init__(self, execPath):
        
        self.FLAGS = Data(
        )

        

        self.PATHS = Data(
            EXEC = execPath,
            SAVES = join(execPath,'saves'),
            ASSETS = join(execPath, 'assets'),
            FONTS = join(execPath, 'assets', 'fonts'),
            IMAGES = join(execPath, 'assets', 'images'),
            SPRITE_OBJECTS = join(execPath, 'assets', 'images')
            # MUSIC = join(execPath, 'assets', 'music'),
            # SOUNDS = join(execPath, 'assets', 'sounds')
        )

        self.FILES = Data(
            LOGO = 'scorpion_games.png',
            
            SETTINGS = 'settings.json',

            MENU_BACKGROUNDS = ['menu{}.png'.format(i) for i in range(1)],

            BLANK_BUTTONS = ['button{}.png'.format(i) for i in range(6)],

            SLIDER_IMAGES = ['slider{}.png'.format(i) for i in range(1)],
            
            # CURSOR_IMAGE = 'cursor.png',
            TEXT_CURSOR_IMAGE = 'text-cursor.png',

            CLICK_SOUND = 'click.ogg',

            FONTS = ['font{}.png'.format(i) for i in range(1)]
        )

        self.COLOURS = Data(
            BLACK   = (  7,  0, 14),
            GREY    = ( 56, 71,102),

            RED     = (255,  0,  0),
            GREEN   = (  0,255,  0),
            YELLOW  = (255,255,  0),
        )

        self.IMAGE_SCALE_FACTOR = 4
        self.BACKGROUND_SCALE_FACTOR = 2

        self.DISPLAY_SIZE = [1280,720]

        self.DEFAULT_SIZE = 2 ** 4

        self.APPLICATION_TITLE = '3D Demo'

        # self.MAX_BACKGROUND_CHANNELS = 1
        # self.MAX_SFX_CHANNELS = 9

        self.DEFAULT_SETTINGS = {
            'showfps': True,
            'maxfps': 120,
            'res': [1280,720],
            'fullscreen': False,
            'keybinds': {
                'escape': K_ESCAPE,
                'a': K_a,
                'd': K_d,
                'w': K_w,
                's': K_s,
                'up': K_UP,
                'down': K_DOWN,
                'left': K_LEFT,
                'right': K_RIGHT,
                'backspace': K_BACKSPACE,
                'delete': K_DELETE
            },
            'audio': {
                'music': 0.2,
                'sfx': 0.2
            }
        }

        self.DEFAULT_SPRITE_RECT = Rect(self.DISPLAY_SIZE[0] / 2, self.DISPLAY_SIZE[1] / 2, self.DEFAULT_SIZE, self.DEFAULT_SIZE)

        # self.MAPPED_ALPHABET = {
        #     K_a: 'a',
        #     K_b: 'b',
        #     K_c: 'c',
        #     K_d: 'd',
        #     K_e: 'e',
        #     K_f: 'f',
        #     K_g: 'g',
        #     K_h: 'h',
        #     K_i: 'i',
        #     K_j: 'j',
        #     K_k: 'k',
        #     K_l: 'l',
        #     K_m: 'm',
        #     K_n: 'n',
        #     K_o: 'o',
        #     K_p: 'p',
        #     K_q: 'q',
        #     K_r: 'r',
        #     K_s: 's',
        #     K_t: 't',
        #     K_u: 'u',
        #     K_v: 'v',
        #     K_w: 'w',
        #     K_x: 'x',
        #     K_y: 'y',
        #     K_z: 'z'
        # }

        # self.SETTINGS_MAXFPS_CYCLE_ORDER = [30,60,90,120,180,240]
        # self.SETTINGS_RESOLUTION_CYCLE_ORDER = [[640,360],[960,540],[1280,720],[1920,1080]]

        self.FONT_ORDER = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?.,:;-"\''#' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?-.,()/\\:;\'"#'#' ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?.,:;-'

        self.FONT0_Y_OFFSET = 10
        self.FONT1_Y_OFFSET = 20
        self.FONT2_Y_OFFSET = 5


        self.TEXT_SCALE = 4
        self.TITLE_SCALE = self.TEXT_SCALE
        
        
        self.LOWER_UPPER_ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ'

        self.KEY_DELAYS = Data(
            INITIAL = 0.5,
            REPEAT = 0.1
        )

        # self.INTERACT_MESSAGE = 'press \'{k_interact}\'' # message display to prompt user to interact

        # self.QUIT_MESSAGE = [
        #     'Are you sure you want to quit?'.upper(),
        #     'All progress in this level will be lost!'.upper()
        # ]

        self.KEY_INPUT_PROMPT = 'Press any key...'#'PRESS ANY KEY...'
        
        self.CURSOR_TIMES = Data(
            ON = 0.6,
            OFF = 0.4
        )
        self.CURSOR_TIMES.TOTAL = self.CURSOR_TIMES.ON + self.CURSOR_TIMES.OFF