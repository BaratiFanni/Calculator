from tkinter import messagebox

def failedWriteFile(ex):
    messagebox.showerror("Hiba", f"Nem sikerült a fájlba írás: {ex}")


def valueError():
    messagebox.showerror("Érvénytelen bemenet", "Érték beli hiba")


def zeroDiv():
    messagebox.showerror("Hiba", "0-val caló osztás nem értelmezett")
