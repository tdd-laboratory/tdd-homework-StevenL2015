import unittest
import library


NUM_CORPUS = '''
On the 5th of May every year, Mexicans celebrate Cinco de Mayo. This tradition
began in 1845 (the twenty-second anniversary of the Mexican Revolution), and
is the 1st example of a national independence holiday becoming popular in the
Western Hemisphere. (The Fourth of July didn't see regular celebration in the
US until 15-20 years later.) It is celebrated by 77.9% of the population--
trending toward 80.                                                                
'''

class TestCase(unittest.TestCase):

    # Helper function
    def assert_extract(self, text, extractors, *expected):
        actual = [x[1].group(0) for x in library.scan(text, extractors)]
        self.assertEqual(str(actual), str([x for x in expected]))

    # First unit test; prove that if we scan NUM_CORPUS looking for mixed_ordinals,
    # we find "5th" and "1st".
    def test_mixed_ordinals(self):
        self.assert_extract(NUM_CORPUS, library.mixed_ordinals, '5th', '1st')

    # Second unit test; prove that if we look for integers, we find four of them.
    def test_integers(self):
        self.assert_extract(NUM_CORPUS, library.integers, '1845', '15', '20', '80')

    # Third unit test; prove that if we look for integers where there are none, we get no results.
    def test_no_integers(self):
        self.assert_extract("no integers", library.integers)

    #4
    def test_extract_date(self):
        self.assert_extract("First date 2015-07-25.", library.dates_iso8601, "2015-07-25")

    #6/7
    def test_invalid_date(self):
        self.assert_extract("hello 2017-99-31.", library.dates_iso8601)
        # 2015-07(<12)-25(<31)

    #8/9
    def test_date_format(self):
        self.assert_extract('This is important 25 Jan 2017.', library.date_pattern, '25 Jan 2017')

    #10+
    # def test_8601_1(self):
    #     self.assert_extract('The date is 2018-06-22 18:22:19.123.',
    #                         library.dates_iso8601, "2018-06-22 18:22:19.123")

    # def test_8601_2(self):
    #     self.assert  2018-06-22T18:22:19.123
    #
    # def test_8601_3(self):
    #     self.assert  2018-06-22 18:22:19.123 MDT
    #
    # def test_8601_4(self):
    #     self.assert  2018-06-22 18:22:19.123-8000
    #
    # def test_8601_5(self):
    #     self.assert  25 Jun, 2017
    #
    # def test_8601_6(self):
    #     self.assert  123,456,789
    #
    # def test_8601_7(self):
    #     self.assert  2018-06-22 18:22:19.123
    #
    # def test_8601_8(self):
    #     self.assert  2018-06-22 18:22:19.123Z


if __name__ == '__main__':
    unittest.main()
