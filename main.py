import asyncio

from config.config import Config
from app.app import App

async def main() -> None:
    cfg: Config = Config.New()

    app :App = await App.New(cfg)
    await app.Run()


if __name__ == '__main__':
    asyncio.run(main())
