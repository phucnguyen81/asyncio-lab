#!/usr/bin/env python
"""
Multiple async function calls in the same context,
see https://docs.python.org/3/library/asyncio-task.html
"""
import asyncio


async def hello():
    """Print "hello" after a delay"""
    await asyncio.sleep(2)
    print("hello")


async def world():
    """Print "world" after a delay"""
    await asyncio.sleep(2)
    print("world")


with asyncio.Runner() as runner:
    runner.run(hello())
    runner.run(world())
