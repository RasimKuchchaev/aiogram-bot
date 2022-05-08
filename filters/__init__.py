from aiogram import Dispatcher

from loader import dp
from .admins import AdminFilter
from .group_chat import IsGroup


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)