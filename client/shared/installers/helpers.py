import os
import shutil


class LocalSourceDirHelper(object):
    '''
    Helper class to deal with source code sitting somewhere in the filesystem
    '''
    def __init__(self, source_dir, destination_dir):
        '''
        :param source_dir: the directory where the pristine source code is
        :param destination_dir: the directory to where a copy of the pristine
                                source code will be copied
        :return: new LocalSourceDirHelper instance
        '''
        self.source = source_dir
        self.destination = destination_dir


    def execute(self):
        '''
        Copies the source directory to the destination directory

        This recursively removes the :attr:`destination` directory, so make
        sure you do not pass a directory other than the directory holding
        the previous version of the source code.
        '''
        if os.path.isdir(self.destination):
            shutil.rmtree(self.destination)

        if os.path.isdir(self.source):
            shutil.copytree(self.source, self.destination)


