class CustomerFilterFormat:
    """Class for construct query and format following data"""

    def __init__(self, city, state):
        self.city = city
        self.state = state
        self.result = ""

    def get_filtered_data(self):
        """"Construct sql query"""

        if self.city is not None and self.state is not None:
            try:
                result = f"""SELECT * FROM customers WHERE city = '{self.city}' AND state = '{self.state}'"""

            except Exception as ex:
                result = ex

            return result

        elif self.city is not None:

            result = f"""SELECT * FROM customers WHERE city = '{self.city}'"""
            return result

        elif self.state is not None:
            result = f"""SELECT * FROM customers WHERE state = '{self.state}'"""
            return result

    def format_data(self, data):
        """
        Format data for web
        :param data: list of tuples
        :return result: str - formated result
        """
        for element in data[0]:
            self.result += str(element) + '<br>'
        return self.result


class FormatCounter:
    def __init__(self):
        self.result = ""

    @staticmethod
    def get_data():
        result = "SELECT FirstName, COUNT(FirstName) FROM customers GROUP BY FirstName"
        return result

    def format_data(self, data):
        for element in data:
            self.result += (element[0] + ' - ' + str(element[1]) + '<br>')
        return self.result


class CalculatePriceFormat:
    def __init__(self):
        self.count = 0
        self.result = "Total price: "

    @staticmethod
    def get_data():
        result = """SELECT UnitPrice, Quantity FROM invoice_items"""
        return result

    def calculate_format_price(self, data):
        for price_quantity in data:
            self.count += (price_quantity[0] * price_quantity[1])

        self.result += str(self.count)
        return self.result
