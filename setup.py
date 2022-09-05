import sys
from cx_Freeze import setup, Executable
import cx_Freeze

#executables= [cx_Freeze.Executable("tkinter1.py")]


exe = Executable(
    script=r"tkinter1.py",
    base="Win32GUI",
    )

setup(
    name = "Mubaarak_Mathematics",
    options= {
        "build.exe": {"includes":["tkinter", "random", "time"],
                    "include_files": [r"C:\Users\rajim\AppData\Local\Programs\Python\Python38-32\DLLs\tcl86t.dll",
                                      r"C:\Users\rajim\AppData\Local\Programs\Python\Python38-32\DLLs\tk86t.dll"]}
        },
    
    version = "0.1",
    description = "An_example",
    executables = [exe]
    )