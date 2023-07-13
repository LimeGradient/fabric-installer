import os
import platform
import tkinter as tk

window = tk.Tk()
window.title("fabric-installer")
window.geometry("326x240")

dirNameVar = tk.StringVar()
modidVar = tk.StringVar()
groupidVar = tk.StringVar()

def run():
    dir_name = dirNameVar.get()
    mod_id = modidVar.get()
    group_id = groupidVar.get()

    if platform.system() != "Windows":
        os.system(f"./fabric-installer-mac.exe {dir_name} {mod_id} {group_id}")
    else:
        os.system(f"fabric-installer-win.exe {dir_name} {mod_id} {group_id}")

    exit()

dirNameLabel = tk.Label(window, text="Main Folder Name")
dirName = tk.Entry(window, textvariable=dirNameVar)

modidLabel = tk.Label(window, text="Mod ID")
modid = tk.Entry(window, textvariable=modidVar)

groupidLabel = tk.Label(window, text="Group ID")
groupid = tk.Entry(window, textvariable=groupidVar)

sub_btn = tk.Button(window, text="Run", command=run)

dirNameLabel.grid(row=0,column=0)
dirName.grid(row=0,column=1)
modidLabel.grid(row=1,column=0)
modid.grid(row=1,column=1)
groupidLabel.grid(row=2,column=0)
groupid.grid(row=2,column=1)
sub_btn.grid(row=3,column=1)

window.mainloop()