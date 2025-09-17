from app.config import Config
from aiogram import Bot
from app.handlers.handlers import Handler
import asyncio


async def main() -> None:
    cfg: Config = Config()

    handler: Handler = await Handler.New(cfg)
    handler.Register_Handlers()

    bot: Bot = Bot(token=cfg.token)

    await handler.dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
