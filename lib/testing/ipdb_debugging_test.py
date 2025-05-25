#!/usr/bin/env python3

from ipdb_debugging import plus_two

class TestIpdbDebugging:
    '''ipdb_debugging.py'''
    
    def test_adds_two(self):
        returned_value = plus_two(3)
        assert(plus_two(3) == 5)
