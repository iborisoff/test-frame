from time import sleep

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from src.core.constants.constants import TIMEOUT
from src.core.exeptions.exeprions import (ClickableElementNotFoundedError,
                                          ElementNotFounderError,
                                          VisibleElementNotFounded,
                                          LocatedElementNotFounded)
from src.core.selenium.locator import Locator


class BasePage:

    def __init__(self) -> None:
        self._driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    @property
    def page_title(self) -> str:
        """ Получить заголовок страница """
        return self._driver.title

    @property
    def current_url(self) -> str:
        """ Получить текущий ulr страницы """
        return self._driver.current_url

    @property
    def driver(self):
        """ Получить драйвер """
        return self._driver

    def refresh_page(self):
        """ Перезагрузить страницу """
        self._driver.refresh()

    def open_page(self, url):
        """ Открыть станицу по url """
        return self._driver.get(url)

    def close_page(self):
        """ Открыть закрыть веб-станицу """
        self._driver.close()

    def wait_timeout(self, timeout: float) -> None:
        self._driver.implicitly_wait(timeout)

    def find_element(self, locator: Locator, timeout: float = TIMEOUT) -> WebElement:
        """ Получить элемент размещенный в DOM дереве  """

        try:
            element = WebDriverWait(driver=self._driver, timeout=timeout).until(
                method=ec.presence_of_element_located(
                    (By.XPATH, locator.locator))
            )
            return element

        except TimeoutException:
            print(
                f"\nНе удалось найти элемент в DOM дереве с локатором {locator.locator} в течение {timeout} секунд")
            raise ElementNotFounderError

    def is_element_exist(self, locator: Locator, timeout: float = TIMEOUT) -> bool:
        """ Проверить доступность элемента в DOM дереве """

        try:
            WebDriverWait(driver=self._driver, timeout=timeout).until(
                method=ec.presence_of_element_located(
                    (By.XPATH, locator.locator))
            )
            return True

        except TimeoutException:
            print(
                f"\nНе удалось найти элемент в DOM дереве с локатором {locator.locator} в течение {timeout} секунд")
            raise LocatedElementNotFounded

    def go_back(self):
        """ Перейти на пердыдущую страницу """
        self._driver.back()

    def go_next(self):
        """ Перейти на слудующую страницу """
        self._driver.forward()

    def find_visible_element(self, locator: Locator, timeout: float = TIMEOUT) -> WebElement:
        """ Ожидать присутсвия элемента в DOM дереве страницы """

        try:
            element = WebDriverWait(driver=self._driver, timeout=timeout).until(
                method=ec.visibility_of_element_located(
                    (By.XPATH, locator.locator))
            )
            return element

        except TimeoutException:
            print(
                f"\nНе удалось найти элемент в DOM дереве с локатором {locator.locator} в течение {timeout} секунд")
            raise VisibleElementNotFounded

    def click_on_element(self, locator: Locator, timeout: float = TIMEOUT) -> None:
        try:
            self.find_element(locator).click()
        except TimeoutException:
            print(
                f"\nНе удалось найти элемент в DOM дереве с локатором {locator.locator} в течение {timeout} секунд")
            raise ClickableElementNotFoundedError
