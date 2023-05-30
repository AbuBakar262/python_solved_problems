import concurrent.futures
import time

start_time = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping for {seconds} Second(s)...")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs]
    #
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

finished_time = time.perf_counter()
print("Finished in", round(finished_time-start_time, 2), "second(s)...")
