#!/usr/bin/env python
"""
Run async coroutine.
Reference: https://docs.python.org/3/library/asyncio-task.html
"""
import asyncio


async def nested():
    """Returns a coroutine."""
    return 42


async def main():
    """The top-level coroutine that calls another one."""
    # Calling "nested()" creates a coroutine but does not run the code
    print(nested())

    # "await" schedules a coroutine to run.
    print(await nested())  # will print "42".


asyncio.run(main())
