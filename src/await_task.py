#!/usr/bin/env python
"""
List modules of current package.
Reference: https://docs.python.org/3/library/asyncio-task.html
"""
import asyncio


async def nested():
    """Returns a coroutine."""
    return 42


async def main():
    """A top-level coroutine that calls another one."""
    # Creates a Task **AND** schedules its execution
    task = asyncio.create_task(nested())

    # "task" can be used to cancel the coroutine
    # or wait until it is complete
    await task


asyncio.run(main())
