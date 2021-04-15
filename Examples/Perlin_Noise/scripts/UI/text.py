from pygame import Rect, Surface

from scripts.utilities.imgedit import get_list_width, rotate

class Text:
    def __init__(self, text, font, position, scale=1, font_y_offset=0, align='center'):
        self.element = 'text'

        self.position = position
        self.y_offset = font_y_offset
        self.align = align

        self.scale = scale

        self.new_text(text, font)

    def new_text(self, text, font):
        self.images = []
        for char in text:
            c = font.characters.get(char)
            if c is not None:
                self.images.append(c)
        # for char,img in font.characters.items():
        #     self.images.append(img)
        if len(self.images) > 0:
            self.rect = Rect((0,0), (get_list_width(self.images)+(len(self.images)-1)*self.scale,self.images[0].get_height()))
        else:
            self.rect = Rect((0,0), (0,0))
            
        if self.align == 'center':
            self.rect.center = self.position
        elif self.align == 'left':
            self.rect.midleft = self.position
        elif self.align == 'right':
            self.rect.midright = self.position
        elif self.align == 'topleft':
            self.rect.topleft = self.position
        else: # in case of invalid align value, default to center
            self.rect.center = self.position

    def new_position(self, position, align='center'):
        self.position = position
        self.align = align

        if self.align == 'center':
            self.rect.center = self.position
        elif self.align == 'left':
            self.rect.midleft = self.position
        elif self.align == 'right':
            self.rect.midright = self.position
        elif self.align == 'topleft':
            self.rect.topleft = self.position
        else: # in case of invalid align value, default to center
            self.rect.center = self.position
    
    def render(self, display):
        width = 0
        for image in self.images:
            display.blit(image, (self.rect.x+width,self.rect.y+self.y_offset))
            width += image.get_width()+self.scale

def singleline_text(text, font, position, display, scale=1, font_y_offset=0, align='center', returnWidth=False):
    images = []
    for char in text:
        c = font.characters.get(char)
        if c is not None:
            images.append(c)

    width = 0

    if len(images) > 0:
        rect = Rect((0,0), (get_list_width(images)+(len(images)-1)*scale,images[0].get_height()))
        
        if align == 'center':
            rect.center = position
        elif align == 'left':
            rect.midleft = position
        elif align == 'right':
            rect.midright = position
        elif align == 'topleft':
            rect.topleft = position
        else: # in case of invalid align value, default to center
            rect.center = position

        
        for image in images:
            display.blit(image, (rect.x+width,rect.y+font_y_offset))
            width += image.get_width()+scale
    
    if returnWidth:
        return width

def multiline_text(text, font, position, display, scale=1, font_y_offset=0, align='center', lineGap=0):
    lines = text.split('\n')
    for i,line in enumerate(lines):
        pos = [position[0], position[1]+(lineGap+font.height)*i]
        singleline_text(line, font, pos, display, scale=scale, font_y_offset=font_y_offset, align=align)

def get_text_width(text, font, scale=1):
    width = 0
    for char in text:
        c = font.characters.get(char)
        if c is not None:
            width += c.get_width()+scale

    return width