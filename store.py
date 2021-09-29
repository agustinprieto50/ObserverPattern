from abc import abstractmethod


class Store():

    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteStore(Store):

    def __init__(self, name, qt, observers = set()):
        self._name = name
        self._qt = qt
        self._observers = observers

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    def notify(self):
        for i in self._observers:
            i.update(self.qt)
    
    @property
    def qt(self):
        return self._qt
    
    @qt.setter
    def qt(self, value):
        print('Current stock: ', self._qt)
        self._qt = value
        print('Stock has changed')
        self.notify()
        

    def attach(self, o):
        self._observers.add(o)
    
    def detach(self, o):
        self._observers.remove(o)

    
            

            