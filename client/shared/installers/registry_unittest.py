#!/usr/bin/python

import os
import re
import unittest
try:
    import autotest.common as common
except ImportError:
    import common

from autotest.client.shared.installers import registry


class NoopInstaller(object):
    '''
    Fake installer that does nothing
    '''
    MODE = 'noop'


class NoModeInstaller(object):
    '''
    Broken installer that has no mode set, and cannot be registered
    '''
    pass


class Registry(unittest.TestCase):

    def setUp(self):
        registry.reset()


    def test_register_noop(self):
        registry.get().register(NoopInstaller)


    def test_register_get_default_modes(self):
        self.assertEqual(registry.get().get_modes(), [])


    def test_register_noop_get_modes(self):
        registry.get().register(NoopInstaller)
        self.assertEqual(registry.get().get_modes(), ['noop'])


    def test_register_no_mode(self):
        self.assertRaises(registry.InstallerHasNoMode,
                          registry.get().register,
                          NoModeInstaller)



if __name__ == '__main__':
    unittest.main()
