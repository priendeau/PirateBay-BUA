from distutils.core import setup
from PirateBayBUA import __version__
from PirateBayBUA import exceptions
from PirateBayBUA import categories
from PirateBayBUA import ObjectCodeAnalysis


setup(
    name="PirateBayBUA",
    version=__version__,
    description="A python interface to thepiratebay dot org. PirateBay Json, Python Query analysis, implemented with Better User Agent and Aparatus in << Software Pirating Analysis >> know in detection of malware, virus and Evil intention. ",
    license="BSD NEW LICENCE",
    url="http://github.com/priendeau/PirateBay-BUA/blob/master/dist/PirateBayBUA-%s-apha-netcy.tar.gz" % ( __version__ ),
    long_description="PirateBay Json, Python Query analysis, implemented with Better User Agent and Aparatus in << Software Pirating Analysis >> know in detection of malware, virus and Evil intention.",
    packages=["PirateBayBUA"],
    cmdclass={ 'categories': categories }
)
