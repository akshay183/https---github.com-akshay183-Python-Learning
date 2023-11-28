# Empty Sets
# When creating set, be sure to not use empty curly braces {} or you will get an empty dictionary 
# instead.

s= {1,2,3}
s.add(4)
print(s)
s.update([4,5,6])
print(s)


# set remove() and discard()
# Both methods will remove an element from the set, but remove() will raise a key error if the value doesn’t exist.

# >>> s = {1, 2, 3}
# >>> s.remove(3)
# >>> s
# # {1, 2}

# >>> s.remove(3)
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # KeyError: 3
# discard() won’t raise any errors.

# >>> s = {1, 2, 3}
# >>> s.discard(3)
# >>> s
# # {1, 2}
# >>> s.discard(3)


