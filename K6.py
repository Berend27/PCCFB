# Debugging, Unit Testing, and Error Handling
import pdb

def process_data(data):
  for item in data:
    if item is not None:  # was missing the 'is' keyword
      print(item)

process_data(["Python", "C++"])

# Error Handling with Try-Except
def calculate_average(values):
  try:
    return sum(values) / len(values)
  except ZeroDivisionError:
    return "Cannot calculate average for an empty list."

# Stepping through code with PyCharm's debugger, not pdb
# import pdb

def calculate_total(cart, tax_rate):
    # pdb.set_trace()  # Step into the debugger here

    subtotal = 0
    for item in cart:
        subtotal += item['price'] * item['quantity']

    tax = subtotal * tax_rate
    total = subtotal + tax

    return round(total, 2)

# Example usage
cart = [
    {'name': 'Apple', 'price': 0.99, 'quantity': 3},
    {'name': 'Bread', 'price': 2.50, 'quantity': 2},
    {'name': 'Milk', 'price': 3.25, 'quantity': 1}
]

total = calculate_total(cart, 0.07)
print(f"Total with tax: ${total}")

# Unit Testing
import unittest

class TestCalculations(unittest.TestCase):

  def test_calculate_average(self):
    self.assertEqual(calculate_average([1, 2, 3]), 2)
    self.assertEqual(calculate_average([]), "Cannot calculate average for an empty list.")

if __name__ == '__main__':
  unittest.main()
