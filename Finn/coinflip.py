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
digits = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "<5": 0,
}
dif_list = []
four_twenties = 0
first_time = time.time()


# while not zero:
for x in range(10):
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
    total += dif
    dif_list.append(dif)
    done = False
    counter = 0
    while not done:
        if len(str(dif)) >= 5:
            digits["<5"] += 1
        if len(str(dif)) == counter:
            digits[str(counter)] += 1
            done = True
        else:
            counter += 1
    if dif >= largest:
        largest = dif
    if dif == 420:
        four_twenties += 1
    if not dif:
        zero = True
    # elif dif <= 10:
    #     print(dif)
    else:
        attempts += 1
    # print(dif)


minutes = str(int((str(time.time() - first_time)).split('.', 1)[0]) / 60)
seconds = str(float('.' + (str(minutes).split('.', 1)[1])) * 60)
total_seconds = int((str(time.time() - first_time)).split('.', 1)[0])
dif_list.sort()

print('ZERO!!!!!')
print('Time:', minutes.split('.')[0], "minutes and", seconds.split('.')[0], "seconds")
print('Attempts:', attempts)
print('Attempts per second:', (attempts/total_seconds))
print('Average Differance:', int(total/attempts))
print('Largest Difference:', largest)
print('Total # of Heads:', total_heads)
print('Total # of Tails:', total_tails)
print("420's:", four_twenties)
print("Digits:", digits)
print('Differences:', dif_list)
