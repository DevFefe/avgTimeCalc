import copy

def euclide(a, b):
    while(b != 0):
        R=a%b
        a=b
        b=R
    return a

class avgTime:
    def __init__(self, jobsNumber, name, duration, time, color):
        self.jobsNumber = copy.copy(jobsNumber)
        self.jobsNumberDuringEx = copy.copy(jobsNumber)
        self.name = copy.copy(name)
        self.duration = copy.copy(duration)
        self.time = copy.copy(time)
        self.color = copy.copy(color)

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
        return self.approx(totalDuration, self.jobsNumber)
