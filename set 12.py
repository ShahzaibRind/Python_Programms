s1 = set()


s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add(5)

print(s1)
s2 = {1,2,3,6}
print("Intersection: ", s1.intersection(s2))
print("Union: ", s1.union(s2))
print("Disjoint: ", s1.isdisjoint(s2))
print("Difference: ", s1.difference(s2))

print(s1.copy(s2))