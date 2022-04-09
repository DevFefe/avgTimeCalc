#Autore: Federico Lisio

import sys
from tkinter import *
import random

def euclide(a, b):
    while(b != 0):
        R=a%b
        a=b
        b=R
    return a

class avgTime:
    def __init__(self, jobsNumber, name, duration, time, color):
        self.jobsNumber = jobsNumber
        self.jobsNumberDuringEx = jobsNumber
        self.name = name
        self.duration = duration
        self.time = time
        self.color = color

    def approx(self, num, den):
        mcd = euclide(num, den)
        return num / mcd, den / mcd


    def FCFS(self):
        durationCount = 0
        prevDuration = 0
        for i in range(len(self.duration)-1):
            durationCount += prevDuration + int(self.duration[i]) - int(self.time[i+1])
            prevDuration += int(self.duration[i])
        return self.approx(durationCount, self.jobsNumber)
   
    def orderByDuration(self):
        for i in range(1, self.jobsNumber, 1):
            for j in range(i, self.jobsNumber, 1):
                if (self.duration[i] > self.duration[j]):
                    self.name[i], self.name[j] = self.name[j], self.name[i]
                    self.duration[i], self.duration[j] = self.duration[j], self.duration[i]
                    self.time[i], self.time[j] = self.time[j], self.time[i]
                    self.color[i], self.color[j] = self.color[j], self.color[i]

    def SJF(self):
        self.orderByDuration()
        return self.FCFS()


    def SRTF(self):
        self.orderByDuration()
        executionTime = 0
        for i in range(self.jobsNumber):
            executionTime += int(self.duration[i])
        currentJobExecutionTime = 0
        jobIndex = 0
        for i in range(executionTime):
            for j in range(jobIndex, self.jobsNumberDuringEx, 1):
                if (self.duration[jobIndex] > self.duration[j] and self.time[j] <= i):
                    for k in range(j, self.jobsNumberDuringEx, 1):
                        if (self.duration[jobIndex] > self.duration[self.jobsNumberDuringEx-1]):
                            self.duration.insert(self.jobsNumberDuringEx, self.duration[jobIndex] - currentJobExecutionTime)
                            self.name.insert(self.jobsNumberDuringEx, self.name[jobIndex])
                            self.time.insert(self.jobsNumberDuringEx, self.time[jobIndex])
                            self.color.insert(self.jobsNumberDuringEx, self.color[jobIndex])
                            self.duration[jobIndex] = currentJobExecutionTime
                            jobIndex += 1
                            currentJobExecutionTime = 0
                            self.jobsNumberDuringEx += 1
                            break
                        elif(self.duration[jobIndex] < self.duration[k] and self.duration[jobIndex] > self.duration[k-1]):
                            self.duration.insert(k, self.duration[jobIndex] - currentJobExecutionTime)
                            self.name.insert(k, self.name[jobIndex])
                            self.time.insert(k, self.time[jobIndex])
                            self.color.insert(k, self.color[jobIndex])
                            self.duration[jobIndex] = currentJobExecutionTime
                            jobIndex += 1
                            currentJobExecutionTime = 0
                            self.jobsNumberDuringEx += 1
                            break
                        # if self.duration[jobIndex] > self.duration[k]:
                        #     self.duration.insert(k+1, self.duration[jobIndex] - currentJobExecutionTime)
                        #     self.name.insert(k+1, self.name[jobIndex])
                        #     self.time.insert(k+1, self.time[jobIndex])
                        #     self.duration[jobIndex] = currentJobExecutionTime
                        #     jobIndex += 1
                        #     currentJobExecutionTime = 0
                        #     break
                    break
            if self.duration[jobIndex] == currentJobExecutionTime:
                jobIndex += 1
                currentJobExecutionTime = 0
            else:
                currentJobExecutionTime += 1
        return self.FCFS() 

    def RR(self):
        timeShare = self.jobsNumber
        # timeShare = 4
        totalDuration = 0
        for i in range(self.jobsNumber):
            if self.duration[i] <= timeShare-1:
                totalDuration += self.duration[i]
            else:
                totalDuration += timeShare
        i = 0
        jobsNumber = self.jobsNumber
        while (i < self.jobsNumberDuringEx):
            if self.duration[i] > timeShare:
                self.name.append(self.name[i])
                self.duration.append(self.duration[i]-timeShare)
                self.time.append(self.time[i])
                self.color.append(self.color[i])
                self.duration[i] = timeShare
                self.jobsNumberDuringEx += 1
            i+=1
            print(i)
        return self.approx(totalDuration, self.jobsNumber)

