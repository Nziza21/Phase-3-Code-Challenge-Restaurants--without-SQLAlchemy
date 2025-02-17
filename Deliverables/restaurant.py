from Deliverables.review import Review

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self._name

    def reviews(self):
        return [review for review in Review.all_reviews() if review.restaurant() == self]

    def customers(self):
        return list(set(review.customer() for review in self.reviews()))

    def average_star_rating(self):
        ratings = [review.rating() for review in self.reviews()]
        if not ratings:
            return 0
        return sum(ratings) / len(ratings)