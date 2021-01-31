from typing import List
from Process import Process


def average_turnaround_time(processes: List[Process]):
    total_turnaround_time = 0
    for process in processes:
        total_turnaround_time += (process.completion_time - process.arrival_time)
    return total_turnaround_time / len(processes)


def average_response_time(processes: List[Process]):
    total_response_time = 0
    for process in processes:
        total_response_time += (process.submission_time - process.arrival_time)
    return total_response_time / len(processes)


def average_waiting_time(processes: List[Process]):
    total_average_waiting_time = 0
    for process in processes:
        total_average_waiting_time += ((process.completion_time - process.arrival_time) - process.burst_time)
    return total_average_waiting_time / len(processes)


def cpu_utilization(processes: List[Process], arrival_time_zero = True):
    if arrival_time_zero:
        return 1 - (processes[0].arrival_time/processes[-1].completion_time)
    else:
        total_burst_time = 0
        for process in processes:
            total_burst_time += process.burst_time
        return round((total_burst_time/processes[-1].completion_time) * 100, 2)
