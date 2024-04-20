"""Client for communicating with the Vantage QLINK Command service.

The QLink Command service is a text-based service that allows interaction with devices
controlled by a Vantage QLink Controller.

Among other things, this service allows you to change the state of devices
(eg. turn on/off a light) as well as subscribe to status changes for devices.

The service is exposed on port 10001by default.
"""

from .commands import CommandClient

__all__ = [
    "CommandClient",
]