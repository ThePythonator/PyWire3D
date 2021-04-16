from pygame import Rect, Surface
from pygame import transform

def clip(surf, x, y, w, h):
    return surf.subsurface(Rect(x,y,w,h)).copy()

def palette_swap(image, old, new):
    copy = Surface(image.get_size())
    copy.fill(new)
    image.set_colorkey(old)
    copy.blit(image, (0,0))
    return copy

def get_list_width(l):
    width = 0
    for i in l:
        width += i.get_width()
    return width

def extract_sprites(image, w, h):
    imgs = []
    
    x = image.get_width()//w
    y = image.get_height()//h

    for iy in range(y):
        for ix in range(x):
            sx = ix*w
            sy = iy*h
            imgs.append(clip(image,sx,sy,w,h))

    return imgs

def rotate(image, angle):
    return transform.rotate(image, angle)

# def multi_rotate(*images, angle):
#     surf = Surface(images[0].get_)