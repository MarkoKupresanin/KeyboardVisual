from pynput import keyboard
import os
import random
from tkinter import *
import webbrowser

root = Tk()



def on_press(key):
    try:
        print('Press: {0}'.format(key.char))
    except AttributeError:
        print('Press: {0}'.format(key))
def on_release(key):
    print('Release: {0}'.format(key))
    if key == keyboard.Key.tab and keyboard.Key.cmd:
        return False
def startKeyboardMonitoring():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

def callback(url):
    webbrowser.open_new(url)

contentTitle = Label(root, text="Keyboard Map:")
activateButton = Button(root, text="Click to START recording keyboard input", command=startKeyboardMonitoring)
deactivationText=Label(root, text="To stop monitoring keystrokes: Cmd+Tab")
githubButton=Button(root, text="See the code", highlightbackground='blue', highlightcolor="blue")





githubButton.bind("<Button-1>", lambda e: callback("https://github.com/MarkoKupresanin/KeyboardVisual"))


contentTitle.grid(row=0, column=20)
activateButton.grid(row=10, column=5)
deactivationText.grid(row=11, column=5)
githubButton.grid(row=0,column=50)



root.geometry("960x540")
root.title("Keyboard Visual")
root.resizable(width=True, height=True)
root.mainloop()
