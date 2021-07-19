from cx_Freeze import setup, Executable
target = (Executable(script = "main.py", base = "Win32GUI")
    )
setup(
    name = "Zombies II",
    version = "0.7",
    description = "Zombies II",
    executables = [target]
    )
