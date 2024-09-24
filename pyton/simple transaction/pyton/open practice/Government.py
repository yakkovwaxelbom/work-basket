from collections import defaultdict


class Constitution:
    def __init__(self):
        pass

    def add_rule(self, rule):
        pass

    def cancel_rule(self, rule):
        pass


class Minister:
    def __init__(self, name: str, party: str):
        self.__name = name
        self.__party = party

    def add_rule(self, rule: str, constitution):
        constitution.add_rule(self, rule)  # למה צריך את self
        print(f'A new rule by {self.__name} was accepted')

    def cancel_rule(self, rule, constitution):
        constitution.cancel_rule(self, rule)
        print(f'rule was canceled by {self.__name}')


b = Constitution


# a = Minister('yakov', 'a')
# a.add_rule('yakov', b)
# a.cancel_rule('yakov', b)
# print(b)


class ActingMinister(Minister):
    def __init__(self, name: str, party: str, ministry_name: str):
        self.ministry_name = ministry_name
        super().__init__(name, party)

    @property
    def ministry_name(self):
        return self._ministry_name

    @ministry_name.setter
    def ministry_name(self, ministry_name):
        upper_string = ministry_name.upper()
        self._ministry_name = upper_string

    def add_rule(self, rule: str, constitution, votes: list):
        count = sum(votes)
        if count <= len(votes) / 2:
            print('rule was not accepted')
        else:
            super().add_rule(rule, constitution)


k = [1, 1]
c = ActingMinister('1', '2', '3')


# c.add_rule('s', b, k)
class Minister:
    def __init__(self, name: str, party: str):
        self.__name = name
        self.__party = party

    def add_rule(self, rule: str, constitution: Constitution):
        constitution.add_rule(rule)  # למה צריך את self
        print(f'A new rule by {self.__name} was accepted ')

    def cancel_rule(self, rule, constitution: Constitution):
        constitution.cancel_rule(rule)
        print(f'rule was canceled by {self.__name}')


b = Constitution


# a = Minister('yakov', 'a')
# a.add_rule('yakov', b)
# a.cancel_rule('yakov', b)
# print(b)


class ActingMinister(Minister):
    def __init__(self, name: str, party: str, ministry_name: str):
        self.ministry_name = ministry_name
        super().__init__(name, party)

    @property
    def ministry_name(self):
        return self._ministry_name

    @ministry_name.setter
    def ministry_name(self, ministry_name):
        upper_string = ministry_name.upper()
        self._ministry_name = upper_string

    def add_rule(self, rule: str, constitution: Constitution, votes: list):
        if votes.count(1) <= len(votes) / 2:
            print('rule was not accepted')
        else:
            super().add_rule(rule, constitution)

    def cancel_rule(self, rule, constitution):
        upper_rule = rule.upper()
        index = self.ministry_name.find(upper_rule)
        if index != -1:
            super().cancel_rule(rule, constitution)
        else:
            ValueError('')


def most_productive_ministry(rule_to_ministry_dict: dict) -> str:
    def get_0():
        return 0
    count_of_rule = defaultdict(get_0)
    for key, value in rule_to_ministry_dict.items():
        count_of_rule[value] += 1
    return max(count_of_rule, key=count_of_rule.get)


a = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 9}
b =a
a[1]=100
print(a)
print(b)
# print(most_productive_ministry(a))
