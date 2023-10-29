import random
import time

zero = False
attempts = 0
heads = 0
total_heads = 0
tails = 0
total_tails = 0
total = 0
largest = 0
first_time = time.time()


while not zero:
    heads = 0
    tails = 0
    for i in range(1*10**6):
        if random.randint(0, 1) == 0:
            heads += 1
            total_heads += 1
        else:
            tails += 1
            total_tails += 1
    dif = abs(heads-tails)
    if dif >= largest:
        largest = dif
    total += dif
    print(dif)
    if not dif:
        zero = True
    # elif dif <= 100:
        # print(dif)
    else:
        attempts += 1

minutes = str(int((str(time.time() - first_time)).split('.', 1)[0]) / 60)
seconds = str(float('.' + (str(minutes).split('.', 1)[1])) * 60)
total_seconds = int((str(time.time() - first_time)).split('.', 1)[0])

print('ZERO!!!!!')
print('Time:', minutes.split('.')[0], "minutes and", seconds.split('.')[0], "seconds")
print('Attempts:', attempts)
print('Attempts per second:', (total_seconds/attempts))
print('Average Differance:', int(total/attempts))
print('Largest Difference:', largest)
print('Total # of Heads:', total_heads)
print('Total # of Tails:', total_tails)
