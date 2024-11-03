from typing import Tuple, Union, Optional, List

def attemptExplodeRecurse(root: 'Snailfish', currentElement: 'Pair', path: List[int], depth, decrementIndicies):
    if depth == 4 and not decrementIndicies:
        root.explodeAtPath(path)
        currentElement = root.getElementAtPath(path)
        decrementIndicies = True
    if isinstance(currentElement[0], Pair):
        path.append(0)
        attemptExplodeRecurse(root, currentElement[0], path, depth+1, decrementIndicies)
        path.pop()
    elif decrementIndicies:
        currentElement[0] -= 1
    if isinstance(currentElement[1], Pair):
        path.append(1)
        attemptExplodeRecurse(root, currentElement[1], path, depth+1, decrementIndicies)
        path.pop()
    elif decrementIndicies:
        currentElement[1] -= 1
        
class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    @property
    def left(self):
        return self.left
    @property
    def right(self):
        return self.right
    @left.setter 
    def setLeft(self, element):
        self.left = element
    @right.setter
    def setRight(self, element):
        self.right = element
    
    def __getitem__(self, key):
        if key == 0:
            return self.left
        elif key == 1:
            return self.right
        else:
            raise KeyError(f'pairs only have index 0 and 1, not {key}')

    def __str__(self):
        return f'({str(self.left)},{str(self.right)})'

class Snailfish:

    def __init__(self, indiciesTree: Pair, valuesList: List[int]):
        # TODO if String
        pass
        self.tree = indiciesTree
        self.values = valuesList

        

    def __str__(self):
        return 'no'
    
    def __add__(self, a: 'Snailfish'):
        values = self.values.copy()
        values.extend(a.values)
        return Snailfish(Pair(self.tree, a.tree), values)
        
    def red():
        pass
    
    def getElementAtPath(self, path: List[int]):
        this = self.tree
        for i in path:
            this = this[i]
        return this
    def setElementAtPath(self, path: List[int], element):
        this = self.tree
        for i in path[0:-1]:
            this = this[i]
        this[path[-1]] = element

    def explodeAtPath(self, path: List[int]):
        element = self.getElementAtPath(path)
        if element[0] != 0:
            self.values[element[0]-1] += self.values[element[0]]
        if element[1] != len(self.values) - 1:
            self.values[element[1]+1] += self.values[element[1]]
        self.values[element[0]] = 0
        self.values.pop(element[1])
        self.setElementAtPath(path, 0)
    


    def attemptExplode(self):
        attemptExplodeRecurse(self, self.tree, list(), 0, False)
        