#Autore: Federico Lisio

import sys
from tkinter import *
import random
from avgTimeClass import avgTime



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

    for i in range(obj.jobsNumberDuringEx):
        jobsName = Label(displayJobsAfter, text = obj.name[i]).grid(column = 0, row = i+1)
        jobsDuration = Label(displayJobsAfter, text = obj.duration[i]).grid(column = 2, row = i+1)
        jobsTime = Label(displayJobsAfter, text = obj.time[i]).grid(column = 4, row = i+1)

    # Gantt
    currentColumn = 0
    # for i in range(len(jobs['name'])):
    #     for j in range(obj.duration[i]):
    #         label = Label(displayGantt,width= 1, bg = obj.color[i] ,borderwidth=1, relief="solid").grid(column=currentColumn, row= 0)
    #         currentColumn += 1
    
    for i in range(obj.jobsNumberDuringEx):
        label = Label(displayGantt, text = obj.name[i],width= obj.duration[i], bg = obj.color[i] ,borderwidth=1, relief="solid").grid(column = currentColumn, row = 0)
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
