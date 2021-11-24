class Node:
    def __init__(self, value):
        self.index = -1
        self.info = value
        self.parent = -1
        self.left_sibling = -1

    def __str__(self):
        return str(self.info) + "  " + str(self.parent) + "  " + str(self.left_sibling)