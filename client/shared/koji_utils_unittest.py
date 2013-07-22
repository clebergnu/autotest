#!/usr/bin/python

import unittest

from autotest.client.shared import koji_utils


class KojiDirIndexParserTest(unittest.TestCase):
    '''
    Test class for KojiDirIndexParser
    '''

    SAMPLE_HTML = '''
<html>
<body>
<a href="foo-1.0-1.rpm">foo</a>
<a href="bar-2.0-2.rpm">bar</a>
<p>This page mentions package baz-3.0-3.rpm</p>
</body>
</html>
'''

    def test_parse_dir_with_rpms(self):
        '''
        Tests that the two package listed on SAMPLE_HTML are identified
        '''
        parser = koji_utils.KojiDirIndexParser()
        parser.feed(self.SAMPLE_HTML)
        self.assertIn('foo-1.0-1.rpm', parser.package_file_names)
        self.assertIn('bar-2.0-2.rpm', parser.package_file_names)


    def test_parse_only_tags(self):
        '''
        Tests that only rpm file names in a <a> tag are identified
        '''
        parser = koji_utils.KojiDirIndexParser()
        parser.feed(self.SAMPLE_HTML)
        self.assertNotIn('baz-3.0-3.rpm', parser.package_file_names)


class RPMFileNameInfoTest(unittest.TestCase):
    '''
    Test class for RPMFileNameInfo
    '''

    FILENAME = 'kernel-3.9.5-301.fc19.x86_64.rpm'

    def test_get_filename_without_suffix(self):
        rfi = koji_utils.RPMFileNameInfo(self.FILENAME)
        self.assertEqual(rfi.get_filename_without_suffix(),
                         'kernel-3.9.5-301.fc19.x86_64')


    def test_get_filename_without_arch(self):
        rfi = koji_utils.RPMFileNameInfo(self.FILENAME)
        self.assertEqual(rfi.get_filename_without_arch(),
                         'kernel-3.9.5-301.fc19')


    def test_get_arch(self):
        rfi = koji_utils.RPMFileNameInfo(self.FILENAME)
        self.assertEqual(rfi.get_arch(), 'x86_64')


    def test_nvr_info_no_koji(self):
        rfi = koji_utils.RPMFileNameInfo(self.FILENAME)
        if not koji_utils.KOJI_INSTALLED:
            self.assertEqual(rfi.get_nvr_info(), None)
        else:
            nvr_info = rfi.get_nvr_info()
            self.assertEqual(nvr_info['epoch'], '')
            self.assertEqual(nvr_info['name'], 'kernel')
            self.assertEqual(nvr_info['release'], '301.fc19')
            self.assertEqual(nvr_info['version'], '3.9.5')


if __name__ == '__main__':
    unittest.main()
