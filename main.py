import processes_scheduling as pros



if __name__ == '__main__':
    startTimeMean = 7
    timeMean = 30
    standardDeviation = 5
    amount = 1000
    processes = []
    fifo = []
    sjf = []
    rr2 = []
    srtf = []
    rr10 = []
    # open_from_file
    filePath='TESTY\\Procesy\\STMean=7 BT=30 SD=5\\10\\10'
    processesStartTime = [0,2,2,3,5,7,9,9,10,14]
    processesBurstTime = [10,5,4,7,5,11,10,3,13,4]

    # processesStartTime = importList(filePath + '\\1000 CHWILA STARTU')
    # processesBurstTime = importList(filePath + '\\1000 CZAS WYKONYWANIA')
    for i in range (len(processesStartTime)):
        fifo.append(pros.Process(processesStartTime[i],processesBurstTime[i],i+1))
        sjf.append(pros.Process(processesStartTime[i],processesBurstTime[i],i+1))
        srtf.append(pros.Process(processesStartTime[i],processesBurstTime[i],i+1))
        rr2.append(pros.Process(processesStartTime[i],processesBurstTime[i],i+1))
        rr10.append(pros.Process(processesStartTime[i],processesBurstTime[i],i+1))
    print('X')
    fifo, graphFIFO = pros.fcfs(fifo)
    srtf, graphSRTF = pros.srtf(srtf)
    sjf, graphSJF = pros.sjf(sjf)
    rr2, graphRR2 = pros.roundRobin(rr2, 2)
    rr10, graphRR10 = pros.roundRobin(rr10, 10)
    print('FIFO')
    pros.summary(fifo)
    pros.printGraph(graphFIFO)
    print('SJF')
    pros.summary(sjf)
    pros.printGraph(graphSJF)
    print('RR q=2')
    pros.summary(rr2)
    print('RR q=10')
    pros.summary(rr10)

