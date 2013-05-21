#!/usr/bin/env python

#  Copyright(c) 2013 Intel Corporation.
#
#  This program is free software; you can redistribute it and/or modify it
#  under the terms and conditions of the GNU General Public License,
#  version 2, as published by the Free Software Foundation.
#
#  This program is distributed in the hope it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin St - Fifth Floor, Boston, MA 02110-1301 USA.
#
#  The full GNU General Public License is included in this distribution in
#  the file called "COPYING".

import unittest
import sys
try:
    import autotest.common as common
except ImportError:
    import common
from autotest.client.shared import backports


def is_python_26_or_greater():
    if sys.version_info[0] >= 3:
        return True
    if sys.version_info[0] >= 2 and sys.version_info[1] >= 6:
        return True
    return False


class TestBackports(unittest.TestCase):

    @staticmethod
    def test_any():
        assert backports.any([False, 0, 1, "", True, set()])
        assert not backports.any([])
        assert not backports.any(set())
        assert not backports.any(["", 0, False])

    @staticmethod
    def test_all():
        assert not backports.all([False, 0, 1, "", True])
        assert backports.all([])
        assert not backports.all(["", 0, False, set()])
        assert backports.all(["True", 1, True])

    @staticmethod
    def test_bin():
        assert backports.bin(170) == '0b10101010'

    if is_python_26_or_greater():
        @staticmethod
        def test_many_bin():
            for n in xrange(10000):
                assert backports.bin(n) == bin(n)
            assert backports.bin(sys.maxint) == bin(sys.maxint)

    @staticmethod
    def test_next():
        assert backports.next((x * 2 for x in range(3, 5))) == 6
        assert backports.next((x * 2 for x in range(3, 5) if x > 100), "default") == "default"
        try:
            backports.next((x * 2 for x in range(3, 5) if x > 100), "default", "extra arg")
            assert False
        except TypeError:
            pass


if __name__ == '__main__':
    unittest.main()