def main():
    global algorithm
    # Scelta Algorimo
    # algorithm = input("Inserisci algoritmo(FCFS, SJF, SRTF, RR): ")

    jobs = {'name': [], 'duration': [], 'time': [] , 'color': []}
    
    #Creazione finestra e frames
    mainWindow = Tk()

    mainWindow.title(algorithm)

    mainWindow.option_add("*font", "Courier 20")
    
    displayJobsLabel = Frame(mainWindow)
    displayJobs = Frame(mainWindow)

    displayJobsAfterLabel = Frame(mainWindow)
    displayJobsAfter = Frame(mainWindow)

    displayAvgTime = Frame(mainWindow)

    displayGantt = Frame(mainWindow)

    # Lettura dei dati prensi dal file esterno
    Label(displayJobsLabel, text = "Jobs Order Before Execution").pack(padx = 10, pady = (20, 0))

    jobsName = Label(displayJobs, text = "Jobs").grid(column = 0, row = 0)
    spacer = Label(displayJobs, text = "|").grid(column = 1, row = 0)
    jobsDuration = Label(displayJobs, text = " Duration").grid(column = 2, row = 0)
    spacer = Label(displayJobs, text = "|").grid(column = 3, row = 0)
    jobsTime = Label(displayJobs, text = " Time").grid(column = 4, row = 0)
    spacer = Label(displayJobs, text = "|").grid(column = 5, row = 0)
    jobsTime = Label(displayJobs, text = " Color").grid(column = 6, row = 0)

    jobsNumber = 0

    file = open('jobs.txt')

    # Color Generator
    number_of_colors = 10

    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(number_of_colors)]
    
    for i, f in enumerate(file):
        splittedData = f.split()

        jobs['name'].append(splittedData[0])
        jobs['duration'].append(int(splittedData[1]))
        jobs['time'].append(int(splittedData[2]))
        jobs['color'].append(color[i])

        jobsName = Label(displayJobs, text = splittedData[0]).grid(column = 0, row = i+1)
        jobsDuration = Label(displayJobs, text =splittedData[1]).grid(column = 2, row = i+1)
        jobsTime = Label(displayJobs, text = splittedData[2]).grid(column = 4, row = i+1)
        jobsColor = Label(displayJobs, width = 1, bg = color[i]).grid(column = 6, row = i+1)

        jobsNumber += 1
    displayJobsNumber = Label(displayAvgTime, text = "Lavori totali: " + str(jobsNumber)).pack()

    # Calcolo Tempo Medio
    obj = avgTime(jobsNumber, jobs['name'], jobs['duration'], jobs['time'], jobs['color'])

    match algorithm:
        case "FCFS":
            num = obj.FCFS()
        case "SJF":
            num = obj.SJF()
        case "SRTF":
            num = obj.SRTF()
        case "RR":
            num = obj.RR()
        case _:
            print("Algortimo non valido")
            sys.exit()

    if num[1] == 1:
        displayTime = Label(displayAvgTime, text = "Tempo medio: " + str(int(num[0]))).pack()
    else:
        displayTime = Label(displayAvgTime, text = "Tempo medio: " + str(int(num[0])) + "/" + str(int(num[1])) + "\nCirca: " + str(round(int(num[0]) / int(num[1]), 1))).pack() 
   
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

    # Gantt
    currentColumn = 0
    # for i in range(len(jobs['name'])):
    #     for j in range(obj.duration[i]):
    #         label = Label(displayGantt,width= 1, bg = obj.color[i] ,borderwidth=1, relief="solid").grid(column=currentColumn, row= 0)
    #         currentColumn += 1
    
    for i in range(len(jobs['name'])):
        label = Label(displayGantt, text = obj.name[i],width= 2 * obj.duration[i], bg = obj.color[i] ,borderwidth=1, relief="solid").grid(column = currentColumn, row = 0)
        currentColumn += 1


    # Pack dei frame
    displayJobsLabel.pack()
    displayJobs.pack(padx = 20, pady = 20)

    displayJobsAfterLabel.pack()
    displayJobsAfter.pack(padx = 20, pady = 20)

    displayAvgTime.pack(padx = 20, pady = 20)

    displayGantt.pack(padx = 20, pady = 20)

    mainWindow.mainloop()

def choose_algorithm():
    chooseAlgorithmWindow = Tk()

    chooseAlgorithmWindow.title("")

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
