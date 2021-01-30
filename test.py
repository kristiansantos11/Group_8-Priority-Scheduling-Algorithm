from Process import Process, arrange

processes = [Process(5, 0, 1, 2, False),
             Process(2, 0, 1, 1, False),
             Process(3, 0, 1, 1, False),
             Process(1, 0, 1, 2, False),
             Process(6, 0, 1, 2, False),
             Process(7, 0, 1, 1, False),
             Process(4, 0, 1, 1, False)]

processes = arrange(processes)
another_list = list()
index_to_remove = list()

print("In processes..")
for process in processes:
    print(process)

for process in processes:
    if process.priority == 2:
        another_list.append(process)
        index_to_remove.append(processes.index(process))
    print(processes.index(process))

for index in sorted(index_to_remove, reverse=True):
    processes.pop(index)

print("In processes..")
for process in processes:
    print(process)

print("In duplicated processes")
for process in another_list:
    print(process)

#duplicated_processes = arrange(processes)
#for process in duplicated_processes:
#    print(process)

#print("Before popping")
#for process in processes:
#    duplicated_processes.append(processes.pop(processes.index(process)))
#print(len(processes))
#print("After popping")
#for process in duplicated_processes:
#    print(process)

#for process in processes:
#    current_priority = process.priority
#    for current in processes:
#        if current.priority == current_priority:
#            duplicated_processes.append(processes.pop(processes.index(current)))
