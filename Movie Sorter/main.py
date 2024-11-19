# Bugs


# init
from src import *
from obj import *


# functions
def write_func():
    global file_loader
    global status
    for movie in file_loader.wlist:
        new_name = str(f'{movie[1]} ({movie[2]})[{movie[3]}]')
        new_path = str(f"upload/{new_name + path.splitext(movie[0])[1]}")
        rename(movie[0],new_path)
    status = False
    startfile('upload')


def find_file():
    global file_path
    global file_year
    global file_res
    resolutions = ['720','1080','2160']
    fp = filedialog.askopenfilename(initialdir='input')
    file_path.set(fp)
    for x in range(1990,2031):
        if str(x) in file_path.get():
            file_year.set(str(x))
            break
        else:
            continue
    for x in resolutions:
        if x in file_path.get():
            if x == '720' or x == '1080':
                file_res.set(f'{x}p')
                break
            else:
                file_res.set('4K')
                break


def add_func():
    global file_loader
    global file_path
    global file_name
    global file_year
    global file_res
    global preview_entry
    found = False
    for paths in file_loader.wlist:
        if file_path.get() in paths:
            found = True
            break
        else:
            found = False
    if not found:
        file_loader.file_build(file_path.get(),file_name.get(),file_year.get(),file_res.get())
        preview_entry.insert(1.0,f"{file_name.get()} ({file_year.get()})[{file_res.get()}]\n")

def rm_func():
    global file_loader
    global preview_entry
    file_loader.wlist.pop()
    preview_entry.delete('1.0','2.0')
    print(file_loader.wlist)


# win config
root = Tk()
screen_height=root.winfo_screenheight()
screen_width=root.winfo_screenwidth()
root.resizable(False,False)
root.title("Movie Sorter V1")
root.geometry(f'1300x825+{int(screen_width/2-650)}+{int(screen_height/2-413)}')
canvas = Canvas(root)
canvas.config(height=825, width=1300, bg='#000000')
canvas.pack()


# vars
file_loader = Loader()
file_path = StringVar()
file_path.set("File Path")
file_name = StringVar()
file_name.set("Name")
file_year = StringVar()
file_year.set("Year")
file_res = StringVar()
file_res.set("Resolution")
status = True


# entries
file_path_entry = Entry(state="readonly",width=100,textvariable=file_path)
file_name_entry = Entry(width=50,textvariable=file_name)
file_year_entry = Entry(width=10,textvariable=file_year)
file_res_entry = Entry(width=10, textvariable=file_res)
preview_entry = Text(height=40,width=100)


# buttons
write_button = Button(text="Write", height=2, width=20, command=write_func)
file_path_button = Button(text="...",height=1,width=2,command=find_file)
add_button = Button(text="Add",height=1,width=20,command=add_func)
rm_button = Button(text="Remove",height=1,width=20,command=rm_func)


# win build
write_button.place(x=1125,y=757)
file_path_button.place(x=625,y=25)
add_button.place(x=1135,y=25)
rm_button.place(x=1135,y=100)

file_path_entry.place(x=10, y=25)
file_name_entry.place(x=675,y=25)
file_year_entry.place(x=980,y=25)
file_res_entry.place(x=1045,y=25)
preview_entry.place(x=10,y=55)



# main loop
while status==True:
    sleep(0.025)
    root.update()
