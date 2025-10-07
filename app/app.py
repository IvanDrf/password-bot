from aiogram import Bot
import logging

from config.config import Config
from app.handlers.handler import Handler


class App:
    def __init__(self, handler: Handler, bot: Bot) -> None:
        self.handler: Handler = handler
        self.bot: Bot = bot

        self.handler.Register_Handlers()

    @classmethod
    async def New(cls, cfg: Config) -> 'App':
        handler: Handler = await Handler.New(cfg)
        bot: Bot = Bot(token=cfg.token)

        return cls(handler, bot)

    async def Run(self) -> None:
        logging.info('bot started successfully')
        await self.handler.dp.start_polling(self.bot)
