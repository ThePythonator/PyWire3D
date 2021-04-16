class Keyboard:
    KEY_DOWN = 0
    KEY_UP = 1

    def __init__(self, CONSTANTS):
        self.keys = {}
        self.keybinds = CONSTANTS.DEFAULT_SETTINGS['keybinds'] # is updated later to be settings.keybinds
        self.justPressed = []
        self.unicodePressed = []

    def refresh(self):
        self.justPressed = []
        self.unicodePressed = []

    def add_event(self, keyPressType, key):
        if keyPressType == Keyboard.KEY_DOWN:
            self.keys[key] = True
            self.justPressed.append(key)
        elif keyPressType == Keyboard.KEY_UP:
            self.keys[key] = False
        else:
            raise self.InvalidKeyPressTypeError('{} keyPressType does not exist'.format(keyPressType))

    def add_unicode(self, uni):
        self.unicodePressed.append(uni)

    def get_key(self, action):
        return self.keys.get(self.keybinds[action], False)

    def just_pressed(self, action):
        return self.keybinds[action] in self.justPressed

    class InvalidKeyPressTypeError(Exception):
        pass