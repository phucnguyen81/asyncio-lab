#!/usr/bin/env python
"""
Concurrent group of tasks,
see https://docs.python.org/3/library/asyncio-task.html
"""
import asyncio
import time


async def say_after(delay, what):
    """Print something after a delay"""
    await asyncio.sleep(delay)
    print(what)


async def main():
    """Run concurrent tasks in a task group"""
    async with asyncio.TaskGroup() as tg:
        tg.create_task(say_after(1, "a"))
        tg.create_task(say_after(1, "b"))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
