import asyncio
'''
Callbacks
When dealing with a Task, which really is a Future, 
then you have the ability to execute a ‘callback’ 
function once the Future has a value set on it.

The following example demonstrates this by modifying 
the previous create_task example code:
'''


async def foo():
    await asyncio.sleep(10)
    return "Foo!"


def got_result(future):
    print(f"got the result! {future.result()}")


async def hello_world():
    task = asyncio.create_task(foo())
    task.add_done_callback(got_result)
    print(task)
    await asyncio.sleep(5)
    print("Hello World!")
    await asyncio.sleep(10)
    print(task)


asyncio.run(hello_world())