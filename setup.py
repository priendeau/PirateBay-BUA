from distutils.core import setup
from PirateBayBUA import __version__
from PirateBayBUA import exceptions
from PirateBayBUA import categories


setup(
    name="PirateBayBUA",
    version=__version__,
    description="A python interface to thepiratebay dot org. PirateBay Json, Python Query analysis, implemented with Better User Agent and Aparatus in << Software Pirating Analysis >> know in detection of malware, virus and Evil intention. ",
    license="BSD NEW LICENCE",
    url="git://github.com/priendeau/PirateBay-BUA.git",
    long_description="PirateBay Json, Python Query analysis, implemented with Better User Agent and Aparatus in << Software Pirating Analysis >> know in detection of malware, virus and Evil intention.",
    packages=["PirateBayBUA"],
    cmdclass={ 'categories': categories }
)
