from typing import List


class Process:
    def __init__(self,
                 process_id,
                 arrival_time,
                 burst_time,
                 priority,
                 finished_state
                 ):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.finished_state = finished_state
        self.remaining_burst_time = burst_time

        # Submission time should change depending on the gantt chart
        self.submission_time = arrival_time

        # Completion time should change depending on the gantt chart
        self.completion_time = burst_time

    def __str__(self):
        return f"Process ID: {self.process_id} " \
               f"Arrival Time: {self.arrival_time} " \
               f"Burst Time: {self.burst_time} " \
               f"Priority: {self.priority} " \
               f"Remaining Burst Time: {self.remaining_burst_time} " \
                f"Submission Time: {self.arrival_time}" \
                f"Completion Time: {self.completion_time}"


# Group the processes according to priority then sort each group according to process_id
def arrange(processes: List[Process]):
    duplicated_processes = list()
    priority_unique = set()
    return_list = list()

    for process in processes:
        priority_unique.add(process.priority)
    priority_unique = list(priority_unique)
    priority_unique.sort()

    for priority in priority_unique:
        print(f"For priority: {priority}")
        temp = list()
        for process in processes:
            if process.priority == priority:
                temp.append(process)
        duplicated_processes.append(temp)

    for duplicated_process in duplicated_processes:
        duplicated_process.sort(key=lambda x: x.process_id)

    for duplicated_process in duplicated_processes:
        return_list.extend(duplicated_process)

    return return_list
