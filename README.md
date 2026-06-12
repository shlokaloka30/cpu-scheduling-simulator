# cpu-scheduling-simulator
Python-based CPU Scheduling Simulator implementing FCFS, SJF, and Round Robin algorithms with performance metric analysis.
# CPU Scheduling Simulator

## Overview

CPU Scheduling Simulator is a Python-based project that demonstrates and compares popular CPU scheduling algorithms used in Operating Systems.

The simulator allows users to enter process details such as arrival time and burst time, then evaluates process execution using different scheduling techniques while calculating important performance metrics.

## Features

* First Come First Serve (FCFS) Scheduling
* Shortest Job First (SJF) Scheduling
* Round Robin Scheduling
* Waiting Time Calculation
* Turnaround Time Calculation
* Completion Time Calculation
* Gantt Chart Representation
* Average Performance Analysis

## Algorithms Implemented

### FCFS (First Come First Serve)

Processes are executed in the order they arrive in the ready queue.

### SJF (Shortest Job First)

The process with the shortest burst time is selected for execution.

### Round Robin

Processes are executed in a cyclic manner using a user-defined time quantum.

## Performance Metrics

The simulator calculates:

* Completion Time (CT)
* Waiting Time (WT)
* Turnaround Time (TAT)
* Average Waiting Time
* Average Turnaround Time

## Technologies Used

* Python 3
* Object-Oriented Programming
* Queue Data Structure
* Scheduling Algorithms

## Sample Input

Number of Processes: 4

P1 → Arrival Time = 0, Burst Time = 5

P2 → Arrival Time = 1, Burst Time = 3

P3 → Arrival Time = 2, Burst Time = 8

P4 → Arrival Time = 3, Burst Time = 6

Time Quantum = 2

## Learning Outcomes

* Understanding CPU Scheduling Concepts
* Operating System Process Management
* Queue-based Simulation
* Algorithm Performance Comparison
* Python Programming and OOP

## Future Enhancements

* Priority Scheduling
* Shortest Remaining Time First (SRTF)
* Multilevel Queue Scheduling
* GUI using Tkinter
* Graphical Gantt Chart Visualization
* CSV Report Export

## Author

Shloka Togarllu
