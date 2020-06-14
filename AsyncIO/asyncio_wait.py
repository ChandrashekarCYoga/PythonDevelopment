import asyncio
from random import randrange


# wait
#
# The following example uses the FIRST_COMPLETED option, meaning whichever
# task finishes first is what will be returned.

async def foo(n):
    s = randrange(5)
    print(f"{n} will sleep for: {s} seconds")
    await asyncio.sleep(s)
    print(f"n: {n}!")


async def main():
    tasks = [foo(1), foo(2), foo(3)]
    result = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(result)


asyncio.run(main())
