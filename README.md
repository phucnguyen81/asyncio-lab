# Description

Learn [Python Async IO](https://docs.python.org/3/library/asyncio.html).

## Setup

- Install direnv, pyenv, and go-task
- Run `task init` to initialize the project's environment
- Run `run $module_name` to run a module in the `src` directory

## Terms

- `coroutine`: code that can be scheduled to run later

## `async` keyword

The `async` keyword decorates a function to returns a coroutine.

```python
async def nested():
    return 42
```
