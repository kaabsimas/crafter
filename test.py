from tests.configTest import ConfigDicTestCase, ConfigFileTestCase
import unittest

cases = [
    ConfigDicTestCase,
    ConfigFileTestCase
    # //gameTest.GameTestCase,
    # //scenarioListTest.ScenarioListTestCase,
]
suite = unittest.TestSuite()
for case in cases:
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(case))
unittest.TextTestRunner(verbosity=2).run(suite)
