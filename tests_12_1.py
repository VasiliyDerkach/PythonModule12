import unittest
import runner12

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rn = runner12.Runner('Fake')
        for i in range(1,10):
            rn.walk()
        self.assertEqual(rn.distance,50)
    def test_run(self):
        rn = runner12.Runner('Fake')
        for i in range(1,10):
            rn.run()
        self.assertEqual(rn.distance,100)
    def test_challenge(self):
        rn = runner12.Runner('Fake')
        rn1 = runner12.Runner('Lord')
        for i in range(1,10):
            rn.run()
            rn.walk()
        self.assertNotEqual(rn.distance,rn1.distance)
if __name__=='__main__':
    unittest.main()
