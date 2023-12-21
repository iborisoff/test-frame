import random
import string


def generate_random_string(length:int = 10) -> str:
   """ Генератор случайной последовательности символов """
   return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length)).lower()

