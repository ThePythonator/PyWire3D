from os.path import join

from pygame.image import load as image_load
from pygame.mixer import Sound
from pygame.transform import scale as image_scale
from pygame import error as pygame_error

from scripts.UI.font import Font

from scripts.utilities.data import Data
from scripts.utilities.imgedit import extract_sprites, palette_swap
from scripts.utilities.filehandle import json_open

def load_image(path, scale=1, colourkey=None):
    # set colourkey to None if convert_alpha() is to be used
    # set colourkey to a list of tuples/lists if convert() and set_colourkey() is to be used
    if colourkey is None:
        image = image_load(path).convert_alpha()
    else:
        image = image_load(path).convert()

        while len(colourkey) > 0:
            s = colourkey.pop(0)
            if len(s) > 1:
                image = palette_swap(image, s[0], s[1])
            else:
                image.set_colorkey(s[0])

    if scale != 1 and scale > 0:
        size = image.get_size()
        image = image_scale(image,[int(size[0]*scale),int(size[1]*scale)])

    return image


class Assets:
    def __init__(self, CONSTANTS):

        self.MENU_BACKGROUNDS = []

        self.FONTS = []

        self.BLANK_BUTTONS = []
        self.SLIDER_IMAGES = []

        self.CLICK_SOUND = None

        # self.CURSOR_IMAGE = None
        self.TEXT_CURSOR_IMAGE = None

        self.load(CONSTANTS)
    
    def load(self, CONSTANTS):

        for path in CONSTANTS.FILES.MENU_BACKGROUNDS:
            self.MENU_BACKGROUNDS.append(load_image(join(CONSTANTS.PATHS.IMAGES, path), scale=CONSTANTS.BACKGROUND_SCALE_FACTOR).convert())

        # Fonts:

        for font in CONSTANTS.FILES.FONTS:
            #25,151,0
            #132,190,39
            self.FONTS.append(Font(load_image(join(CONSTANTS.PATHS.FONTS, font), scale=CONSTANTS.TEXT_SCALE, colourkey=[[(0,0,0),(53,130,130)],[(0,255,0)]]), CONSTANTS.FONT_ORDER, CONSTANTS.COLOURS, overlap=False))

        # other coloured fonts:

        self.FONTS.append(Font(load_image(join(CONSTANTS.PATHS.FONTS, CONSTANTS.FILES.FONTS[0]), scale=CONSTANTS.TITLE_SCALE, colourkey=[[(0,0,0),(221,221,221)],[(0,255,0)]]), CONSTANTS.FONT_ORDER, CONSTANTS.COLOURS, overlap=False))
        self.FONTS.append(Font(load_image(join(CONSTANTS.PATHS.FONTS, CONSTANTS.FILES.FONTS[0]), scale=CONSTANTS.TEXT_SCALE, colourkey=[[(0,0,0),(221,221,221)],[(0,255,0)]]), CONSTANTS.FONT_ORDER, CONSTANTS.COLOURS, overlap=False))        
        # self.FONTS.append(Font(load_image(join(CONSTANTS.PATHS.FONTS, CONSTANTS.FILES.FONTS[0]), scale=CONSTANTS.IMAGE_SCALE_FACTOR, colourkey=[[(0,0,0),(70,115,25)],[(0,255,0)]]), CONSTANTS.FONT_ORDER, CONSTANTS.COLOURS, overlap=False))
        # self.FONTS.append(Font(load_image(join(CONSTANTS.PATHS.FONTS, CONSTANTS.FILES.FONTS[0]), scale=CONSTANTS.IMAGE_SCALE_FACTOR*4, colourkey=[[(0,0,0),(86,133,39)],[(0,255,0)]]), CONSTANTS.FONT_ORDER, CONSTANTS.COLOURS, overlap=False))
        # self.FONTS.append(Font(load_image(join(CONSTANTS.PATHS.FONTS, CONSTANTS.FILES.FONTS[0]), scale=CONSTANTS.IMAGE_SCALE_FACTOR, colourkey=[[(0,0,0),(255,255,255)],[(0,255,0)]]), CONSTANTS.FONT_ORDER, CONSTANTS.COLOURS, overlap=False))
        # self.FONTS.append(Font(load_image(join(CONSTANTS.PATHS.FONTS, CONSTANTS.FILES.FONTS[1]), scale=CONSTANTS.IMAGE_SCALE_FACTOR, colourkey=[[(0,0,0),(255,255,255)],[(0,255,0)]]), CONSTANTS.FONT_ORDER, CONSTANTS.COLOURS, overlap=False))

        # title font
        #207,172,31
        self.TITLE_FONT = Font(load_image(join(CONSTANTS.PATHS.FONTS, CONSTANTS.FILES.FONTS[0]), scale=CONSTANTS.TITLE_SCALE, colourkey=[[(0,0,0),(132,190,39)],[(0,255,0)]]), CONSTANTS.FONT_ORDER, CONSTANTS.COLOURS, overlap=False)

        for path in CONSTANTS.FILES.BLANK_BUTTONS:
            self.BLANK_BUTTONS.append(load_image(join(CONSTANTS.PATHS.IMAGES, path), scale=CONSTANTS.IMAGE_SCALE_FACTOR).convert_alpha())

        for path in CONSTANTS.FILES.SLIDER_IMAGES:
            self.SLIDER_IMAGES.append(load_image(join(CONSTANTS.PATHS.IMAGES, path), scale=CONSTANTS.IMAGE_SCALE_FACTOR).convert_alpha())

        # Text cursor image:
        # self.TEXT_CURSOR_IMAGE = load_image(join(CONSTANTS.PATHS.IMAGES, CONSTANTS.FILES.TEXT_CURSOR_IMAGE), scale=CONSTANTS.IMAGE_SCALE_FACTOR).convert_alpha()
