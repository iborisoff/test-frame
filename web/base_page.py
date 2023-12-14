from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common import TimeoutException
from locator import Locator
from web import constants
from webdriver_manager.chrome import ChromeDriverManager

class Keys:
    ENTER = Keys.ENTER
    ESCAPE = Keys.ESCAPE
    TAB = Keys.TAB

class BasePage:

    def __init__(self) -> None:
        self._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    @property
    def page_title(self) -> None:
        """ Получить заголовок страницы """
        return self._driver.title
    
    @property
    def current_url(self) -> None:
        """ Получить текущий ulr стриницы """
        return self._driver.current_url
    
    @property
    def get_driver(self):
        """ Получить драйвер """
        return self._driver

    def refresh_page(self):
        """ Перезагрузить страницу """
        self._driver.refresh()

    def open_page(self, url):
        """ Открыть станицу по url """
        return self._driver.get(url)

    def find_element(self, locator: Locator, timeout: float = constants.TIMEOUT) -> WebElement:
            """ Получить элемент размещенный в DOM дереве  """  
            
            try:
                  element = WebDriverWait(driver=self._driver, timeout=timeout).until(
                       method=EC.presence_of_element_located((By.XPATH, locator.locator))
                  )
                  return element  
            
            except TimeoutException as e:
                 print(e)
                 return f"Не удалось найти элемент в DOM дереве с локатором {locator.locator} в течение {timeout} секунд"             
            
    def is_element_exist(self, locator: Locator, timeout: float = constants.TIMEOUT) -> bool:
        """ Проверить доступность элемента в DOM дереве """

        try:
                WebDriverWait(driver=self._driver, timeout=timeout).until(
                    method=EC.presence_of_element_located((By.XPATH, locator.locator))
                )
                return True  
        
        except TimeoutException as e:
                print(e)
                return f"Не удалось найти элемент в DOM дереве с локатором {locator.locator} в течение {timeout} секунд" 


    def find_visible_element(self, locator: Locator, timeout: float = constants.TIMEOUT) -> WebElement:
        """ Ожидать присутсвия элемента в DOM дереве страницы """ 

        try: 
            element = WebDriverWait(driver=self._driver, timeout=timeout).until(
                method=EC.visibility_of_element_located((By.XPATH, locator.locator))
            )
            return element
            
        except TimeoutException as e:
            print(e)
            return f"Не удалось найти элемент в DOM дереве с локатором {locator.locator} в течение {timeout} секунд"



                   

