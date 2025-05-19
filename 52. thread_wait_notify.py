import threading

count = 0
value_set = False


def Producer(condition):
    global count
    global value_set

    condition.acquire()
    while count < 10:
        if not value_set:
            count += 1
            value_set = True
            print(f"Produced: {count}")
            condition.notify()
        else:
            print("Already produced, waiting for consumption")
            condition.wait()

    condition.release()


def Consumer(condition):
    global count
    global value_set

    with condition:  # syntatic sugar for condition.acquire() and condition.release()
        while count < 10:
            if not value_set:
                print("Waiting for production")
                condition.wait()
            else:
                print(f"Consumed: {count}")
                value_set = False
                condition.notify()


condition = threading.Condition()
t_producer = threading.Thread(target=Producer, args=(condition,))
t_consumer = threading.Thread(target=Consumer, args=(condition,))

t_producer.start()
t_consumer.start()

t_producer.join()
t_consumer.join()

print("Completed")
