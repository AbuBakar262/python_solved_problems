import threading
import time

start_time = time.perf_counter()


def do_something():
    print("Sleeping")
    time.sleep(1)
    print("Done Sleeping")


threads = []

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finished_time = time.perf_counter()
print("Finished in", round(finished_time-start_time, 2))
