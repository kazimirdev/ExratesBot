import asyncio
import logging
from os import register_at_fork

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.handlers.answer_pln import register_answer_pln
from tgbot.handlers.buy_sell_pln_json import register_get_bs_pln_json
from tgbot.handlers.buy_pln import register_buy_pln
from tgbot.handlers.crypto import register_get_crypto
from tgbot.handlers.crypto_json import register_get_crypto_json
from tgbot.handlers.crypto_xml import register_get_crypro_xml 
from tgbot.handlers.fiat import register_get_fiat
from tgbot.handlers.fiat_json import register_get_fiat_json
from tgbot.handlers.fiat_xml import register_get_fiat_xml
from tgbot.handlers.sell_pln import register_sell_pln
from tgbot.handlers.menu import register_menu
from tgbot.filters.admin import AdminFilter
from tgbot.middlewares.db import DbMiddleware

logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_menu(dp)
    register_buy_pln(dp)
    register_get_bs_pln_json(dp)
    register_get_crypto(dp)
    register_get_crypto_json(dp)
    register_get_crypro_xml(dp)
    register_get_fiat(dp)
    register_get_fiat_json(dp)
    register_get_fiat_xml(dp)
    register_sell_pln(dp)
    register_answer_pln(dp)


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
