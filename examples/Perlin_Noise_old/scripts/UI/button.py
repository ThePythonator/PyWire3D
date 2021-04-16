class Button:
    def __init__(self, data, CONSTANTS):
        self.element = 'button'
        
        # self.DISPLAY_SIZE = CONSTANTS.DISPLAY_SIZE
        self.images = data.images

        self.texts = getattr(data, 'text', [])

        self.id = data.id
        self.name = getattr(data, 'name', self.id)

        self.images.active = getattr(data.images, 'active', self.images.inactive)

        self.shiftWhenActive = getattr(data, 'shift', False)

        self.image = self.images.inactive
        self.rect = self.image.get_rect()
        self.rect.center = data.position

        if self.shiftWhenActive:
            for text in self.texts:
                # set the text position to be in the inactive position
                text.new_position([text.position[0]-text.scale,text.position[1]-text.scale], text.align)

        self.pressed = False

        self.held = False

        self.visible = True

    def move(self, x, y):
        self.rect.centerx += x
        self.rect.centery += y

        for text in self.texts:
            # do not have new align for text, text is already aligned and is moved relatively in this case
            text.new_position([text.rect.centerx+x,text.rect.centery+y])

    def move_to(self, x, y):
        self.rect.center = x, y

        for text in self.texts:
            text.new_position([x, y])

    def update(self, app):
        if self.rect.collidepoint(app.data.mouse.position):
            if self.shiftWhenActive and self.image == self.images.inactive: # causes text to shift down and right only if button has just been inactive
                for text in self.texts:
                    text.new_position([text.position[0]+text.scale,text.position[1]+text.scale], text.align)

            self.image = self.images.active

            if app.data.mouse.left:
                self.held = True

                if app.data.mouse.leftPressed:
                    self.pressed = True
                else:
                    self.pressed = False

            else:
                self.held = False

        else:
            if self.shiftWhenActive and self.image == self.images.active: # causes text to shift up and left only if button has just been active
                for text in self.texts:
                    text.new_position([text.position[0]-text.scale,text.position[1]-text.scale], text.align)

            self.image = self.images.inactive
            self.pressed = False
            self.held = False

    def render(self, display):
        if self.visible:
            display.blit(self.image, self.rect)
            for text in self.texts:
                text.render(display)