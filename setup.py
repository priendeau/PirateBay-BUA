from distutils.core import setup
from PirateBayBUA import __version__
from PirateBayBUA import exceptions
from PirateBayBUA import categories


setup(
    name="PirateBayBUA",
    version=__version__,
    description="A python interface to thepiratebay dot org. PirateBay Json, Python Query analysis, implemented with Better User Agent and Aparatus in << Software Pirating Analysis >> know in detection of malware, virus and Evil intention. ",
    license="BSD NEW LICENCE, PS, no regulation over method of displaying in Specific text content, here a bzip2/base64 inline license: QlpoOTFBWSZTWT9S45QAAAvfgFAQUHf0HT/n/+A/79/wUANmzTYA3ZVBKBE00yU8TSaTFHlDyT1GM1JoNDENBpqZGkFHo1GgaepoNAAA9Q9CGgip71Mon6ptIGjQAAAAANAAYqZqmamTymKDRpiAAYjBDQNGOYBNMAmQwABMEwAABwKoaf3zPkeXl2/9bz7uuUTVqXARwIfbwt+f371peX4mde+PUUYm0/G87r5Ll0Uvibmdnv616skpJabOw0YUgswy2hwU41DQGOfwoZowKTOjVQyhJQCDICeVrTS1OAYArlX2j7i91EAdBRxKK6nUQK6SOLKGCjCVa4FaZOTpg9TRWTOtEpCVgrUOsGU5M+cHZ3LuhMwUc3bivs6+9fDl9KYRLlsYelt5G/c/n6Gh0+bdm5B4ZNsfBIf9TIwj3WCQEHELiHP0CRevjO+LvdWU+VRSOSC177WlJJeXiJwzUuIoQUEkiLBUkZB5vVVjotg3xHEwgGv0gU44mKTac96SSYgWJ0Bg0gCG/AULick8o2SnoiIgqikw4QqnGWOS3RMVISxujynfRYaJDmDSNws5AnxFMTVGoxq6q17ZbHvKZIWTPfp4muaObMbhTlijD8ZMMo2LDqzMEAsWZBklIksKw4oR0zNJQA3E4mVckspqURKl89VzJF7NfZIfkqcF1FyZFUVTZRr4DQmpheZ4knSGJ0VWo478KhFZlycMcpI5ZsasoulSkQ+S0MFXi6W1N5GJkqumbD5DUQrg2UVU6L0mYrIiDcUGN0/rOq1xM9Ez1bRKRtI1oQspmk1dscYIgqYHmfb8+48pIfBT/YOfOnp9bVO+dU+hcTxWvuObmK8yiJH756YIoqqK5calcRJEUYsMaVETGsQAqr9FxMzv+rAcc566ZtQnYTzNZZG8qQmhSKX3EpEQEAZr5e8CBBqRPKA8T4jjdBLXOA5FkXgdiYpoqJPZKGvafVwodSjJadDhnipI7+KQmnXSJkR0jPI/CcPA5LNUYH7HJoGYpxczBiGVkr0rooIt4y4VA3CiEev/ntTaKBVa08CxyOozOKRNNVDVGFRVF4m6QkRcT5JH2eqU0E4VozB1AokUrRFnRZqwhGdTyiAxeERWJlCQPlgZeuV7k6mSIQzIoxjAqujELMKS5TsppG4sqlTQY3QUpqxmqTQpRZGyYf+LuSKcKEgfqXHKAA==",
    url="git://github.com/priendeau/PirateBay-BUA.git",
    long_description="PirateBay Json, Python Query analysis, implemented with Better User Agent and Aparatus in << Software Pirating Analysis >> know in detection of malware, virus and Evil intention.",
    packages=["PirateBayBUA"],
    cmdclass={ 'categories': categories }
)
