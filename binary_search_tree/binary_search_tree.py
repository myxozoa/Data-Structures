class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value > value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True

        if self.left == None or self.right == None:
            return False

        if self.value > target:
            if self.left.value == target:
                return True
            else:
                self.left.contains(target)
        else:
            if self.right.value == target:
                return True
            else:
                self.right.contains(target)

    def get_max(self):
        current = self.right
        max = self
        while not current == None:
            if current.value > max.value:
               max = current
            current = current.right
        return max.value