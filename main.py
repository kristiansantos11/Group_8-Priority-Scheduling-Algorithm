# Process class is created to give names to attributes
# Unlike the ones seen on the internet using lists (it's unreadable but efficient code.)
# We tried to make this as readable as possible ;)
# (and yes this takes into account duplicate arrival time AND priority level)
from Computation import *
from GanttChart import GanttChart
from Process import arrange

# Initialize process_amount as 0
process_amount = 0
processes = list()

arrival_time_zero = False

# In order to ensure that the input is integer and a while loop is enforced to repeat input
# if the previous input is invalid.
while True:
    try:
        process_amount = int(input('Enter number of processes: '))
        if process_amount < 2:
            print("There should be at least 2 processes!")
            continue
        else:
            break
    except ValueError:
        print("Please enter a process amount from 2-5\n")
        continue

for amount in range(1, process_amount + 1):

    # FROM KRISTIAN:
    # A list called process is created to store:
    # [process_id, arrival_time, burst_time, priority, finished_state, remaining_burst_time]
    # I am inclined to use dictionaries however they do not have order.
    # Efficiency calculations are not important anyways (read attached requirements)
    # Therefore the program will run in time complexity: O(n^3) = Cubic / Exponential
    # It is inefficient in python, but it is efficient if implemented in a lower level language
    while True:
        try:
            arrival_time = int(input(f"Enter arrival time of process {str(amount)}: "))
            if arrival_time == 0:
                arrival_time_zero = True
            burst_time = int(input(f"Enter burst time of process {str(amount)}: "))
            priority = int(input(f"Enter priority number of process {str(amount)}: "))
            processes.append(Process(amount,
                                     arrival_time,
                                     burst_time,
                                     priority,
                                     burst_time,
                                     arrival_time,
                                     burst_time))
            break
        except ValueError:
            print("Please enter a valid integer.")
            continue

# First, sort the processes according to arrival time.
processes.sort(key=lambda x: x.arrival_time)

# Initialize ready_queue, process_queue and current_time
ready_queue = list()
process_queue = list()
current_time = 0

# List of processes in a sequence.
# Works like a timestamp of processes.
sequence_of_process = list()

# This is where the processing begins:
while True:
    # Check if a process / processes needs to put to the waiting_queue
    # If process inside processes list matches the current time, insert it to the ready_queue
    index_to_remove = list()
    for process in processes:
        if process.arrival_time == current_time:
            index_to_remove.append(processes.index(process))
            ready_queue.append(process)

    # After the processes are appended, these have to be removed from the processes list.
    for index in sorted(index_to_remove, reverse=True):
        processes.pop(index)

    # Check if length of waiting queue is more than 1
    if len(ready_queue) >= 1:
        # Sort the ready_queue according to priority
        ready_queue.sort(key=lambda x: x.priority)
        # Group the processes according to priority then sort each group according to process_id
        ready_queue = arrange(ready_queue)

    # If the process_queue is empty, check if the ready_queue is empty.
    if len(process_queue) == 0:
        # If ready queue is not empty, then insert the first index inside the ready queue
        if len(ready_queue) != 0:
            ready_queue[0].submission_time = current_time
            process_queue.append(ready_queue.pop(0))

    # BURST TIME DEDUCTION STARTS HERE

    # If a process exists inside process_queue, deduct 1 to its remaining burst time
    if len(process_queue) == 1:
        process_queue[0].remaining_burst_time -= 1

    current_time += 1

    # If the burst time remaining is 0, then it should swapped out of process_queue
    # Then append the completed process to sequence_of_process
    if len(process_queue) == 1 and process_queue[0].remaining_burst_time == 0:
        process_queue[0].completion_time = current_time
        # Copy the Process object to another Process object for a saved instance of the completed Process
        # be appended inside the sequence_of_process list.
        completed_process = Process(process_queue[0].process_id,
                                    process_queue[0].arrival_time,
                                    process_queue[0].burst_time,
                                    process_queue[0].priority,
                                    process_queue[0].remaining_burst_time,
                                    process_queue[0].submission_time,
                                    process_queue[0].completion_time)
        process_queue.pop(0)
        sequence_of_process.append(completed_process)

        # Insert first index process inside waiting queue
        if len(ready_queue) != 0:
            ready_queue[0].submission_time = current_time
            process_queue.append(ready_queue.pop(0))
        # If the ready queue, process queue and processes list (or waiting queue) are empty, it means it is finished
        # Then the outermost while loop should be broken to output the gantt chart and the final results
        elif len(ready_queue) == 0 and len(process_queue) == 0 and len(processes) == 0:
            break

# Output the GANTT Chart
print("\n\nGantt Chart: ")
print(GanttChart(sequence_of_process))
print("\n\n")

# Output the Utilization, TAT, ART, AWT.
print(f"CPU Utilization: {cpu_utilization(sequence_of_process, arrival_time_zero)}")
print(f"Average turnaround time: {average_turnaround_time(sequence_of_process)}")
print(f"Average response time: {average_response_time(sequence_of_process)}")
print(f"Average waiting time: {average_waiting_time(sequence_of_process)}")
