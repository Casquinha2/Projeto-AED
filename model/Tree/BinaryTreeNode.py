class BinaryTreeNode:
    def __innit__(self):
        self.element = None
        self.left_child = None
        self.right_child = None

    def get_element(self):
        return self.element
    def set_element(self, element):
        self.element = element
    def get_left_child(self):
        return self.left_child
    def set_left_child(self, left_child):
        self.left_child = left_child
        