from model.Tree.Tree import*

class UtilizadorTree(Tree):
    def __init__(self, root):
        self.root = root
    def get_root (self):
        return self.root
    def size(self):
        return self.node_size(self.root)
    def node_size(self, node):
        if node is None:
            return 0
        return (1 + self.node_size(node.get_left_child()) + self.node_size(node.get_right_child()))
    def is_empty (self):
        return self.size() == 0
    def is_full (self):
        return False
    def height (self):
        return self.node_height(self.root)
    def node_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.node_height(node.get_left_child()), self.node_height(node.get_rigth_child()))
    
    