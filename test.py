from tests import configTest
import unittest

cases = [
    # //gameTest.GameTestCase,
    # //scenarioListTest.ScenarioListTestCase,
    configTest.ConfigDicTestCase,
    configTest.ConfigFileTestCase
]

for case in cases:
    suite = unittest.TestLoader().loadTestsFromTestCase(case)
    unittest.TextTestRunner(verbosity=2).run(suite)
