from abc import abstractmethod


class Client():

    @abstractmethod
    def update(self, value):
        pass


class ConcreteClient(Client):

    def __init__(self, name, surname, state=None):
        self._name = name
        self._surname = surname
        self._state = state

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname
 
    @surname.setter
    def surname(self, value):
        self._surname = value

    def update(self, value):
        self._state = value
        print('New Stock: ', self._state,)

