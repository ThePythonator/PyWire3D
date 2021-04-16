from scripts.main.window import Window

def main(execPath):
    try:
        window = Window(execPath)
        window.run()
    except Exception as e: # general catch-all to allow displaying of errors encountered
        s = u'{}: {}'.format(e.__class__.__name__,e)
        raise # to remove
        try:
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, s, u'Error', 0)
        except Exception as e:
            print(s)
