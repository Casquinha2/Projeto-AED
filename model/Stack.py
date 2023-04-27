from abc import ABC, abstractmethod
class Stack(ABC):
    @abstractmethod
    def is_empty(self):
        ''' Retorna True se a stack não contém elementos. '''
    @abstractmethod
    def is_full(self):
        ''' Retorna True se a stack não puder conter mais elementos. '''
    @abstractmethod
    def size(self):
        ''' Retorna o número de elementos na stack. '''
    @abstractmethod
    def top(self):
        ''' Retorna o elemento no topo da stack.'''
    @abstractmethod
    def push(self, element):
        ''' Insere o elemento especificado no topo da stack.'''
    @abstractmethod
    def pop(self):
        ''' Remove e retorna o elemento no topo da stack. '''
