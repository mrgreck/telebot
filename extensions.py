import requests
import json


from config import  keys

class ConvertionException(Exception):
    pass


class Convert:
    @staticmethod
    def get_price(base: str, symbold: str, amount: str):

        if base == symbold:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            BaseTicker = keys[base]
        except KeyError:
            raise ConvertionException(f'Неверно указан данный параметер: {base}')

        try:
            SymboldTicker = keys[symbold]
        except KeyError:
            raise ConvertionException(f'Неверно указан данный параметер: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException('Неверое число валюты')

        if amount < 0:
            raise ConvertionException('Число валюты не может быть отрицательной')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={BaseTicker}&symbols={SymboldTicker}')

        value = json.loads(r.content)['rates'][keys[symbold]] * int(amount)

        return value
