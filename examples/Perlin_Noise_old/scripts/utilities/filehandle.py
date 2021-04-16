from json import dump, load

def json_open(fp):
    with open(fp, 'r') as f:
        d = load(f)
    return d

def json_save(fp, d):
    with open(fp, 'w+') as f:
        dump(d,f)

def text_open(fp):
    with open(fp, 'r') as f:
        d = [line.replace('\n', '') for line in f.readlines()]
    return d

def text_save(fp, d):
    with open(fp, 'w+') as f:
        f.writelines(d)

def file_prompt():
    import tkinter, tkinter.filedialog
    top = tkinter.Tk()
    top.withdraw()  # hide base tk window
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name