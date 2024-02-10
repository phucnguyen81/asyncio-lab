#!/usr/bin/env python
"""
async coroutine, see https://docs.python.org/3/library/asyncio-task.html
"""
import asyncio
import time


async def say_after(delay, what):
    """Print something after a delay"""
    await asyncio.sleep(delay)
    print(what)


async def main():
    """The coroutine to run with asyncio"""
    print(f"started at {time.strftime('%X')}")

    await say_after(1, "hello")
    await say_after(2, "world")

    print(f"finished at {time.strftime('%X')}")


# The shortcut is: asyncio.run(main())
with asyncio.Runner() as runner:
    runner.run(main())
