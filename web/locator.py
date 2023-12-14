

class Locator:

    def __init__(self, name: str, locator: str):
        self.__name = name
        self.__locator = locator

    @property
    def locator(self):
        return self.__locator

    @property
    def name(self):
        return self.__name

    def __str__(self) -> str:
        return f"Локатор с названием {self.name}"
    
