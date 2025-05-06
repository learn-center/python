import threading
import time

# print(threading.current_thread().name)


def print_numbers():
    for i in range(5):
        print(f"{threading.current_thread().name} - {i}")
        time.sleep(1)


t1 = threading.Thread(target=print_numbers, name="custom-thread-1")
t1.start()

t2 = threading.Thread(target=print_numbers, name="custom-thread-2")
t2.start()

# t1.join()
t2.join()

for i in range(5, -1, -1):
    print(f"{threading.current_thread().name} - {i}")
    # time.sleep(3)
