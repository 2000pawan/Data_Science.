class FuzzySet:
 def __init__(self,elements):
  self.set=dict(elements)
 def __str__(self):
  return '{'+', '.join(f'({key}, {value})' for key,value in self.set.items())+'}'
 def union(self,other):
  result=self.set.copy()
  for element,degree in other.set.items():
   if element in result:
    result[element]=max(result[element],degree)
   else:
    result[element]=degree
  return FuzzySet(result.items())
 def intersection(self,other):
  result={}
  for element,degree in self.set.items():
   if element in other.set:
    result[element]=min(degree,other.set[element])
  return FuzzySet(result.items())
 def complement(self):
  result={key:1-value for key,value in self.set.items()}
  return FuzzySet(result.items())
 def is_subset(self,other):
  for element,degree in self.set.items():
   if element in other.set and degree>other.set[element]:
    return False
  return True
 def is_superset(self,other):
  for element,degree in other.set.items():
   if element in self.set and self.set[element]<degree:
    return False
  return True
 def is_disjoint(self,other):
  for element in self.set:
   if element in other.set:
    if min(self.set[element],other.set[element])>0:
     return False
  return True
 def cardinality(self):
  return sum(self.set.values())
 def crisp_set(self):
  return {key for key,value in self.set.items() if value>0.5}

fuzzy_set1=FuzzySet([('apple',0.7),('banana',0.9),('cherry',0.5)])
fuzzy_set2=FuzzySet([('banana',0.8),('cherry',0.6),('date',0.4)])
union_set=fuzzy_set1.union(fuzzy_set2)
print("Union:",union_set)
intersection_set=fuzzy_set1.intersection(fuzzy_set2)
print("Intersection:",intersection_set)
complement_set=fuzzy_set1.complement()
print("Complement of fuzzy_set1:",complement_set)
print("Is fuzzy_set1 a fuzzy subset of fuzzy_set2?",fuzzy_set1.is_subset(fuzzy_set2))
print("Is fuzzy_set1 a fuzzy superset of fuzzy_set2?",fuzzy_set1.is_superset(fuzzy_set2))
print("Are fuzzy_set1 and fuzzy_set2 fuzzy disjoint?",fuzzy_set1.is_disjoint(fuzzy_set2))
print("Cardinality of fuzzy_set1:",fuzzy_set1.cardinality())
crisp_set=fuzzy_set1.crisp_set()
print("Crisp set (membership > 0.5):",crisp_set)
