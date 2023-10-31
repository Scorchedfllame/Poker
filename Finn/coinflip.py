import random
import time
import threading


def till_zero1():
    zero1 = False
    attempts1 = 0
    heads1 = 0
    total_heads1 = 0
    tails1 = 0
    total_tails1 = 0
    total1 = 0
    largest1 = 0
    digits1 = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "<5": 0,
    }
    dif_list1 = []
    four_twenties1 = 0
    first_time1 = time.time()
    #while not zero1:
    for x in range(10):
        heads1 = 0
        tails1 = 0
        for i in range(1*10**6):
            if random.randint(0, 1) == 0:
                heads1 += 1
                total_heads1 += 1
            else:
                tails1 += 1
                total_tails1 += 1
        dif1 = abs(heads1-tails1)
        total1 += dif1
        dif_list1.append(dif1)
        done1 = False
        counter1 = 0
        while not done1:
            if len(str(dif1)) >= 5:
                digits1["<5"] += 1
            if len(str(dif1)) == counter1:
                digits1[str(counter1)] += 1
                done1 = True
            else:
                counter1 += 1
        if dif1 >= largest1:
            largest = dif1
        if dif1 == 420:
            four_twenties1 += 1
        if not dif1:
            zero1 = True
        # elif dif <= 10:
        #     print(dif)
        else:
            attempts1 += 1
        print(f"{1}:  {dif1}")
    minutes1 = str(int((str(time.time() - first_time1)).split('.', 1)[0]) / 60)
    seconds1 = str(float('.' + (str(minutes1).split('.', 1)[1])) * 60)
    total_seconds1 = int((str(time.time() - first_time1)).split('.', 1)[0])
    dif_list1.sort()
    global final1
    final1 = []
    final1.append(zero1)
    final1.append(time.time() - first_time1)
    final1.append(attempts1)
    final1.append(attempts1 / total_seconds1)
    final1.append(int(total1 / attempts1))
    final1.append(largest1)
    final1.append(total_heads1)
    final1.append(total_tails1)
    final1.append(four_twenties1)
    final1.append(digits1)
    final1.append(dif_list1)


def till_zero2():
    zero2 = False
    attempts2 = 0
    heads2 = 0
    total_heads2 = 0
    tails2 = 0
    total_tails2 = 0
    total2 = 0
    largest2 = 0
    digits2 = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "<5": 0,
    }
    dif_list2 = []
    four_twenties2 = 0
    first_time2 = time.time()
    #while not zero2:
    for x in range(10):
        heads2 = 0
        tails2 = 0
        for i in range(1*10**6):
            if random.randint(0, 1) == 0:
                heads2 += 1
                total_heads2 += 1
            else:
                tails2 += 1
                total_tails2 += 1
        dif2 = abs(heads2-tails2)
        total2 += dif2
        dif_list2.append(dif2)
        done2 = False
        counter2 = 0
        while not done2:
            if len(str(dif2)) >= 5:
                digits2["<5"] += 1
            if len(str(dif2)) == counter2:
                digits2[str(counter2)] += 1
                done2 = True
            else:
                counter2 += 1
        if dif2 >= largest2:
            largest2 = dif2
        if dif2 == 420:
            four_twenties2 += 1
        if not dif2:
            zero2 = True
        # elif dif <= 10:
        #     print(dif)
        else:
            attempts2 += 1
        print(f"{2}:  {dif2}")

    minutes2 = str(int((str(time.time() - first_time2)).split('.', 1)[0]) / 60)
    seconds2 = str(float('.' + (str(minutes2).split('.', 1)[1])) * 60)
    total_seconds2 = int((str(time.time() - first_time2)).split('.', 1)[0])
    dif_list2.sort()
    global final2
    final2 = []
    final2.append(zero2)
    final2.append(time.time() - first_time2)
    final2.append(attempts2)
    final2.append(attempts2 / total_seconds2)
    final2.append(int(total2 / attempts2))
    final2.append(largest2)
    final2.append(total_heads2)
    final2.append(total_tails2)
    final2.append(four_twenties2)
    final2.append(digits2)
    final2.append(dif_list2)


def till_zero3():
    zero3 = False
    attempts3 = 0
    heads3 = 0
    total_heads3 = 0
    tails3 = 0
    total_tails3 = 0
    total3 = 0
    largest3 = 0
    digits3 = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "<5": 0,
    }
    dif_list3 = []
    four_twenties3 = 0
    first_time3 = time.time()
    #while not zero3:
    for x in range(10):
        heads3 = 0
        tails3 = 0
        for i in range(1 * 10 ** 6):
            if random.randint(0, 1) == 0:
                heads3 += 1
                total_heads3 += 1
            else:
                tails3 += 1
                total_tails3 += 1
        dif3 = abs(heads3 - tails3)
        total3 += dif3
        dif_list3.append(dif3)
        done3 = False
        counter3 = 0
        while not done3:
            if len(str(dif3)) >= 5:
                digits3["<5"] += 1
            if len(str(dif3)) == counter3:
                digits3[str(counter3)] += 1
                done3 = True
            else:
                counter3 += 1
        if dif3 >= largest3:
            largest3 = dif3
        if dif3 == 420:
            four_twenties3 += 1
        if not dif3:
            zero3 = True
        # elif dif <= 10:
        #     print(dif)
        else:
            attempts3 += 1
        print(f"{3}:  {dif3}")

    minutes3 = str(int((str(time.time() - first_time3)).split('.', 1)[0]) / 60)
    seconds3 = str(float('.' + (str(minutes3).split('.', 1)[1])) * 60)
    total_seconds3 = int((str(time.time() - first_time3)).split('.', 1)[0])
    dif_list3.sort()
    global final3
    final3 = []
    final3.append(zero3)
    final3.append(time.time() - first_time3)
    final3.append(attempts3)
    final3.append(attempts3 / total_seconds3)
    final3.append(int(total3 / attempts3))
    final3.append(largest3)
    final3.append(total_heads3)
    final3.append(total_tails3)
    final3.append(four_twenties3)
    final3.append(digits3)
    final3.append(dif_list3)



