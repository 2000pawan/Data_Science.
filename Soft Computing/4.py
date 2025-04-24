class Relation:
    def __init__(self, relation_type='classical', relation_data=None):
        self.relation_type = relation_type
        self.relation_data = relation_data if relation_data else []

    def classical_composition(self, other):
        result = []
        for (x, y) in self.relation_data:
            for (y2, z) in other.relation_data:
                if y == y2:
                    result.append((x, z))
        return result

    def fuzzy_composition(self, other):
        result = []
        for (x, mu_x), (y, mu_y) in zip(self.relation_data, other.relation_data):
            result.append(((x, y), min(mu_x, mu_y)))
        return result

    def get_composed_relation(self, other):
        if self.relation_type == 'classical':
            return self.classical_composition(other)
        elif self.relation_type == 'fuzzy':
            return self.fuzzy_composition(other)

R1_classical = Relation('classical', [(1, 'a'), (2, 'b'), (3, 'c')])
R2_classical = Relation('classical', [('a', 4), ('b', 5), ('c', 6)])
classical_composition_result = R1_classical.get_composed_relation(R2_classical)
print("Classical Composition Result:")
print(classical_composition_result)

R1_fuzzy = Relation('fuzzy', [(1, 0.8), (2, 0.6), (3, 1.0)])
R2_fuzzy = Relation('fuzzy', [('a', 0.9), ('b', 0.7), ('c', 0.5)])
fuzzy_composition_result = R1_fuzzy.get_composed_relation(R2_fuzzy)
print("Fuzzy Composition Result:")
for pair, degree in fuzzy_composition_result:
    print(f"Pair: {pair}, Degree: {degree}")

