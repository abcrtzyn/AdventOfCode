from typing import List

def attemptExplodeRecurse(root: 'Snailfish', currentElement: 'Pair', path: List[int], depth: int, decrementIndicies: bool):
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
    def __init__(self, left: 'Pair | int', right: 'Pair | int'):
        self._left: Pair | int = left
        self._right: Pair | int = right
    
    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right
    @left.setter 
    def setLeft(self, element: 'Pair | int'):
        self._left = element
    @right.setter
    def setRight(self, element: 'Pair | int'):
        self._right = element
    
    def __getitem__(self, key: int):
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

        

    # def __str__(self):
    #     return 'no'
    
    def __add__(self, a: 'Snailfish'):
        values = self.values.copy()
        values.extend(a.values)
        return Snailfish(Pair(self.tree, a.tree), values)
        
    def red(self):
        pass
    
    def getElementAtPath(self, path: List[int]) -> Pair | int:
        this = self.tree
        for i in path:
            if isinstance(this,int):
                print("unable to traverse the tree anymore, reached an int before the end of the path")
                exit(1)
            this = this[i]
        return this
    
    def setElementAtPath(self, path: List[int], element: Pair):
        this = self.tree
        for i in path[0:-1]:
            this = this[i]
        this[path[-1]] = element

    def explodeAtPath(self, path: List[int]):
        element = self.getElementAtPath(path)
        assert isinstance(element,Pair)
        e0 = element[0]
        assert isinstance(e0,int)
        e1 = element[1]
        assert isinstance(e1,int)

        if e0 != 0:
            self.values[e0-1] += self.values[e0]
        if e1 != len(self.values) - 1:
            self.values[e1+1] += self.values[e1]
        self.values[e0] = 0
        self.values.pop(e1)
        self.setElementAtPath(path, 0)
    


    def attemptExplode(self):
        attemptExplodeRecurse(self, self.tree, list(), 0, False)
        