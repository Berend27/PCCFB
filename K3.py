# Kapitel 3 - The Array Archipelago
# Working with lists, tuples, and sets
# This challenge has three parts.

# Teil 1 - given a list of student names and grades,
# sort the list by grades and
# filter out students who score below 80
students = [('Charlie', 95), ('Alice', 85), ('Bob', 70)]

sorted_students = sorted([student for student in students if student[1] > 80], key=lambda x: x[1])
print(sorted_students)

# Teil 2 - add a new member to a list, and
# instantiate a set from an existing set
team_members = ['Alice', 'Bob', 'Charlie']
project_milestones = ('Planning', 'Execution', 'Closure')
required_skills = {'Python', 'Data Analysis', 'Communication'}

team_members.append('Dana')
print(team_members)
unique_skills = set(required_skills)
print(unique_skills)

# Teil 3 - filter and sort in descending order a list of tuples,
# then create a union of two sets

products = [('Laptop', 150), ('Phone', 200), ('Tablet', 50), ('Monitor', 120)]
top_products = sorted([product for product in products if product[1] > 100],
                      key=lambda x: x[1], reverse=True)

categories = {'Electronics', 'Gadgets', 'Accessories'}
new_categories = {'Wearables', 'Home Appliances'}
all_categories = categories | new_categories
# all_categories = categories.union(new_categories) can work instead

print(top_products)
print(all_categories)