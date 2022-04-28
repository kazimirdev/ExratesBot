import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.handlers.echo import register_echo 
from tgbot.handlers import (register_answer_pln,
                            register_buy_pln,
                            register_get_crypto,
                            register_get_crypto_file,
                            register_get_answer_fcd,
                            register_get_fcd,
                            register_get_fiat,
                            register_get_fiat_file,
                            register_get_pln_file,
                            register_write_name_fcd,
                            register_menu,
                            register_sell_pln)
from tgbot.filters.admin import AdminFilter
from tgbot.middlewares.db import DbMiddleware


logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):

    register_menu(dp)
    register_get_crypto(dp)
    register_get_crypto_file(dp)
    register_get_fiat(dp)
    register_get_fiat_file(dp)
    register_write_name_fcd(dp)
    register_get_answer_fcd(dp)
    register_get_fcd(dp)
    register_buy_pln(dp)
    register_sell_pln(dp)
    register_answer_pln(dp)
    register_get_pln_file(dp)

    #register_echo(dp)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
