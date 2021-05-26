"""
example_3.py

Just a short example demonstraing a simple state machine in Python
However, this one has delays that affect it
"""

import time
import queue


import time


def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        t = time.process_time()
        for x in range(count):
            print(f'Task {name} running')
            time.sleep(1)
            total += 1
            yield
        print(f'Task {name} total: {total}')
        elapsed_time = time.process_time() - t
        print(f'Task {name} total elapsed time: {elapsed_time}')


def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [1, 1, 5, 2]:
        work_queue.put(work)


    tasks = [
        task('One', work_queue),
        task('Two', work_queue)
    ]
    # run the scheduler to run the tasks
    tm = time.process_time()
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True

    elapsed_time = time.process_time() - tm
    print(f'Total elapsed time: {elapsed_time}')


if __name__ == '__main__':
    main()