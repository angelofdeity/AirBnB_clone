import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.review.place_id = "1"
        self.review.user_id = "2"
        self.review.text = "This is a great place!"

    def test_attributes_exists(self):
        self.assertEqual(hasattr(self.review, 'place_id'), True)
        self.assertEqual(hasattr(self.review, 'user_id'), True)
        self.assertEqual(hasattr(self.review, 'text'), True)

    def test_attributes_values(self):
        self.assertEqual(self.review.place_id, "1")
        self.assertEqual(self.review.user_id, "2")
        self.assertEqual(self.review.text, "This is a great place!")


if __name__ == '__main__':
    unittest.main()
