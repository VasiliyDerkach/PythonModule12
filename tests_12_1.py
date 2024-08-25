import unittest
import runner12

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rn0 = runner12.Runner('Fake')
        for i in range(10):
            rn0.walk()
        self.assertEqual(rn0.distance,50)
    def test_run(self):
        rn = runner12.Runner('Fake')
        for i in range(10):
            rn.run()
        self.assertEqual(rn.distance,100)
    def test_challenge(self):
        rn2 = runner12.Runner('Fake')
        rn1 = runner12.Runner('Lord')
        for i in range(10):
            rn2.run()
            rn1.walk()
        self.assertNotEqual(rn2.distance,rn1.distance)
if __name__=='__main__':
    unittest.main()
