import unittest
import tests_12_2
import tests_12_1

RunnerTSuite = unittest.TestSuite()
RunnerTSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
RunnerTSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
Runner = unittest.TextTestRunner(verbosity=2)
Runner.run(RunnerTSuite)