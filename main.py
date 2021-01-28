import matplotlib
#QWERTRTYUIOPASFGHJKLZCVBNM<ASDFGHJKLQWRTYUIOP
while True:
    try:
        process_amount = int(input('How many process? '))
    except TypeError:
        continue

    for amount in range(1, process_amount + 1):
        print("Process: " + str(amount))

    break


