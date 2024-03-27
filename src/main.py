import asyncio
import logging
import sys

from bot.main import bot  # , dp
from temp_dispatcher import dp


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
