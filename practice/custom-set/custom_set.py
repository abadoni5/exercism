"""
Approach:
1. Initialize the CustomSet with an optional list of elements. Convert this list into a set to ensure uniqueness.
2. Define methods to check if the set is empty, if it contains a specific element, if it is a subset of another set, and if it is disjoint from another set.
3. Implement comparison methods to check for equality between two CustomSets.
4. Implement methods to add elements to the set, compute the intersection of two sets, and perform set difference and union operations.
"""

class CustomSet:
    def __init__(self, elements=[]):
        self.elements = set(elements)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return self.elements.issubset(other.elements)

    def isdisjoint(self, other):
        return self.elements.isdisjoint(other.elements)

    def __eq__(self, other):
        return self.elements == other.elements

    def add(self, element):
        self.elements.add(element)

    def intersection(self, other):
        return CustomSet(self.elements.intersection(other.elements))

    def __sub__(self, other):
        return CustomSet(self.elements - other.elements)

    def __add__(self, other):
        return CustomSet(self.elements.union(other.elements))