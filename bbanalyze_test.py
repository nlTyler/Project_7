from unittest import TestCase
from unittest import main
import shelve
from bbanalyze import bbanalyze
import pandas as pd
import numpy as np
import math


def compFloat(exp, act, atol=0.00001):
    if math.isnan(exp) and math.isnan(act):
        return True
    if math.isinf(exp) and math.isinf(act):
        return True
    return np.isclose(exp, act, atol=atol)


def compSeries(exp: pd.Series, act: pd.Series, atol=0.000001):
    if exp.equals(act):
        return True
    return exp.apply(lambda x, y: compFloat(x, y), args=(act,)).all()


class Test_bbanalyze(TestCase):
    def setUp(self):
        with shelve.open('expected_results') as expected_results:
            self.exp = expected_results['bbanalyze']
            self.act = bbanalyze()

    def test_bb(self):
        bbexp = self.exp['bb']
        bbact = self.act['bb']
        self.assertTrue(bbexp.equals(bbact))

    def test_al(self):
        al_exp = self.exp['al']
        al_act = self.act['al']
        self.assertEqual(al_exp['players'], al_act['players'])
        self.assertEqual(al_exp['teams'], al_act['teams'])

    def test_nl(self):
        nl_exp = self.exp['nl']
        nl_act = self.act['nl']
        self.assertEqual(nl_exp['players'], nl_act['players'])
        self.assertEqual(nl_exp['teams'], nl_act['teams'])

    def test_record_count(self):
        self.assertEqual(self.exp['record.count'], self.act['record.count'])


if __name__ == '__main__':
    main(verbosity=2)