import asyncio
from create_bot import bot, dispatcher
from handlers.queue import queue_router
from handlers.start import start_router

async def main():
    dispatcher.include_router(start_router)
    dispatcher.include_router(queue_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())