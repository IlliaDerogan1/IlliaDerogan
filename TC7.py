import random
import threading
from time import time, sleep
from datetime import datetime

N = 3
P = 10

T1 = 2 # sec
T2 = 5 # sec

# time to check pacient
T3 = 10  # from
T4 = 15  # to

doctors_time = [random.randint(T3, T4) for i in range(N)]  # Час за який конктретний доктор приймає пацієнта
doctors_on_work = [False] * N  # якщо в доктора є клієнт то True, якщо він вільний то False

counter = 0 # number of pacient

def hospital():
    global counter
    th = []

    time_to_next = random.randint(T1, T2)
    last_time = datetime.now()
    while counter<P:

        if (datetime.now()-last_time).seconds >= time_to_next:
            t = threading.Thread(target=pacient_work)
            th.append(t)
            t.start()
            time_to_next = random.randint(T1, T2)
            last_time = datetime.now()
            counter += 1


def pacient_work():
    global doctors_on_work
    try_to_find_doctor = True
    my_doctor_number = None

    pacient_number = counter

    print(f"pacient {pacient_number} come")

    while True:
        if try_to_find_doctor:
            print(f"pacient {pacient_number} try to find doctor")
            for i in range(N):
                if not doctors_on_work[i]:
                    doctors_on_work[i] = True
                    my_doctor_number = i
                    try_to_find_doctor = False
                    break
            sleep(1)
        else:
            print(f"pacient {pacient_number} in cabinet")
            sleep(doctors_time[my_doctor_number])
            doctors_on_work[my_doctor_number] = False
            print(f"pacient {pacient_number} out")
            return






if __name__ == "__main__":
    hospital()
