from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    "output": 'smoke-repot'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)