import rt_with_exceptions as runner
import unittest

import logging

class RunnerTest(unittest.TestCase):
    is_frozen = True
    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            rn0 = runner.Runner('Николай',-7)
            for i in range(10):
                rn0.walk()
            self.assertEqual(rn0.distance,50)
            logging.info('"test_run" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")


    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            rn = runner.Runner(['Шуоа','Мура'],10)
            for i in range(10):
                rn.run()
            self.assertEqual(rn.distance,100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rn2 = runner.Runner('Fake')
        rn1 = runner.Runner('Lord')
        for i in range(10):
            rn2.run()
            rn1.walk()
        self.assertNotEqual(rn2.distance,rn1.distance)
logging.basicConfig(filename='runner_tests.log',filemode='w',level=logging.INFO,encoding='UTF-8',format='%(asctime)s | %(levelname)s | %(message)s')
    #unittest.main()
