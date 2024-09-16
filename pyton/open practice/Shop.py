class Product:
    def __init__(self, name, bought_with={}):
        self.name = name
        self.bought_with = bought_with

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) >= 2:
            self._name = name
        else:
            raise ValueError('Invalid name')

    @property
    def bought_with(self):
        return self._bought_with

    @bought_with.setter
    def bought_with(self, bought_with):
        self._bought_with = bought_with

    def __repr__(self):
        return self.name

    def update(self, product_names):
        for product in product_names:
            try:
                self.bought_with[product] += 1
            except KeyError:  # I didn't know I needed to add KeyError
                self.bought_with[product] = 1

    def get_recommendations(self, k):
        if k < 0:
            raise ValueError('Invalid k')
        elif k == 0:
            return []
        else:
            products = []
            current = [[value, key] for key, value in
                       self.bought_with.items()]  # I didn't know it was necessary to write self.bought_with.items()
            current.sort()
            if len(current) > k:
                for i in range(len(current) - 1, k - 1, -1):  # I have a mistake should write k-1
                    products.append(current[i][1])
            else:
                for i in range(len(current) - 1, -1, -1):
                    products.append(current[i][1])


class GoldProduct(Product):
    def __init__(self, name, amount, bought_with={}):  # I wrote a default argument before a non-default argument
        super().__init__(name, bought_with)
        self.amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount == int(amount):
            self._amount = amount
        else:
            raise ValueError('')

    def __str__(self):
        return f'{self.name} ({self.amount} units left!)'

    def __repr__(self):
        return self.__str__()

    def update(self, product_names):
        self.amount -= 1
        super().update(product_names)  # I did not write in the brackets product_names

    def get_recommendations(self, k):  # I couldn't make an inheritance
        if k < 0:
            raise ValueError('Invalid k')
        elif k == 0:
            return []
        else:
            products, i = [], 0
            current = [[value, key] for key, value in
                       self.bought_with.items()]  # I didn't know it was necessary to write self.bought_with.items()
            current.sort()
            current = current[::-1]
            while i < k or i <= len(current) - 1:
                if current[i][0] >= 10:  # I forgot to make a condition
                    products.append(current[i][1])
                    i += 1
            return products


a = [52, 23, 77, 92, 34, 41, 87, 17, 66, 99]
a = a[::-1]
print(a)
