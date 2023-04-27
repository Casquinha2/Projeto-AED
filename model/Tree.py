from abc import ABC, abstractmethod

class Tree(ABC):
    @abstractmethod
    def get_root (self):
        '''Retorna a raiz da árvore.'''
    @abstractmethod
    def size(self):
        """Retorna o número de elementos na árvore."""
    @abstractmethod
    def height (self):
        """Retorna a altura da árvore."""
    @abstractmethod
    def is_empty (self):
        """Retorna True se a árvore estiver vazia."""
    @abstractmethod
    def is_full (self):
        """Retorna True se a árvore estiver cheia."""
