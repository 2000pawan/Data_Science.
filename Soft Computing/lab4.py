class FuzzySet:
    def __init__(self, elements):
        """
        Initializes a fuzzy set.
        elements should be a list of tuples where each tuple consists of
        an element and its membership degree.
        Example: [('apple', 0.7), ('banana', 0.9)]
        """
        self.set = dict(elements)

    def __str__(self):
        """String representation of the fuzzy set."""
        return '{' + ', '.join(f'({key}, {value})' for key, value in self.set.items()) + '}'

    def union(self, other):
        """Union of two fuzzy sets (max membership degree for each element)."""
        result = self.set.copy()
        for element, degree in other.set.items():
            result[element] = max(result.get(element, 0), degree)
        return FuzzySet(result.items())

    def intersection(self, other):
        """Intersection of two fuzzy sets (min membership degree for each element)."""
        result = {element: min(degree, other.set[element]) for element, degree in self.set.items() if element in other.set}
        return FuzzySet(result.items())

    def complement(self):
        """Complement of a fuzzy set (1 - membership degree)."""
        result = {key: 1 - value for key, value in self.set.items()}
        return FuzzySet(result.items())

    def is_subset(self, other):
        """Check if the current fuzzy set is a fuzzy subset of the other set."""
        return all(self.set[element] <= other.set.get(element, 0) for element in self.set)

    def is_superset(self, other):
        """Check if the current fuzzy set is a fuzzy superset of the other set."""
        return all(self.set.get(element, 0) >= degree for element, degree in other.set.items())

    def is_disjoint(self, other):
        """Check if the two fuzzy sets are fuzzy disjoint (no intersection)."""
        return all(min(self.set.get(element, 0), other.set.get(element, 0)) == 0 for element in self.set)

    def cardinality(self):
        """Compute the cardinality of a fuzzy set (sum of membership degrees)."""
        return sum(self.set.values())

    def crisp_set(self):
        """Convert fuzzy set to a crisp set (only include elements with membership > 0.5)."""
        return {key for key, value in self.set.items() if value > 0.5}


# Example Usage
fuzzy_set1 = FuzzySet([('apple', 0.7), ('banana', 0.9), ('cherry', 0.5)])
fuzzy_set2 = FuzzySet([('banana', 0.8), ('cherry', 0.6), ('date', 0.4)])

print("Union:", fuzzy_set1.union(fuzzy_set2))
print("Intersection:", fuzzy_set1.intersection(fuzzy_set2))
print("Complement of fuzzy_set1:", fuzzy_set1.complement())
print("Is fuzzy_set1 a fuzzy subset of fuzzy_set2?", fuzzy_set1.is_subset(fuzzy_set2))
print("Is fuzzy_set1 a fuzzy superset of fuzzy_set2?", fuzzy_set1.is_superset(fuzzy_set2))
print("Are fuzzy_set1 and fuzzy_set2 fuzzy disjoint?", fuzzy_set1.is_disjoint(fuzzy_set2))
print("Cardinality of fuzzy_set1:", fuzzy_set1.cardinality())
print("Crisp set (membership > 0.5):", fuzzy_set1.crisp_set())


'''
PS G:\Coding\Git Uploads\Data Science & Machine Learning Using Python\Data-Science\Soft Computing> & C:/Users/YADUV/anaconda3/python.exe "g:/Coding/Git Uploads/Data Science & Machine Learning Using Python/Data-Science/Soft Computing/lab4.py"
Union: {(apple, 0.7), (banana, 0.9), (cherry, 0.6), (date, 0.4)}
Intersection: {(banana, 0.8), (cherry, 0.5)}
Complement of fuzzy_set1: {(apple, 0.30000000000000004), (banana, 0.09999999999999998), (cherry, 0.5)}
Is fuzzy_set1 a fuzzy subset of fuzzy_set2? False
Is fuzzy_set1 a fuzzy superset of fuzzy_set2? False
Are fuzzy_set1 and fuzzy_set2 fuzzy disjoint? False
Cardinality of fuzzy_set1: 2.1
Crisp set (membership > 0.5): {'banana', 'apple'}
PS G:\Coding\Git Uploads\Data Science & Machine Learning Using Python\Data-Science\Soft Computing> 
'''