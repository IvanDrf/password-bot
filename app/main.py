from config import Config
from aiogram import Bot
from handlers.commands import Handler
from handlers.handlers import Handler
import asyncio


async def main() -> None:
    cfg: Config = Config()

    Handler.Register_Handlers()

    bot: Bot = Bot(token=cfg.token)

    await Handler.dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
