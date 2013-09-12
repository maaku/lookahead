# -*- coding: utf-8 -*-
# Copyright © 2013 by its contributors. See AUTHORS for details.
# Distributed under the MIT/X11 software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
"Provides unit test cases for the `lookahead()` generator."

# Python standard library, unit-testing
import unittest2 as unittest

# Lookahead generator
from lookahead import lookahead

# Python patterns, scenario unit-testing
from scenariotest import ScenarioMeta, ScenarioTest

SCENARIOS = [
    # Test string iterables...
    dict(iterable='',         tuples=[]),
    dict(iterable='a',        tuples=[('a',None)]),
    dict(iterable='ab',       tuples=[('a','b'),('b',None)]),
    dict(iterable='abc',      tuples=[('a','b'),('b','c'),('c',None)]),
    # Test array iterables...
    dict(iterable=[],         tuples=[]),
    dict(iterable=[1],        tuples=[(1,None)]),
    dict(iterable=[1,2],      tuples=[(1,2),(2,None)]),
    dict(iterable=[1,2,3],    tuples=[(1,2),(2,3),(3,None)]),
    # Test tuple iterables...
    dict(iterable=(),         tuples=[]),
    dict(iterable=(1,),       tuples=[(1,None)]),
    dict(iterable=(1,'a'),    tuples=[(1,'a'),('a',None)]),
    dict(iterable=(1,'a',{}), tuples=[(1,'a'),('a',{}),({},None)]),
    # Test list of None values (edge case)...
    dict(iterable=[None]*3,   tuples=[(None,None),(None,None),(None,None)]),
    # Test single parameter form (lookahead)...
    dict(iterable=[1,2,3], args=(0,), tuples=[(1,),(2,),(3,)]),
    dict(iterable=[1,2,3], args=(1,), tuples=[(1,2),(2,3),(3,None)]),
    dict(iterable=[1,2,3], args=(2,), tuples=[(1,2,3),(2,3,None),(3,None,None)]),
    dict(iterable=[1,2,3], args=(3,), tuples=[(1,2,3,None),(2,3,None,None),(3,None,None,None)]),
    # Test twin parameter form (lookbehind, lookahead)...
    dict(iterable=[1,2,3], args=(0,0), tuples=[(1,),(2,),(3,)]),
    dict(iterable=[1,2,3], args=(0,1), tuples=[(1,2),(2,3),(3,None)]),
    dict(iterable=[1,2,3], args=(0,2), tuples=[(1,2,3),(2,3,None),(3,None,None)]),
    dict(iterable=[1,2,3], args=(0,3), tuples=[(1,2,3,None),(2,3,None,None),(3,None,None,None)]),
    dict(iterable=[1,2,3], args=(1,0), tuples=[(None,1,),(1,2,),(2,3,)]),
    dict(iterable=[1,2,3], args=(1,1), tuples=[(None,1,2),(1,2,3),(2,3,None)]),
    dict(iterable=[1,2,3], args=(1,2), tuples=[(None,1,2,3),(1,2,3,None),(2,3,None,None)]),
    dict(iterable=[1,2,3], args=(1,3), tuples=[(None,1,2,3,None),(1,2,3,None,None),(2,3,None,None,None)]),
    dict(iterable=[1,2,3], args=(2,0), tuples=[(None,None,1,),(None,1,2,),(1,2,3,)]),
    dict(iterable=[1,2,3], args=(2,1), tuples=[(None,None,1,2),(None,1,2,3),(1,2,3,None)]),
    dict(iterable=[1,2,3], args=(2,2), tuples=[(None,None,1,2,3),(None,1,2,3,None),(1,2,3,None,None)]),
    dict(iterable=[1,2,3], args=(2,3), tuples=[(None,None,1,2,3,None),(None,1,2,3,None,None),(1,2,3,None,None,None)]),
    dict(iterable=[1,2,3], args=(3,0), tuples=[(None,None,None,1,),(None,None,1,2,),(None,1,2,3,)]),
    dict(iterable=[1,2,3], args=(3,1), tuples=[(None,None,None,1,2),(None,None,1,2,3),(None,1,2,3,None)]),
    dict(iterable=[1,2,3], args=(3,2), tuples=[(None,None,None,1,2,3),(None,None,1,2,3,None),(None,1,2,3,None,None)]),
    dict(iterable=[1,2,3], args=(3,3), tuples=[(None,None,None,1,2,3,None),(None,None,1,2,3,None,None),(None,1,2,3,None,None,None)]),
]

class TestBaseEncode(unittest.TestCase):
    "Test the behavior of `lookahead()` from within a variety of illustrative scenarios."
    __metaclass__ = ScenarioMeta
    class test_lookahead(ScenarioTest):
        scenarios = SCENARIOS
        def __test__(self, iterable, tuples, args=(), kwargs={}):
          self.assertEqual(list(lookahead(iterable, *args, **kwargs)), tuples)
