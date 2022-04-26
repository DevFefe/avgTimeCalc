#Autore: Federico Lisio

import sys
from tkinter import *
from tkinter import ttk
import random
from avgTimeClass import avgTime

# Colors
color = ['#FFAAA7', '#FFD3B4', '#D5ECC2', '#98DDCA']

def main():

    jobs = {'name': [], 'duration': [], 'time': [] , 'color': []}

    #Creazione finestra e frames
    mainWindow = Tk()

    mainWindow.option_add("*font", "Courier 20")

    # Lettura e Stampa dei dati prensi dal file esterno
    displayJobsLabel = Frame(mainWindow)
    displayJobs = Frame(mainWindow)

    displayAvgTime = Frame(mainWindow)

    displayJobsLabel.pack()
    displayJobs.pack(padx = 20, pady = 20)

    displayAvgTime.pack()

    Label(displayJobsLabel, text = "Jobs Order Before Execution").pack(padx = 10, pady = (20, 0))

    jobsNae = Label(displayJobs, text = "Jobs").grid(column = 0, row = 0)
    spacer = Label(displayJobs, text = "|").grid(column = 1, row = 0)
    jobsDuration = Label(displayJobs, text = " Duration").grid(column = 2, row = 0)
    spacer = Label(displayJobs, text = "|").grid(column = 3, row = 0)
    jobsTime = Label(displayJobs, text = " Time").grid(column = 4, row = 0)
    spacer = Label(displayJobs, text = "|").grid(column = 5, row = 0)
    jobsTime = Label(displayJobs, text = " Color").grid(column = 6, row = 0)

    jobsNumber = 0

    file = open('jobs.txt')

    for i, f in enumerate(file):
        splittedData = f.split()

        jobs['name'].append(splittedData[0])
        jobs['duration'].append(int(splittedData[1]))
        jobs['time'].append(int(splittedData[2]))
        jobs['color'].append(color[i%4])

        jobsName = Label(displayJobs, text = splittedData[0]).grid(column = 0, row = i+1)
        jobsDuration = Label(displayJobs, text =splittedData[1]).grid(column = 2, row = i+1)
        jobsTime = Label(displayJobs, text = splittedData[2]).grid(column = 4, row = i+1)
        jobsColor = Label(displayJobs, width = 1, bg = color[i%4]).grid(column = 6, row = i+1)

        jobsNumber += 1
    displayJobsNumber = Label(displayAvgTime, text = "Lavori totali: " + str(jobsNumber)).pack()

    tabs = ttk.Notebook(mainWindow)
    tabs.pack()

    FCFS_frame = Frame(mainWindow)
    SJF_frame = Frame(mainWindow)
    SRTF_frame = Frame(mainWindow)
    RR_frame = Frame(mainWindow)

    FCFS_frame.pack(fill = BOTH, expand = 1)
    SJF_frame.pack(fill = BOTH, expand = 1)
    SRTF_frame.pack(fill = BOTH, expand = 1)
    RR_frame.pack(fill = BOTH, expand = 1)

    tabs.add(FCFS_frame, text = 'FCFS')
    tabs.add(SJF_frame, text = 'SJF')
    tabs.add(SRTF_frame, text = 'SRTF')
    tabs.add(RR_frame, text = 'RR')

# Algorithms Processing Cicle

    FCFS_obj = avgTime(jobsNumber, jobs['name'], jobs['duration'], jobs['time'], jobs['color'])
    SJF_obj = avgTime(jobsNumber, jobs['name'], jobs['duration'], jobs['time'], jobs['color'])
    SRTF_obj = avgTime(jobsNumber, jobs['name'], jobs['duration'], jobs['time'], jobs['color'])
    RR_obj = avgTime(jobsNumber, jobs['name'], jobs['duration'], jobs['time'], jobs['color'])

    algorithms = {
            'obj': [FCFS_obj, SJF_obj, SRTF_obj, RR_obj],
            'algorithm' : [FCFS_obj.FCFS(), SJF_obj.SJF(), SRTF_obj.SRTF(), RR_obj.RR()],
            'frame': [FCFS_frame, SJF_frame, SRTF_frame, RR_frame]}

    for index, obj in enumerate(algorithms['algorithm']):
        displayJobsAfterLabel = Frame(algorithms['frame'][index])
        displayJobsAfter = Frame(algorithms['frame'][index])

        displayAvgTime = Frame(algorithms['frame'][index])

        displayGantt = Frame(algorithms['frame'][index])

        displayJobsAfterLabel.pack()
        displayJobsAfter.pack(padx = 20, pady = 20)

        displayGantt.pack(side = BOTTOM, padx = 20, pady = 20)

        displayAvgTime.pack(side = BOTTOM)

        #Calcolo Valori Medi
        num = obj

        if num[1] == 1:
            displayTime = Label(displayAvgTime, text = "Tempo medio: " + str(int(num[0]))).pack()
        else:
            displayTime = Label(displayAvgTime, text = "Tempo medio: " + str(int(num[0])) + "/" + str(int(num[1])) + "\nCirca: " + str(round(int(num[0]) / int(num[1]), 1))).pack() 


        Label(displayJobsAfterLabel, text = "Jobs Order After Execution").pack(padx = 10, pady = (20, 0))

        jobsName = Label(displayJobsAfter, text = "Jobs").grid(column = 0, row = 0)
        spacer = Label(displayJobsAfter, text = "|").grid(column = 1, row = 0)
        jobsDuration = Label(displayJobsAfter, text = " Duration").grid(column = 2, row = 0)
        spacer = Label(displayJobsAfter, text = "|").grid(column = 3, row = 0)
        jobsTime = Label(displayJobsAfter, text = " Time").grid(column = 4, row = 0)

        for i in range(algorithms['obj'][index].jobsNumberDuringEx):
            jobsName = Label(displayJobsAfter, text = algorithms['obj'][index].name[i]).grid(column = 0, row = i+1)
            jobsDuration = Label(displayJobsAfter, text = algorithms['obj'][index].duration[i]).grid(column = 2, row = i+1)
            jobsTime = Label(displayJobsAfter, text = algorithms['obj'][index].time[i]).grid(column = 4, row = i+1)
        
        # Gantt
        currentColumn = 0
        for i in range(algorithms['obj'][index].jobsNumberDuringEx):
            label = Label(displayGantt, text = algorithms['obj'][index].name[i],width= 2 * algorithms['obj'][index].duration[i], bg = algorithms['obj'][index].color[i], fg = 'black', borderwidth=1, relief="solid").grid(column = currentColumn, row = 0)
            currentColumn += 1
     

    mainWindow.mainloop()

main()
