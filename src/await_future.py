#!/usr/bin/env python
"""
Low-level async callback-based code.
Reference: https://docs.python.org/3/library/asyncio-future.html
"""
import asyncio


async def set_after(fut, delay, value):
    """Set value of a Future after a delay."""
    await asyncio.sleep(delay)
    fut.set_result(value)


async def main():
    """Run async code that accepts a Future to set result."""
    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    fut = loop.create_future()

    # Run "set_after()" coroutine in a parallel Task.
    # We are using the low-level "loop.create_task()" API here because
    # we already have a reference to the event loop at hand.
    # Otherwise we could have just used "asyncio.create_task()".
    loop.create_task(set_after(fut, 1, "... world"))

    print("hello ...")

    # Wait until *fut* has a result and print it.
    print(await fut)


asyncio.run(main())
