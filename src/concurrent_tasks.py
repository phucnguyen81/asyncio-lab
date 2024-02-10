#!/usr/bin/env python
"""
coroutine for concurrent tasks, see https://docs.python.org/3/library/asyncio-task.html
"""
import asyncio
import time


async def say_after(delay, what):
    """Print something after a delay"""
    await asyncio.sleep(delay)
    print(what)


async def main():
    """Coroutine that runs concurrent tasks"""
    task1 = asyncio.create_task(say_after(2, "a"))
    task2 = asyncio.create_task(say_after(2, "b"))

    print(f"started at {time.strftime('%X')}")

    # Run both tasks concurrently (should take 2 seconds, not 4)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
