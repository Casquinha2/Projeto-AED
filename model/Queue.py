from abc import ABC, abstractmethod
class Queue(ABC):
    @abstractmethod
    def is_empty(self):
        ''' Retorna True se a queue não não contém elementos. '''
    @abstractmethod
    def is_full(self):
        ''' Retorna True se a queue não puder conter mais elementos. '''
    @abstractmethod
    def size(self):
        ''' Retorna o número de elementos na queue.'''
    @abstractmethod
    def enqueue(self, element):
        ''' Insere o elemento especificado no final da queue. '''
    @abstractmethod
    def dequeue(self):
        ''' Remove e retorna o elemento na frente da queue.'''