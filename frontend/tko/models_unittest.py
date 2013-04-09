#!/usr/bin/python

import unittest
try:
    import autotest.common as common
except ImportError:
    import common
from autotest.frontend import setup_django_environment
from autotest.frontend import test_utils
from autotest.frontend.tko import models


class IterationAttributeTest(unittest.TestCase,
                             test_utils.FrontendTestMixin):
    def setUp(self):
        self._frontend_common_setup()


    def tearDown(self):
        self._frontend_common_teardown()


    def _create_test(self):
        machine = models.Machine.objects.create(hostname='foo.bar')
        job = models.Job.objects.create(tag='unittest.iterationattribute',
                                        label='foo',
                                        username='debug_user',
                                        machine=machine)
        kernel = models.Kernel.objects.create(kernel_hash='UNKNOWN',
                                              base='UNKNOWN',
                                              printable='UNKNOWN')
        status = models.Status.objects.get(word='GOOD')
        test = models.Test.objects.create(job=job,
                                          test='unittest',
                                          kernel=kernel,
                                          status=status,
                                          machine=machine)
        return test


    def test_single_attributes_for_one_test(self):
        test = self._create_test()
        iteration_attr = models.IterationAttribute.objects.create(
            test=test,
            iteration=1,
            attribute='attribute',
            value='value')
        iteration_attr.save()
        iteration_attr.delete()
        test.delete()


if __name__ == '__main__':
    unittest.main()
