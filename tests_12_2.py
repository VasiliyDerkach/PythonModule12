import  unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
    def setUp(self):
        self.runners=[]
        self.runners.append(runner_and_tournament.Runner('Усэйн',10))
        self.runners.append(runner_and_tournament.Runner('Андрей',9))
        self.runners.append(runner_and_tournament.Runner('Ник',3))
        self.outsider = self.runners[2]
    @classmethod
    def tearDownClass(cls):

        for a in TournamentTest.all_results:
            print('{',end='')
            for k,u in a.items():
                print(k,':',u.name,end=' ,')
            print('}')
    def test_13(self):
        t13 = runner_and_tournament.Tournament(90,self.runners[0],self.runners[2])
        dres = t13.start()
        TournamentTest.all_results.append(dres)
        self.assertTrue(dres[max(dres.keys())]==self.outsider.name)
    def test_23(self):
        t23 = runner_and_tournament.Tournament(90,self.runners[1],self.runners[2])
        dres = t23.start()
        TournamentTest.all_results.append(dres)
        self.assertTrue(dres[max(dres.keys())]==self.outsider.name)
    def test_123(self):
        t123 = runner_and_tournament.Tournament(90,self.runners[0],self.runners[1],self.runners[2])
        dres = t123.start()
        TournamentTest.all_results.append(dres)
        self.assertTrue(dres[max(dres.keys())]==self.outsider.name)
    def test_minidist(self):
        t123 = runner_and_tournament.Tournament(90,self.runners[0],self.runners[1],self.runners[2])
        speeds = [v.speed for v in t123.participants]
        #print(speeds)
        t123.full_distance = 2*min(speeds)
        dres = t123.start()
        TournamentTest.all_results.append(dres)
        self.assertTrue(dres[max(dres.keys())]==self.outsider.name)

if __name__=='__main__':
    unittest.main()