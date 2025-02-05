# my_family
my_family = ("mother", "father", "sister", "brother", "sister")
print(my_family)
print("Type of myfamily:", type(my_family))

print("First occurrence of 'sister':", my_family[2])
print("Second occurrence of 'sister':", my_family[4])

try:
    my_family.append("me")
except AttributeError as e:
    print("Error:", e)
try:
    my_family.pop(3)
except AttributeError as e:
    print("Error:", e)
