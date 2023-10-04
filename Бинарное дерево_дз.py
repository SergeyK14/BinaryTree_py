class Node:

    def __init__(self, value):
        BinaryTree
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        """Метод печати Node"""
        res = f'значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res


class BinaryTree:

    # метод для ключевого элемента
    def __init__(self, root_value):
        """ Инициализация BinaryTree"""
        self.root = Node(root_value)

    
    def add(self, value):
        """Метод добавления к дереву элементов"""
        res = self.search(self.root, value)

        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print("Хорош")

    
    def search(self, node, value, parent=None):
        """Метод поиска по дереву"""
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)
        
        
    def delete(self, node, value):
        """Метод удаления элемента из дерева"""
        res = self.search(self, value)

        if res[0].value or res[1].value == value:
            node(value) == None
            return node
        else:
            print("Таких элементов нет")
        
    
    def counter(self, value, node, count=0):
        """Метод подсмчета количества элементов в дереве"""
        if node != None:
            count += 1
            return count
        if value > node.value:
            if node.right:
                return self.counter(self, value, node)
            if node.left:
                return self.counter(self, value, node)
        if value < node.value:
            if node.left:
                return self.counter(self, value, node)
            if node.right:
                return self.counter(self, value, node)
        return print(f"В дереве {count} элементов")
        

    def printTree(self, node, value): 
        """Метод печати элементов дерева"""  
        if node != None: 
            res = f'значение узла: {node.value}'
            if node.left or node.right:
                print (res)
                print(f"{node.left} <--{node.value}--> {node.right}")
            if node.left:
                return self.printTree(self, node, value)
            if node.right:
                return self.printTree(self, node, value)
        return print(f"В дереве пока нет элементов")

    
bt = BinaryTree(5)
bt.add(10)
bt.add(15)
bt.add(3)
bt.add(4)

print(bt.root)
#print(bt.search(bt.root, 8)[1])
# print(bt.root.left)
# print(bt.root.right)
bt.printTree(bt.root, 8)