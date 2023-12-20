import requests


class JsonplaPceholderUsers:

    @staticmethod
    def get_users():
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        return response.json()

    def get_email_by_id(self, id: int):
        for user in self.usersList:
            if int(user.get('id')) == id:
                return user.get('email')
        return -1

    def get_phone_by_id(self):
        for user in self.usersList:
            if int(user.get('id')) == id:
                return user.get('phone')
        return -1

    def __new__(cls, *args, **kwargs):
       if not hasattr(cls, 'instance'):
           cls.instance = super().__new__(cls)
           cls.instance.usersList = cls.get_users()
           cls.instance.lastUser = cls.instance.usersList[-1]
           cls.instance.firstUser = cls.instance.usersList[0]
       return cls.instance
