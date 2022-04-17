from .privat_chat import IsPrivate
from .admin import dp
from loader import dp

#  Привязка фильтра
if __name__ == "filters":
    dp.filters_factory.bind(IsPrivate)

