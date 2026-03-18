import threading

buffer = []
capacity = 3
mutex = threading.Lock()

def producer():
    item = 1
    while item <= 5:
        with mutex:
            if len(buffer) < capacity:
                buffer.append(item)
                print("Produced:", item, "| Buffer:", buffer)
                item += 1

def consumer():
    count = 5
    while count > 0:
        with mutex:
            if buffer:
                item = buffer.pop(0)
                print("Consumed:", item, "| Buffer:", buffer)
                count -= 1

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()