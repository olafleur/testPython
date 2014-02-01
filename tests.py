# coding=utf-8
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

import unittest


class TestTeamcityMessages(unittest.TestCase):
    def test_pass(self):
        assert 1 == 1

    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)


if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)