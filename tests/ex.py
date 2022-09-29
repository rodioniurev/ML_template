from collections import Counter

b = 5
s = 1
ab = 8 * [b]
ast = 10 * [s]
print(ab)
import heapq

sss = [5, 0, 1, 2, 3]
print(heapq.nsmallest(3, sss)[-1])


class CategoryTree:

    def __init__(self):
        self.children = {}

    def add_category(self, category, parent):
        self.children[parent] = category

    def get_children(self, parent):
        return self.children[parent]



c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')
print(','.join(c.get_children('A') or []))


class MovingTotal:

    def __init__(self):
        self.container = None

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        self.container = numbers

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        return Counter(self.container)[total]




movingtotal = MovingTotal()

movingtotal.append([1, 2, 3, 4])
print(movingtotal.contains(6))
print(movingtotal.contains(9))
print(movingtotal.contains(12))
print(movingtotal.contains(7))

movingtotal.append([5])
print(movingtotal.contains(6))
print(movingtotal.contains(9))
print(movingtotal.contains(12))
print(movingtotal.contains(7))