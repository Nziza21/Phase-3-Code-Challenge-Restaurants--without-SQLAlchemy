# Phase-3-Code-Challenge-Restaurants--without-SQLAlchemy

# Yelp-style Domain Project

## Overview

This project simulates a simplified Yelp-style domain, focusing on three main models: `Customer`, `Restaurant`, and `Review`. The relationships are designed to represent a many-to-many relationship between `Restaurant` and `Customer`, where a `Review` belongs to both a `Customer` and a `Restaurant`.

## Folder Structure

The project is organized into separate files for each class and a main file for testing:

- `customer.py`: Contains the `Customer` class.
- `restaurant.py`: Contains the `Restaurant` class.
- `review.py`: Contains the `Review` class.
- `main.py`: A file for testing the classes and their methods.

## Classes and Methods

### Customer Class

- **Initializer**
  - `__init__(self, given_name, family_name)`: Initializes a customer with a given name and family name.

- **Readers and Writers**
  - `given_name()`: Returns the customer's given name.
  - `family_name()`: Returns the customer's family name.
  - `full_name()`: Returns the full name of the customer.
  - `all()`: Returns all customer instances.

- **Object Relationship Methods**
  - `restaurants()`: Returns a unique list of all restaurants a customer has reviewed.
  - `add_review(restaurant, rating)`: Adds a new review for a restaurant and associates it with the customer.

- **Aggregate and Association Methods**
  - `num_reviews()`: Returns the total number of reviews that a customer has authored.
  - `find_by_name(name)`: Class method. Given a full name, returns the first customer whose full name matches.
  - `find_all_by_given_name(name)`: Class method. Given a given name, returns a list containing all customers with that given name.

### Restaurant Class

- **Initializer**
  - `__init__(self, name)`: Initializes a restaurant with a name.

- **Readers and Writers**
  - `name()`: Returns the restaurant's name.

- **Object Relationship Methods**
  - `reviews()`: Returns a list of all reviews for that restaurant.
  - `customers()`: Returns a unique list of all customers who have reviewed a particular restaurant.
  - `average_star_rating()`: Returns the average star rating for a restaurant based on its reviews.

### Review Class

- **Initializer**
  - `__init__(self, customer, restaurant, rating)`: Initializes a review with a customer, restaurant, and rating.

- **Readers and Writers**
  - `rating()`: Returns the rating for a restaurant.

- **Object Relationship Methods**
  - `customer()`: Returns the customer object for that review.
  - `restaurant()`: Returns the restaurant object for that given review.
  
- **Aggregate and Association Methods**
  - `all_reviews()`: Class method. Returns all reviews.

## Usage

1. Install dependencies using the provided Pipfile.
2. Run the `main.py` file to test the classes and methods.

Feel free to customize this README to provide additional details or instructions specific to your project.