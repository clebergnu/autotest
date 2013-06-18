'''
Installer classes are responsible for building and installing specific software
components.

It's possible to group them based on whether the installers contain
functionality that targets the proper installation of a specific software
package.
'''


class InstallerHasNoMode(Exception):
    '''
    Exception raised when the installer to be installed has no mode defined
    '''
    pass


class InstallerRegistry(dict):
    '''
    Holds information on known installer classes

    This class is used to create a single instance, named INSTALLER_REGISTRY,
    that will hold all information on known installer types.

    For registering a new installer class, use the register() method. If the
    virt type is not set explicitly, it will be set to 'base'. Example:

    >>> INSTALLER_REGISTRY.register('yum', base_installer.YumInstaller)

    If you want to register a virt specific installer class, set the virt
    (third) param:

    >>> INSTALLER_REGISTRY.register('yum', qemu_installer.YumInstaller, 'qemu')

    For getting a installer class, use the get_installer() method. This method
    has a fallback option 'get_default_virt' that will return a generic virt
    installer if set to true.
    '''

    #: A specialization class is a grouping of installers that are tunned to a
    #: specific group of software packages. Suppose that installing a piece of
    #: software, be it from source code or from a binary package involves
    #: similar or even identical steps. This would be a good target for having
    #: a installer specialization class shared among all installers for that
    #: specific software component.
    DEFAULT_SPECIALIZATION = None

    def __init__(self, **kwargs):
        dict.__init__(self, **kwargs)
        self[self.DEFAULT_SPECIALIZATION] = {}


    def register(self, klass, specialization=None):
        '''
        Register a class as responsible for installing software components

        If :param:`specialization` is not set, it will assume a default value
        of :attr:`DEFAULT_SPECIALIZATION_NAME`.
        '''
        if not hasattr(klass, 'MODE'):
            raise InstallerHasNoMode

        if not self.has_key(specialization):
            self[specialization] = {}

        self[specialization][klass.MODE] = klass


    def get_installer(self, mode, specialization=None, get_default=False):
        '''
        Gets a installer class that should be able to install the virt software

        Always try to use classes that are specific to the virtualization
        technology that is being tested. If you have confidence that the
        installation is rather trivial and does not require custom steps, you
        may be able to get away with a base class (by setting get_default
        to True).
        '''
        if not self.has_key(specialization):
            # return a base installer so the test could and give it a try?
            if get_default:
                return self[self.DEFAULT_SPECIALIZATION].get(mode)
        else:
            return self[specialization].get(mode)


    def get_modes(self, specialization=None):
        '''
        Returns a list of all registered installer modes
        '''
        if not self.has_key(specialization):
            return []

        return self[specialization].keys()


#
# InstallerRegistry unique instance
#
INSTALLER_REGISTRY = InstallerRegistry()


def get():
    '''
    Shortcut that returns the installer registry
    '''
    global INSTALLER_REGISTRY
    return INSTALLER_REGISTRY


def reset():
    '''
    Resets the installer registry with a brand new instance
    '''
    global INSTALLER_REGISTRY
    INSTALLER_REGISTRY = InstallerRegistry()
