import concurrent.futures

THREAD_POOL = concurrent.futures.ThreadPoolExecutor(max_workers=5)


def slow_op(*args):
    with open("/dev/urandom", "rb") as f:
        return f.read(100000)


def do_something():
    future = THREAD_POOL.submit(slow_op, "a", "b", "c")

    THREAD_POOL.shutdown()

    assert future.done() and not future.cancelled()

    print(f"got the result from slow_op: {len(future.result())}")


if __name__ == "__main__":
    print("program started")
    do_something()
    print("program complete")