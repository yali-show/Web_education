import requests
import config


class Data:
    """
    Get all data and setup of url
    """

    def __init__(self, date, from_one, to_another, bank, url=config.url):
        self.date = date
        self.url = url + self.date
        self.basecurrency = from_one
        self.currency = to_another
        self.bank = bank

        self.purchase = "purchaseRate"
        self.sale = "saleRate"
        self.work = self.__set_up()

    def __set_up(self):
        if self.bank == 'privat':
            self.bank = ''

        self.purchase += self.bank
        self.sale += self.bank

        if self.currency != "UAH" or self.basecurrency != "UAH":
            return False

        return True


class Parser:
    """
    Get data from json and costruct result
    """

    def __init__(self, data):
        if data.work:
            self.currency = data.currency
            self.basecurrency = data.basecurrency
            self.result = f'Не знайдено конвертації {self.basecurrency} в {self.currency}'

        else:
            self.bank = data.bank
            self.date = data.date
            self.url = data.url
            self.currency = data.currency
            self.basecurrency = data.basecurrency
            self.purchase = data.purchase
            self.sale = data.sale
            self.purchaseRate = 0
            self.saleRate = 0
            self.result = f'Курс {self.date} в '

    def get_data(self):
        try:
            response = requests.get(self.url)
            json = response.json()
        except Exception as ex:
            raise KeyError(f"Api error: {ex}")
        all_currencies = json["exchangeRate"]
        for dictionary in all_currencies:
            if dictionary.get('currency') == self.currency or dictionary.get('currency') == self.basecurrency:
                if dictionary.get('currency') != "UAH":
                    self.purchaseRate = dictionary[self.purchase]
                    self.saleRate = dictionary[self.sale]

    def construct_result(self):
        if self.bank == '':
            self.result += "ПриватБанку "
        else:
            self.result += "НБУ "

        self.result += f'з {self.basecurrency} в {self.currency} - '

        if self.basecurrency == 'UAH':
            self.result += f'{self.purchaseRate}'

        else:
            self.result += f'{self.saleRate}'

        return self.result

    def main(self):
        self.get_data()
        return self.construct_result()
