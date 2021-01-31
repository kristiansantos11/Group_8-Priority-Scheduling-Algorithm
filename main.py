# Process class is created to give names to attributes
# Unlike the ones seen on the internet using lists (it's unreadable but efficient code.)
# We tried to make this as readable as possible ;)
# (and yes this takes into account duplicate arrival time AND priority level)
from Process import Process, arrange
from Computation import *

# Initialize process_amount as 0
process_amount = 0
processes = []

arrival_time_zero = False

# In order to ensure that the input is integer and a while loop is enforced to repeat input
# if the previous input is invalid.
while True:
    try:
        process_amount = int(input('Enter number of processes: '))
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
            finished_state = False
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
waiting_queue = list()
ready_queue = list()
process_queue = list()

start_time = list()
exit_time = list()
current_time = 0

# List of processes in a sequence.
# Works like a timestamp of processes.
# FOR SOME ODD REASON.
sequence_of_process = list()

# This is where the processing begins:
while True:
    # Check if a process / processes needs to put to the waiting_queue
    print("Time: " + str(current_time))
    # _ = input("Press any key to continue...")

    # WARNING: THIS FOR LOOP DOES NOT WORK (YET) ==========================
    index_to_remove = list()
    for process in processes:
        if process.arrival_time == current_time:
            index_to_remove.append(processes.index(process))
            ready_queue.append(process)

    for index in sorted(index_to_remove, reverse=True):
        processes.pop(index)

    # DEBUG
    print("Processes left")
    for process in processes:
        print(process)

    print("Processes inside ready queue:")
    for process in ready_queue:
        print(process)
    # WARNING: READ ABOVE. ================================================

    # _ = input("Press any key to continue...")

    # Check if length of waiting queue is more than 1
    if len(ready_queue) >= 1:
        ready_queue.sort(key=lambda x: x.priority)
        # Group the processes according to priority then sort each group according to process_id
        ready_queue = arrange(ready_queue)

    # _ = input("Press any key to continue...")

    if len(process_queue) == 0:
        if len(ready_queue) != 0:
            ready_queue[0].submission_time = current_time
            process_queue.append(ready_queue.pop(0))

        # DEBUG
        #print("Process queue: \n" + str(process_queue[0]))
        #print("Processes left inside ready_queue: ")
        #for process in ready_queue:
        #    print(process)

    """elif len(process_queue) == 1 and len(ready_queue) != 0:
        if ready_queue[0].priority < process_queue[0].priority:
            process_queue[0].completion_time = current_time
            swapped_process = Process(process_queue[0].process_id,
                                      process_queue[0].arrival_time,
                                      process_queue[0].burst_time,
                                      process_queue[0].priority,
                                      process_queue[0].remaining_burst_time,
                                      process_queue[0].submission_time,
                                      process_queue[0].completion_time)
            sequence_of_process.append(swapped_process)
            ready_queue[0].submission_time = current_time
            process_queue.append(ready_queue.pop(0))
            ready_queue.insert(0, process_queue.pop(0))"""


            # DEBUG
            #print("Process queue: \n" + str(process_queue[0]))
            #print("Processes left inside ready_queue: ")
            #for process in ready_queue:
            #    print(process)

    # _ = input("Press any key to continue...")
    # DEBUG
    #print("Before process queue remaining burst time: " + str(process_queue[0].remaining_burst_time))

    if len(process_queue) == 1:
        process_queue[0].remaining_burst_time -= 1

    current_time += 1

    # DEBUG
    #print("After process queue remaining burst time: " + str(process_queue[0].remaining_burst_time))

    # _ = input("Press any key to continue...")

    # If the burst time remaining is 0, then it should swapped out of process_queue
    # Then append the completed process to sequence_of_process
    if len(process_queue) == 1 and process_queue[0].remaining_burst_time == 0:
        process_queue[0].completion_time = current_time
        completed_process = Process(process_queue[0].process_id,
                                    process_queue[0].arrival_time,
                                    process_queue[0].burst_time,
                                    process_queue[0].priority,
                                    process_queue[0].remaining_burst_time,
                                    process_queue[0].submission_time,
                                    process_queue[0].completion_time)
        process_queue.pop(0)
        sequence_of_process.append(completed_process)

        # DEBUG


        # Insert first index process inside waiting queue
        if len(ready_queue) != 0:
            ready_queue[0].submission_time = current_time
            process_queue.append(ready_queue.pop(0))
        elif len(ready_queue) == 0 and len(process_queue) == 0 and len(processes) == 0:
            break

    # _ = input("Press any key to continue...")

print("\n\nSequence of process is now: ")

# Replace this with GANTT chart.
for process in sequence_of_process:
    print(process)

print("\n\n")

print(f"CPU Utilization: {cpu_utilization(sequence_of_process, arrival_time_zero)}")
print(f"Average turnaround time: {average_turnaround_time(sequence_of_process)}")
print(f"Average response time: {average_response_time(sequence_of_process)}")
print(f"Average waiting time: {average_waiting_time(sequence_of_process)}")


