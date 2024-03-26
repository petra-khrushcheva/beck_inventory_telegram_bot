import asyncio
import logging
import sys

from bot.dispatcher import dp
from bot.main import bot, storage


async def main() -> None:
    await dp.start_polling(bot=bot, storage=storage)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
