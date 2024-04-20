# This is a sample Python script.
import asyncio
import logging

from aiovantage_qlink import CommandClient
from aiovantage_qlink.command_client.object_interfaces.load import LoadInterface

_LOGGER = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


async def main():
    async with CommandClient("test") as client:
        lightLevel1 = await LoadInterface(client).get_level(9051)
        lightLevel2 = await LoadInterface(client).get_level(1023)
        _LOGGER.debug("lightLevel1 %s", lightLevel1)
        _LOGGER.debug("lightLevel2 %s", lightLevel2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(main())
