# -*- coding: utf-8 -*-

import sys
import os

try:
    import autotest.common
except ImportError:
    import common

from autotest.client.shared.version import get_version
from autotest.frontend import setup_django_environment

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode']


master_doc = 'index'
project = u'autotest'
copyright = u'2013, Autotest Team'

v_parts = get_version().split('.')
version = "%s.%s" % (v_parts[0], v_parts[1])
release = '%s.%s.%s' % (v_parts[0], v_parts[1], v_parts[2])

pygments_style = 'sphinx'

latex_documents = [
    ('index', 'autotest.tex', u'autotest Documentation',
     u'Autotest Team', 'manual'),
]

man_pages = [
    ('index', 'autotest', u'autotest Documentation',
     [u'Autotest Team'], 1)
]


texinfo_documents = [
    ('index', 'autotest', u'autotest Documentation',
     u'Autotest Team', 'autotest', 'One line description of project.',
     'Miscellaneous'),
]

epub_title = u'autotest'
epub_author = u'Autotest Team'
epub_publisher = u'Autotest Team'
epub_copyright = u'2013, Autotest Team'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'django': ('http://docs.djangoproject.com/en/dev/',
               'http://docs.djangoproject.com/en/dev/_objects/')
}
