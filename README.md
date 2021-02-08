# Group_8-Priority-Scheduling-Algorithm
Group_8-Priority-Scheduling-Algorithm Repository

Requirements:
- Design a program (any programming language of your choice) that will input the following:
> - Number of processes (minimum of 2 and maximum of 5)
>
> - Arrival Time
>
> - Burst Time
>
> - Priority number
- Produce a Gantt Chart ( any form of Gantt chart will be accepted that shows the submission and completion of each processes)
- Compute for the following: (2 decimal places)
>- CPU Utilization
>
>- Average Turnaround Time
>
>- Average response Time
>
>- Average Waiting Time
 
 # Paste this inside the code if you want pre-emptive priority scheduling
 ### Replace the BURST TIME DEDUCTION STARTS HERE comment
    elif len(process_queue) == 1 and len(ready_queue) != 0:
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
            ready_queue.insert(0, process_queue.pop(0))
