"""
example_1.py

Synchronous Programming

Just a short example showing synchronous running of 'tasks'
"""

import queue

def task(name, work_queue):
    if work_queue.empty():
        print(f'Task {name} nothing to do')
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            for x in range(count):
                print(f'Task {name} running')
                total += 1
            print(f'Task {name} total: {total}')


def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # create some tasks
    tasks = [
        (task, 'One', work_queue),
        (task, 'Two', work_queue)
    ]

    # run the tasks
    for t, n, q in tasks:
        t(n, q)

if __name__ == '__main__':
    main()

"""
When we run this task we get a listing showing that task one does all the work. 
The loop within it consumes all the work on the queue, and performs it. 
When that loop exits, task two gets a chance to run, but finds the queue empty, 
so it prints a statement to that affect and exits. There is nothing in the code 
that allows task one and task two to play nice together and switch between them.
"""