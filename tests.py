import unittest


class DesTests(unittest.TestCase):
    #test2
    def test(self):
        self.assertTrue(True)

    def autre_test(self):
        self.assertEquals(3, 3)


if __name__ == '__main__':
    unittest.main()