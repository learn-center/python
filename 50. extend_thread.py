from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"Thread {self.name} is starting")
        time.sleep(2)
        print(f"Thread {self.name} is finishing")


t1 = MyThread("T1")
t2 = MyThread("T2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Main thread completed")
