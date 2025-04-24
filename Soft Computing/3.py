class CartesianProduct:
 def __init__(self,set1,set2,fuzzy=False):
  self.set1=set1
  self.set2=set2
  self.fuzzy=fuzzy
 def classical_product(self):
  return[(x,y)for x in self.set1 for y in self.set2]
 def fuzzy_product(self):
  result=[]
  for(x,mu_x)in self.set1:
   for(y,mu_y)in self.set2:
    mu_xy=min(mu_x,mu_y)
    result.append(((x,y),mu_xy))
  return result
 def get_product(self):
  if self.fuzzy:
   return self.fuzzy_product()
  else:
   return self.classical_product()

set1=['a1','a2','a3']
set2=['b1','b2']
fuzzy_set1=[('a1',0.8),('a2',0.6),('a3',0.9)]
fuzzy_set2=[('b1',0.7),('b2',0.5)]
classical_product=CartesianProduct(set1,set2,fuzzy=False)
print("Classical Cartesian Product:")
print(classical_product.get_product())
fuzzy_product=CartesianProduct(fuzzy_set1,fuzzy_set2,fuzzy=True)
print("\nFuzzy Cartesian Product:")
for pair,degree in fuzzy_product.get_product():
 print(f"Pair: {pair}, Degree: {degree}")
