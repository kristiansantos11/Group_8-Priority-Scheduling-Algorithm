from typing import List
from Utils.Process import Process


class GanttChart:
    def __init__(self, processes: List[Process]):
        self.processes = processes

    def __str__(self):
        begin = f"({self.processes[0].arrival_time}--"

        # You can use self.processes[-1]
        end = f"[P{self.processes[-1].process_id}]--{self.processes[-1].completion_time})"

        between = ""
        for process in self.processes:
            if self.processes.index(process) == (len(self.processes)-1):
                between += end
                break
            between += f"[P{process.process_id}]--{process.completion_time}--"

        return begin + between
