from config import Config
from aiogram import Bot
from handlers.commands import Handler
from handlers.handlers import Handler
import asyncio


Handler.Register_Handlers()


async def main() -> None:
    cfg: Config = Config()

    bot: Bot = Bot(token=cfg.token)

    await Handler.dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
