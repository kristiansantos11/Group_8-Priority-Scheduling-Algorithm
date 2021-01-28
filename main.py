# Initialize process_amount as 0
process_amount = 0
processes = []

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
    # A list called process is created to store:
    # [process_id, arrival_time, burst_time, priority]
    # I am inclined to use dictionaries however they do not have order.
    # Efficiency calculations are not important anyways (read attached requirements)
    while True:
        try:
            arrival_time = int(input(f"Enter arrival time of process {str(amount)}: "))
            burst_time = int(input(f"Enter burst time of process {str(amount)}: "))
            priority = int(input(f"Enter priority number of process {str(amount)}: "))
            processes.append([amount, arrival_time, burst_time, priority])
            break
        except ValueError:
            print("Please enter a valid integer.")
            continue




