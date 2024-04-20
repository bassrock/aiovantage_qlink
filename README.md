# aiovantage-qlink

aiovantage-qlink is a Python library for interacting with and controlling Vantage QLink home automation controllers via an IP Enabler.

Inspired heavily by the [aiovantage](https://raw.githubusercontent.com/loopj/aiovantage) library.


## Example

```python
from aiovantage_qlink import CommandClient
from aiovantage_qlink.command_client.object_interfaces.load import LoadInterface

async with CommandClient("test") as client:
    loadInterface = LoadInterface(client)
    lightLevel1 = loadInterface.get_level(9051)
```


## Features

- Uses Python asyncio for non-blocking I/O.

## Supported objects types

The following interfaces are currently supported.

| Type          | Description           |
| ------------- | --------------------- |
| Load          | Lights, relays, etc   |
