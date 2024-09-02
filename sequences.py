#tuple
def sort_by_age(tuples):
    """Sorts a list of tuples by age."""
    return sorted(tuples, key=lambda x: x[1])

#usage

people = [
    ("John", 25),
    ("Alice", 30),
    ("Bob", 20),
    ("Charlie", 35),
    ("David", 15)
]

sorted_people = sort_by_age(people)

print("Sorted by age:")
for person in sorted_people:
    print(f"{person[0]}: {person[1]} years old")