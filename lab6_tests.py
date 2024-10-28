import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1

    def test_book_index_smallest_from_1(self):
        books = [data.Book(["Kevin", "George"], "Avocado"), data.Book(["Kevin", "George"], "Banana"), data.Book([""], "AA")]
        result = lab6.book_index_smallest_from(books, 0)
        expected = 2
        self.assertEqual(expected, result)

    def test_book_index_smallest_from_2(self):
        books = [data.Book(["Kevin", "George"], "ZAvocado"), data.Book(["Kevin", "George"], "ABanana"), data.Book([""], "Timothy")]
        result = lab6.book_index_smallest_from(books, 1)
        expected = 1
        self.assertEqual(expected, result)

    def test_selection_sort_books_1(self):
        books = [data.Book(["a"], "Avocado"), data.Book(["a"], "Banana"), data.Book(["a"], "AA"), data.Book(["a"], "Craigolas")]
        expected = [books[2], books[0], books[1], books[3]]
        lab6.selection_sort_books(books)
        self.assertEqual(expected, books)

    def test_selection_sort_books_2(self):
        books = [data.Book(["a"], "ZAvocado"), data.Book(["a"], "SBanana"), data.Book(["a"], "KAA"), data.Book(["a"], "/")]
        expected = [books[-1], books[-2], books[1], books[0]]
        lab6.selection_sort_books(books)
        self.assertEqual(expected, books)

    # Part 2

    def test_swap_case_1(self):
        input = "Apple Haha! 가언"
        result = lab6.swap_case(input)
        expected = "aPPLE hAHA! 가언"
        self.assertEqual(expected, result)

    def test_swap_case_2(self):
        input = ""
        result = lab6.swap_case(input)
        expected = ""
        self.assertEqual(expected, result)

    # Part 3

    def test_str_translate_1(self):
        result = lab6.str_translate('abcdcba', 'a', 'x')
        expected = 'xbcdcbx'
        self.assertEqual(expected, result)

    def test_str_translate_2(self):
        result = lab6.str_translate("", "", "X")
        expected = ""
        self.assertEqual(expected, result)

    # Part 4

    def test_histogram_1(self):
        result = lab6.histogram("The Boy is a Big Boy.")
        expected = {"The": 1, "Boy": 1, "is": 1, "a" : 1, "Big": 1, "Boy.": 1}
        self.assertEqual(expected, result)

    def test_histogram_2(self):
        result = lab6.histogram("The Boy is a Big Boy (wow).")
        expected = {"The": 1, "Boy": 2, "is": 1, "a" : 1, "Big": 1, "(wow).": 1}
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
