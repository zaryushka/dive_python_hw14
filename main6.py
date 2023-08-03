# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import pytest
import json


class UserError(Exception):
    pass


class UserLvlError(UserError):
    pass


class UserAccessError(UserError):
    def __str__(self):
        return 'Wrong password or login'


class User:
    def __init__(self, name, id, lvl):
        self.name = name
        self.id = id
        self.lvl = lvl

    def __str__(self):
        return f'{self.name} {self.id} {self.lvl}'

    def __repr__(self):
        return f'User({self.name}, {self.id}, {self.lvl})'

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash((self.name, self.id))


class SignIn:
    def __init__(self):
        self.tmp_user = None
        self.set_user = set()

    def coder(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for lvl, value in data.items():
            for id, name in value.items():
                self.set_user.add(User(name, id, lvl))

        return self.set_user

    def sign_in(self, my_name, my_id):
        new_user = User(my_name, my_id, 0)
        if new_user not in self.set_user:
            raise UserAccessError
        else:
            for user in self.set_user:
                if new_user == user:
                    self.tmp_user = user
                    return self.tmp_user

    def add(self, name, id, lvl):
        if self.tmp_user.lvl > lvl:
            raise UserLvlError
        else:
            new_user = User(name, id, lvl)
            self.set_user.add(new_user)
        return new_user

    def show(self):
        return self.set_user

    # def __repr__(self):
    #     return f'User({self.}, {}, {})'


@pytest.fixture()
def data():
    sg1 = SignIn()
    sg2 = SignIn()
    user1 = User('a', '01', '1')
    user2 = User('sobaka', '15', '10')


@pytest.fixture()
def set_user():
    user_set = {
        User('kjh', '14', '2'),
        User('tr', '05', '5'),
        User('lk', '07', '7'),
        User('ff', '08', '1'),
        User('hds', '13', '5'),
        User('kd', '09', '2'),
        User('ds', '10', '2'),
        User('a', '01', '1'),
        User('wq', '15', '1'),
        User('kj', '06', '6'),
        User('r', '03', '3'),
        User('d', '02', '2'),
        User('yy', '04', '4')
    }
    return user_set


def test_load(set_user):
    sign_in = SignIn()
    sign_in.coder('data.json')
    assert sign_in.set_user == set_user


def test_signin_user():
    sign = SignIn()
    sign.coder('data.json')
    result = sign.sign_in('a', '01')
    assert result == User('a', '01', '1')


def test_1_1():
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-v'])