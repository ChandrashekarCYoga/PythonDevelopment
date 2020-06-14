import asyncio


async def foo(n):
    await asyncio.sleep(5)  # wait 5s before continuing
    print(f"n: {n}!")


async def hello_world():
    await foo()  # waits for `foo()` to complete
    print("Hello World!")


async def main():
    tasks = [foo(1), foo(2), foo(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())

