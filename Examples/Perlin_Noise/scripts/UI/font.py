from scripts.utilities.imgedit import palette_swap, clip

class Font:
    def __init__(self, image, order, COLOURS, overlap=False):
        self.characters = {}
        self.order = order
        self.height = image.get_height()

        # swap must be a list. Each element is iterated over, and if len(element) == 1, colour key of image is set to that, else colour element[0] is swapped to colour element[1]

        # if swap is not None:
        #     while len(swap) > 0:
        #         s = swap.pop(0)
        #         if len(s) > 1:
        #             image = palette_swap(image, s[0], s[1])
        #         else:
        #             image.set_colorkey(s[0])

        width = 0
        count = 0
        
        for x in range(image.get_width()):
            colour = image.get_at((x, 0))

            if colour == COLOURS.RED:
                if width == 0:
                    pass
                else:
                    if overlap:
                        self.characters[order[count]] = clip(image, (x+1)-width, 0, width-1, image.get_height())
                    else:
                        self.characters[order[count]] = clip(image, x-width, 0, width, image.get_height())
                    count += 1
                    width = 0
            elif colour == COLOURS.YELLOW:
                break
            else:
                width += 1