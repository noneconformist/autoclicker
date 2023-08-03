import tkinter as tk
from tkinter import font
import pyautogui
import threading
import time

window = tk.Tk()
window.title("Autoclicker v 0.1")
window.geometry("220x100")
window.resizable(False, False)
window.configure(bg="black")
window.iconbitmap("help_desk.ico")

#счётчик автокликов
autoclicks = 0

#режим цикла (по умолчанию выключен)
on_autoclicks = False

#остановка цикла
def off_autoclicks():
    global on_autoclicks
    on_autoclicks = False

#сброс счётчика
def autoclicks_reset():
    global autoclicks
    autoclicks = 0
    counter.configure(text = autoclicks)

#after threading
def autoclicks_button():
    global autoclicks
    global on_autoclicks
    while True:
        if on_autoclicks:
            if pyautogui.locateOnScreen("picRepeat4minute.jpg", confidence = 0.9):
                xy = pyautogui.locateCenterOnScreen("picRepeat4minute.jpg", confidence = 0.9)
                time.sleep(0.5)
                pyautogui.click(xy)
                autoclicks += 1
                counter.configure(text = autoclicks)
        else:
            break

#main 
def main():
    global on_autoclicks
    on_autoclicks = True
    threading.Thread(target=autoclicks_button, daemon=True).start()

#кнопки
button1 = tk.Button(window, text = "Start", bg="pale green", width=13, height=2, command = main)
button2 = tk.Button(window, text = "Stop", bg="brown1", width=13, height=2, command = off_autoclicks)
button3 = tk.Button(window, text = "Reset", bg="gold", width=13, height=1, command = autoclicks_reset)

#позиционирование кнопок в окне
button1.place(x=5, y=5)
button2.place(x=115, y=5)
button3.place(x=115, y=52)

#позиционирование счётчика
font2 = font.Font(family = "Arial", size = 12)
counter = tk.Label(text=autoclicks, fg="gold", bg="black", font=font2)
counter.place(x=50, y=55)

#автор
font1 = font.Font(family = "Arial", size = 8)
created_by = tk.Label(text="created by Anton Galkin", fg='IndianRed3', bg="black", font=font1)
created_by.place(x=50, y=82)

if __name__ == "__main__":
    main

#цикл обновления состояний окна
window.mainloop()
