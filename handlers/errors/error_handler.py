import logging

from aiogram.types import Update

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """
    from aiogram.utils.exceptions import (Unauthorized, InvalidQueryID, TelegramAPIError,
                                          CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                          MessageTextIsEmpty, RetryAfter,
                                          CantParseEntities, MessageCantBeDeleted, BadRequest)

    if isinstance(exception, CantDemoteChatCreator):
        logging.debug("Can't Demote Chat Creator")
        # do something here?
        return True

    if isinstance(exception, MessageNotModified):
        logging.debug('Message is not modified')
        # do something here?
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.info("Message Cant Be Deleted")
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.info("Message To Delete Not Found")
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.debug("MessageTextIsEmpty")
        return True

    if isinstance(exception, Unauthorized):
        logging.info(f"Unauthorized: {exception}")
        return True

    if isinstance(exception, InvalidQueryID):
        logging.exception(f"InvalidQueryID: {exception} \n Update: {update}")
        return True
      
    if isinstance(exception, CantParseEntities):
        await Update.get_current().message.answer(f"Попало в эррор хендлер.CantParseEntities: {exception.args}")
        return True

    if isinstance(exception, RetryAfter):
        logging.exception(f"RetryAfter: {exception} \n Update: {update}")
        return True
    if isinstance(exception, BadRequest):
        logging.exception(f"BadRequest: {exception} \n Update: {update}")
        return True

    #  MUST BE THE  LAST CONDITION (ЭТО УСЛОВИЕ ВСЕГДА ДОЛЖНО БЫТЬ В КОНЦЕ)
    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True
    
    # At least you have tried.
    logging.exception(f'Update: {update} \n{exception}')
