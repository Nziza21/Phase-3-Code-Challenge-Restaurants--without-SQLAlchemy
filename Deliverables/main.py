from Deliverables.customer import Customer
from Deliverables.restaurant import Restaurant

from Deliverables.customer import Customer
from Deliverables.restaurant import Restaurant

# Sample instances for testing
customer1 = Customer("George", "Washington")
customer2 = Customer("John", "Adams")
restaurant1 = Restaurant("The Best Restaurant")
restaurant2 = Restaurant("Delicious Eats")

# Testing methods
review1 = customer1.add_review(restaurant1, 4)
review2 = customer2.add_review(restaurant1, 5)
review3 = customer1.add_review(restaurant2, 3)

print(customer1.full_name())  # Output: George Washington
print(customer1.restaurants())  # Output: [The Best Restaurant, Delicious Eats]
print(restaurant1.customers())  # Output: [George Washington, John Adams]
print(restaurant1.average_star_rating())  # Output: 4.5