import asyncio

'''
create_task
The following example demonstrates how to convert 
a coroutine into a Task and schedule it onto the event loop.

'''


async def foo():
    await asyncio.sleep(10)
    print("Foo!")


async def hello_world():
    task = asyncio.create_task(foo())
    print(task)
    await asyncio.sleep(5)
    print("Hello World!")
    await asyncio.sleep(10)
    print(task)


asyncio.run(hello_world())
