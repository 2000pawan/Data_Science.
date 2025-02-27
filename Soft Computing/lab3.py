class SetOperations:
    def __init__(self, set1, set2):
        self.set1 = set(set1)  # Convert to set in case input is not a set
        self.set2 = set(set2)

    def union(self):
        """Return the union of two sets."""
        return self.set1.union(self.set2)

    def intersection(self):
        """Return the intersection of two sets."""
        return self.set1.intersection(self.set2)

    def difference(self):
        """Return the difference of the first set from the second."""
        return self.set1.difference(self.set2)

    def symmetric_difference(self):
        """Return the symmetric difference of two sets."""
        return self.set1.symmetric_difference(self.set2)

    def is_subset(self):
        """Check if the first set is a subset of the second set."""
        return self.set1.issubset(self.set2)

    def is_superset(self):
        """Check if the first set is a superset of the second set."""
        return self.set1.issuperset(self.set2)

    def is_disjoint(self):
        """Check if the two sets are disjoint (no common elements)."""
        return self.set1.isdisjoint(self.set2)

    def cartesian_product(self):
        """Return the Cartesian product of two sets."""
        product = set()
        for x in self.set1:
            for y in self.set2:
                product.add((x, y))
        return product

    def power_set(self):
        """Return the power set of the first set (all subsets)."""
        power_set = [[]]
        for elem in self.set1:
            power_set += [item + [elem] for item in power_set]
        return [set(item) for item in power_set]

# Example Usage
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
operations = SetOperations(set1, set2)

# Union
print("Union:", operations.union())  # {1, 2, 3, 4, 5, 6}

# Intersection
print("Intersection:", operations.intersection())  # {3, 4}

# Difference
print("Difference (set1 - set2):", operations.difference())  # {1, 2}

# Symmetric Difference
print("Symmetric Difference:", operations.symmetric_difference())  # {1, 2, 5, 6}

# Subset
print("Is set1 a subset of set2?", operations.is_subset())  # False

# Superset
print("Is set1 a superset of set2?", operations.is_superset())  # False

# Disjoint
print("Are set1 and set2 disjoint?", operations.is_disjoint())  # False

# Cartesian Product
print("Cartesian Product:", operations.cartesian_product())  # {(1, 3), (1, 4), (1, 5), (1, 6), ...}

# Power Set
print("Power Set of set1:", operations.power_set())  # [set(), {1}, {2}, {3}, {4}, {1, 2}, {1, 3}, ...]



'''PS G:\Coding\Git Uploads\Data Science & Machine Learning Using Python\Data-Science\Soft Computing> & C:/Users/YADUV/anaconda3/python.exe "g:/Coding/Git Uploads/Data Science & Machine Learning Using Python/Data-Science/Soft Computing/lab3.py"
Union: {1, 2, 3, 4, 5, 6}
PS G:\Coding\Git Uploads\Data Science & Machine Learning Using Python\Data-Science\Soft Computing> & C:/Users/YADUV/anaconda3/python.exe "g:/Coding/Git Uploads/Data Science & Machine Learning Using Python/Data-Science/Soft Computing/lab3.py"
Intersection: {3, 4}
Difference (set1 - set2): {1, 2}
Symmetric Difference: {1, 2, 5, 6}
Is set1 a subset of set2? False
Is set1 a superset of set2? False
Are set1 and set2 disjoint? False
Cartesian Product: {(4, 4), (2, 4), (3, 4), (1, 5), (4, 3), (4, 6), (1, 4), (2, 3), (4, 5), (3, 3), (2, 6), (3, 6), (1, 6), (2, 5), (1, 3), (3, 5)}
Power Set of set1: [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}, {4}, {1, 4}, {2, 4}, {1, 2, 4}, {3, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4}]
PS G:\Coding\Git Uploads\Data Science & Machine Learning Using Python\Data-Science\Soft Computing>
'''