#till_zero1()
a = threading.Thread(target=till_zero1)
b = threading.Thread(target=till_zero2)
c = threading.Thread(target=till_zero3)
# # d = threading.Thread(target=till_zero4)
# # e = threading.Thread(target=till_zero5)
# # f = threading.Thread(target=till_zero6)
a.start()
b.start()
c.start()
# # d.start()
# # e.start()
# # f.start()
a.join()
b.join()
c.join()
# # d.join()
# # e.join()
# # f.join()

print(final1)
print(final2)
print(final3)
print('ZERO!!!!!')
# print('Time:', minutes.split('.')[0], "minutes and", seconds.split('.')[0], "seconds")
print('Attempts:', final1[2] + final2[2] + final3[2])
print('Attempts per second:', ((final1[2] + final2[2] + final3[2]) / total_seconds))
print('Average Differance:', int(total/attempts))
print('Largest Difference:', largest)
print('Total # of Heads:', total_heads)
print('Total # of Tails:', total_tails)
print("420's:", four_twenties)
print("Digits:", digits)
print('Differences:', dif_list)

# minutes = str(int((str(time.time() - first_time)).split('.', 1)[0]) / 60)
# seconds = str(float('.' + (str(minutes).split('.', 1)[1])) * 60)
# total_seconds = int((str(time.time() - first_time)).split('.', 1)[0])
# dif_list.sort()
#
# print('ZERO!!!!!')
# print('Time:', minutes.split('.')[0], "minutes and", seconds.split('.')[0], "seconds")
# print('Attempts:', attempts)
# print('Attempts per second:', (attempts/total_seconds))
# print('Average Differance:', int(total/attempts))
# print('Largest Difference:', largest)
# print('Total # of Heads:', total_heads)
# print('Total # of Tails:', total_tails)
# print("420's:", four_twenties)
# print("Digits:", digits)
# print('Differences:', dif_list)

# zero3 = False
#     attempts3 = 0
#     heads3 = 0
#     total_heads3 = 0
#     tails3 = 0
#     total_tails3 = 0
#     total3 = 0
#     largest3 = 0
#     digits3 = {
#         "1": 0,
#         "2": 0,
#         "3": 0,
#         "4": 0,
#         "<5": 0,
#     }
#     dif_list3 = []
#     four_twenties3 = 0
#     first_time3 = time.time()
#     #while not zero3:
#     for x in range(10):
#         heads3 = 0
#         tails3 = 0
#         for i in range(1 * 10 ** 6):
#             if random.randint(0, 1) == 0:
#                 heads3 += 1
#                 total_heads3 += 1
#             else:
#                 tails3 += 1
#                 total_tails3 += 1
#         dif3 = abs(heads3 - tails3)
#         total3 += dif3
#         dif_list3.append(dif3)
#         done3 = False
#         counter3 = 0
#         while not done3:
#             if len(str(dif3)) >= 5:
#                 digits3["<5"] += 1
#             if len(str(dif3)) == counter3:
#                 digits3[str(counter3)] += 1
#                 done3 = True
#             else:
#                 counter3 += 1
#         if dif3 >= largest3:
#             largest3 = dif3
#         if dif3 == 420:
#             four_twenties3 += 1
#         if not dif3:
#             zero3 = True
#         # elif dif <= 10:
#         #     print(dif)
#         else:
#             attempts3 += 1
#         print(f"{3}:  {dif3}")
#
#     minutes3 = str(int((str(time.time() - first_time3)).split('.', 1)[0]) / 60)
#     seconds3 = str(float('.' + (str(minutes3).split('.', 1)[1])) * 60)
#     total_seconds3 = int((str(time.time() - first_time3)).split('.', 1)[0])
#     dif_list3.sort()
#
#     print('ZERO!!!!!')
#     print('Time:', minutes3.split('.')[0], "minutes and", seconds3.split('.')[0], "seconds")
#     print('Attempts:', attempts3)
#     print('Attempts per second:', (attempts3 / total_seconds3))
#     print('Average Differance:', int(total3 / attempts3))
#     print('Largest Difference:', largest3)
#     print('Total # of Heads:', total_heads3)
#     print('Total # of Tails:', total_tails3)
#     print("420's:", four_twenties3)
#     print("Digits:", digits3)
#     print('Differences:', dif_list3)
