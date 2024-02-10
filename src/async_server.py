#!/usr/bin/env python
"""
An echo server using asyncio.start_server with contextvars.
Reference: https://docs.python.org/3/library/contextvars.html
"""
import asyncio
import contextvars

# Create a context variable not yet bound to any thread
client_addr_var = contextvars.ContextVar("client_addr")


def render_goodbye():
    """Say goodbye to the current client."""
    # The address of the currently handled client can be accessed
    # without passing it explicitly to this function.

    client_addr = client_addr_var.get()
    return f"Good bye, client @ {client_addr}\n".encode()


async def handle_request(reader, writer):
    """
    Keep echoing messages from the client until getting an empty message.
    """
    addr = writer.transport.get_extra_info("socket").getpeername()
    client_addr_var.set(addr)

    # In any code that we call is now possible to get
    # client's address by calling 'client_addr_var.get()'.

    while True:
        line = await reader.readline()
        print(line)
        if not line.strip():
            break
        writer.write(line)

    writer.write(render_goodbye())
    writer.close()


async def main():
    """Start the server on localhost:8081."""
    server = await asyncio.start_server(handle_request, "127.0.0.1", 8081)

    async with server:
        await server.serve_forever()


asyncio.run(main())

# To test it you can use telnet:
#     telnet 127.0.0.1 8081
