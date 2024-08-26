import unittest
import runner

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        rn0 = runner.Runner('Fake')
        for i in range(10):
            rn0.walk()
        self.assertEqual(rn0.distance,50)

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        rn = runner.Runner('Fake')
        for i in range(10):
            rn.run()
        self.assertEqual(rn.distance,100)

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rn2 = runner.Runner('Fake')
        rn1 = runner.Runner('Lord')
        for i in range(10):
            rn2.run()
            rn1.walk()
        self.assertNotEqual(rn2.distance,rn1.distance)
if __name__=='__main__':
    unittest.main()
