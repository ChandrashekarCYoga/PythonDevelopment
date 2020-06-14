"""
example_2.py

Simple Cooperative Concurrency

Just a short example demonstrating a simple state machine in Python
"""

import queue

def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        for x in range(count):
            print(f'Task {name} running')
            total += 1
            yield
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
        task('One', work_queue),
        task('Two', work_queue)
    ]

    # run the tasks
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


if __name__ == '__main__':
    main()

"""
The “task” in this program is just a function that accepts a string and a queue. 
When executed it looks to see if there is anything in the queue to process, 
and if so it pulls values off the queue, starts a for loop to count up to that 
value, and prints the total at the end. It continues this till there is nothing 
left in the queue, and exits.

When we run this task we get a listing showing that task one does all the work. 
The loop within it consumes all the work on the queue, and performs it. 
When that loop exits, task two gets a chance to run, but finds the queue empty, 
so it prints a statement to that affect and exits. There is nothing in the code 
that allows task one and task two to play nice together and switch between them.
"""