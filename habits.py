from tkinter import *

window = Tk()
window.geometry("400x400")
window.resizable(True, True)

time = 1000
count = 0
catcher = 0
pause = False

timer = [00,00,00]

def stopwatch():
    global count
    global timer
    text.config(text=f"{timer[2]}:{timer[1]}:{timer[0]}")
    count += 1
    if count <= time and pause == True:
        timer[0] +=1

        if timer[0] > 59:
            timer[0] = 0
            timer[1] +=1

        if timer[1] > 59:
            timer[1] = 0
            timer[2] +=1
        window.after(1000, stopwatch)
 
def pauseing():
    global pause
    pause = not pause
    print(pause)
    btn.config(text="play")

    if pause:
        btn.config(text="pause")
        stopwatch()

btn = Button(window, text="play", command=pauseing)
btn.pack()

text = Label(window, text=str(count))
text.pack()

window.mainloop()
