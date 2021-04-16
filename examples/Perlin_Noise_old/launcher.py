if __name__ == '__main__':
    import sys
    from os.path import dirname, join

    if getattr(sys, 'frozen', False):
        execPath = '' # this means all imports are relative
    else:
        execPath = dirname(__file__)
        sys.path.insert(0, execPath)
        sys.path.insert(0, join(execPath,'..','..','src'))

    from scripts.main.main import main

    main(execPath)