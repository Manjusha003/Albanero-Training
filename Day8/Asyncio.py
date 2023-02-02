# Two main components are introduced in Python:

# asyncio which is a Python package that allows an API to run and manage coroutines.
# async/await to help you define coroutines.

import asyncio

# async def count():
#     print(1)
#     await asyncio.sleep(3)
#     print(2)

# asyncio.run(count())


# async def count1():
#     task=asyncio.create_task(count2())
#     print(1)
#     await asyncio.sleep(1)
#     print(2)
#     await task

# async def count2():
#     print(3)
#     await asyncio.sleep(2)
#     print(4)

# asyncio.run(count1())


# async def main():
#     task=asyncio.create_task(count())
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")
#     await task

# async def count():
#     print("three")
#     await asyncio.sleep(2)
#     print("Four")

# asyncio.run(main())


# import asyncio
# import time
# async def say_something(delay, words):
#     print(f"Before {words}")
#     await asyncio.sleep(delay)
#     print(f"After {words}")
# async def main():
#     print(f"Started: {time.strftime('%X')}")
#     await say_something(1, "Task 1")
#     await say_something(2, "Task 2")
#     print(f"Finished: {time.strftime('%X')}")

# asyncio.run(main())


# asyncio.create_task() function which is used to schedule the coroutine for execution


# Coroutines

# import asyncio
# async def mult(first, second):
#     print("Calculating multiplication...")
#     await asyncio.sleep(5)
#     mul = first * second
#     print(f"{first} multiplied by {second} is {mul}")
#     return mul
# async def add(first, second):
#     print("Calculating sum...")
#     await asyncio.sleep(1)
#     sum = first + second
#     print(f"Sum of {first} and {second} is {sum}")
#     return sum

# async def main(first, second):
#     await mult(first, second)
#     await add(first, second)

# asyncio.run(main(10, 20))


# To schedule a coroutine to run in the event loop, we use the asyncio.create_task() function.

import asyncio


async def mult(first, second):
    print("Calculating multiplication...")
    await asyncio.sleep(3)
    mul = first * second
    print(f"{first} multiplied by {second} is {mul}")
    return mul


async def add(first, second):
    print("Calculating sum...")
    await asyncio.sleep(1)
    sum = first + second
    print(f"Sum of {first} and {second} is {sum}")
    return sum


async def main(first, second):
    mult_task = asyncio.create_task(mult(first, second))
    add_task = asyncio.create_task(add(first, second))
    await mult_task
    await add_task
asyncio.run(main(10, 20))


# A Future is a low-level awaitable object that represents the result of an asynchronous computation. It is created by calling the asyncio.Future() function.

# from asyncio import Future
# future = Future()
# print(future.done())
# print(future.cancelled())
# future.cancel()
# print(future.done())
# print(future.cancelled())


# Timeouts
# Use asyncio.wait_for(aw, timeout, *) to set a timeout for an awaitable object to complete. Note that aw here is the awaitable object. This is useful if you want to raise an exception if the awaitable object takes too long to complete. The exception as asyncio.TimeoutError.


async def slow_operation():
    await asyncio.sleep(400)
    print("Completed.")


async def main():
    try:
        await asyncio.wait_for(slow_operation(), timeout=5)
    except asyncio.TimeoutError:
        print("Timed out!")

asyncio.run(main())
