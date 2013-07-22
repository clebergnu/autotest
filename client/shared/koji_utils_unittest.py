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


if __name__ == '__main__':
    unittest.main()
