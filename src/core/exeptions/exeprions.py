""" Модуль с исключениями для модуля core/selenium/selenium.py """

from src.core.selenium.locator import Locator


class Error(Exception):
    pass


class ElementNotFounderError(Error):

    def __init__(self, locator: Locator, message: str = 'В DOM дереве нет элемента с локатором'):
        self.message = f"{message}: {locator.locator}"
        super().__init__(self.message)


class ClickableElementNotFoundedError(Error):

    def __init__(self, locator: Locator, message: str = 'В DOM дереве нет кликабельного элемента с локатором'):
        self.message = f"{message}: {locator.locator}"
        super().__init__(self.message)


class VisibleElementNotFounded(Error):

    def __init__(self, locator: Locator, message: str = 'В DOM дереве не отобразился элемент с локатором'):
        self.message = f"{message}: {locator.locator}"
        super().__init__(self.message)


class LocatedElementNotFounded(Error):

    def __init__(self, locator: Locator, message: str = 'В DOM дереве нет элемента с локатором'):
        self.message = f"{message}: {locator.locator}"
        super().__init__(self.message)
