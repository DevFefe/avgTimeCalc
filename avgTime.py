#Autore: Federico Lisio

import sys
from tkinter import *

def euclide(a, b):
    while(b != 0):
        R=a%b
        a=b
        b=R
    return a

class avgTime:
    def __init__(self, jobsNumber, name, duration, time):
        self.jobsNumber = jobsNumber
        self.name = name
        self.duration = duration
        self.time = time

    def approx(self, num, den):
        mcd = euclide(num, den)
        return num / mcd, den / mcd


    def FCFS(self):
        durationCount = 0
        prevDuration = 0
        for i in range(self.jobsNumber-1):
            durationCount += prevDuration + int(self.duration[i]) - int(self.time[i+1])
            prevDuration += int(self.duration[i])
        return self.approx(durationCount, self.jobsNumber)

    def SJF(self):
        for i in range(1, self.jobsNumber, 1):
            for j in range(i, self.jobsNumber, 1):
                if (self.duration[i] > self.duration[j]):
                    self.name[i], self.name[j] = self.name[j], self.name[i]
                    self.duration[i], self.duration[j] = self.duration[j], self.duration[i]
                    self.time[i], self.time[j] = self.time[j], self.time[i]
        return self.FCFS()


    def SRTF(self):
        print()

    def RR(selft):
        print("Ancora non pronto")
        sys.exit()

def main():
    global algorithm
    # Scelta Algorimo
    # algorithm = input("Inserisci algoritmo(FCFS, SJF, SRTF, RR): ")

    jobs = {'name': [], 'duration': [], 'time': [] }
    
    #Creazione finestra e frames
    mainWindow = Tk()

    mainWindow.title(algorithm)

    mainWindow.option_add("*font", "Courier 20")
    
    displayJobsLabel = Frame(mainWindow)
    displayJobs = Frame(mainWindow)

    displayJobsAfterLabel = Frame(mainWindow)
    displayJobsAfter = Frame(mainWindow)

    displayAvgTime = Frame(mainWindow)

    # Lettura dei dati prensi dal file esterno
    Label(displayJobsLabel, text = "Jobs Order Before Execution").pack(padx = 10, pady = (20, 0))

    jobsName = Label(displayJobs, text = "Jobs").grid(column = 0, row = 0)
    spacer = Label(displayJobs, text = "|").grid(column = 1, row = 0)
    jobsDuration = Label(displayJobs, text = " Duration").grid(column = 2, row = 0)
    spacer = Label(displayJobs, text = "|").grid(column = 3, row = 0)
    jobsTime = Label(displayJobs, text = " Time").grid(column = 4, row = 0)

    jobsNumber = 0

    file = open('jobs.txt')

    for i, f in enumerate(file):
        splittedData = f.split()

        jobs['name'].append(splittedData[0])
        jobs['duration'].append(splittedData[1])
        jobs['time'].append(splittedData[2])

        jobsName = Label(displayJobs, text = splittedData[0]).grid(column = 0, row = i+1)
        jobsDuration = Label(displayJobs, text =splittedData[1]).grid(column = 2, row = i+1)
        jobsTime = Label(displayJobs, text = splittedData[2]).grid(column = 4, row = i+1)

        jobsNumber += 1
    displayJobsNumber = Label(displayAvgTime, text = "Lavori totali: " + str(jobsNumber)).pack()

    # Calcolo Tempo Medio
    obj = avgTime(jobsNumber, jobs['name'], jobs['duration'], jobs['time'])

    match algorithm:
        case "FCFS":
            num, den = str(int(obj.FCFS()[0])), str(int(obj.FCFS()[1]))
        case "SJF":
            num, den = str(int(obj.SJF()[0])), str(int(obj.SJF()[1]))
        case "SRTF":
            num, den = str(int(obj.SRTF()[0])), str(int(obj.SRTF()[1]))
        case "RR":
            num, den = str(int(obj.RR()[0])), str(int(obj.RR()[1]))
        case _:
            print("Algortimo non valido")
            sys.exit()

    if den == "1":
        displayTime = Label(displayAvgTime, text = "Tempo medio: " + num).pack()
    else:
        displayTime = Label(displayAvgTime, text = "Tempo medio: " + num + "/" + den + "\nCirca: " + str(round(int(num) / int(den), 1))).pack() 
   
    # Stampa valori dopo algoritmo
    Label(displayJobsAfterLabel, text = "Jobs Order After Execution").pack(padx = 10, pady = (20, 0))


    jobsName = Label(displayJobsAfter, text = "Jobs").grid(column = 0, row = 0)
    spacer = Label(displayJobsAfter, text = "|").grid(column = 1, row = 0)
    jobsDuration = Label(displayJobsAfter, text = " Duration").grid(column = 2, row = 0)
    spacer = Label(displayJobsAfter, text = "|").grid(column = 3, row = 0)
    jobsTime = Label(displayJobsAfter, text = " Time").grid(column = 4, row = 0)

    for i in range(len(jobs['name'])):
        jobsName = Label(displayJobsAfter, text = jobs['name'][i]).grid(column = 0, row = i+1)
        jobsDuration = Label(displayJobsAfter, text = jobs['duration'][i]).grid(column = 2, row = i+1)
        jobsTime = Label(displayJobsAfter, text = jobs['time'][i]).grid(column = 4, row = i+1)

    # Pack dei frame
    displayJobsLabel.pack()
    displayJobs.pack(padx = 20, pady = 20)

    displayJobsAfterLabel.pack()
    displayJobsAfter.pack(padx = 20, pady = 20)

    displayAvgTime.pack(padx = 20, pady = 20)

    mainWindow.mainloop()

def choose_algorithm():
    chooseAlgorithmWindow = Tk()

    chooseAlgorithmWindow.option_add("*font", "Courier 20")

    variable = StringVar(chooseAlgorithmWindow)
    variable.set("---")

    OPTIONS = (
    "FCFS",
    "SJF",
    "SRTF",
    "RR")

    chooseAlgorithm = OptionMenu(chooseAlgorithmWindow, variable, *OPTIONS)
    chooseAlgorithm.pack(padx = 5, pady = 20, side = "left")

    def ok():
        global algorithm
        algorithm = variable.get()
        main()

    button = Button(chooseAlgorithmWindow, text="OK", command=ok)
    button.pack(padx = 5, pady = 20, side = "right")

    chooseAlgorithmWindow.mainloop()

choose_algorithm()
