from tkinter import *
import math

window = Tk()
window.geometry("400x400")
window.resizable(True, True)

window.update()

def stopwatchMaster(w):
    global time,count,catcher,pause,timer
    time = 1000
    count = 0
    catcher = 0
    pause = False

    timer = [00,00,00,00]

    def stopwatch():
        global count
        global timer
        text.config(text=f"{timer[3]:02d}:{timer[2]:02d}:{timer[1]:02d}")
        if count <= time and pause == True:
            count += 1
            timer[1] +=1
   
            if timer[1] > 59:
                timer[1] = 0
                timer[2] +=1
            if timer[2] > 59:
                timer[2] = 0
                timer[3] +=1
            w.after(1000, stopwatch)
            print(timer[0])

    def pauseing():
        global pause
        pause = not pause
        print(pause)
        btn.config(text="play")

        if pause:
            btn.config(text="pause")
            stopwatch()

    btn = Button(w, text="play", command=pauseing)
    btn.pack()

    text = Label(w, text="00:00:00")
    text.pack()

def timerMaster(w):
    global timeT,countT,pauseT,timerT
    timeT = 0
    countT = 100000
    pauseT = False

    timerT = [00,00,00]

    timerT[2] = math.floor(countT/3600)
    timerT[1] = math.floor((countT%3600)/60)
    timerT[0]= (countT%3600)%60


    def stopwatch():
        global countT
        global timerT
        text.config(text=f"{timerT[2]:02d}:{timerT[1]:02d}:{timerT[0]:02d}")
        if countT > 0 and pauseT == True:
            countT -= 1
            timerT[0] -= 1
            if timerT[0] < 0:
                timerT[0] = 59
                timerT[1] -=1

            if timerT[1] < 0:
                timerT[1] = 59
                timerT[2] -=1
            w.after(1000, stopwatch)
    
    def pauseing():
        global pauseT
        pauseT = not pauseT
        print(pauseT)
        btn.config(text="play")

        if pauseT:
            btn.config(text="pause")
            stopwatch()

    btn = Button(w, text="playT", command=pauseing)
    btn.pack()

    text = Label(w, text=f"{timerT[2]}:{timerT[1]}:{timerT[0]}")
    text.pack()


stopwatchMaster(window)
timerMaster(window)
    

window.mainloop()

