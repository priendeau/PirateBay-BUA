import byteplay
from byteplay import *

def BytePlayEncoder( CodeBytePlay, ClassLevelName ):
    """
    This Decorator will create a Byteplay Statck known to Add Exception List in head of
    decorated function... Instead of adding raiser ( NotImplementedYet, Is ready ) This byteplay decorator
    will add it naturally, By playing with StackModule Level implemented close to here...

    See instruction on http://pypi.python.org/pypi/byteplay/N.N = ( 0.2 )

    The marshaller computes a key from function arguments
    """
    def decorator(func):
        def inner(*args, **kwargs):
            if not ClassLevelName in CodeBytePlay.keys():
                CodeBytePlay[ClassLevelName]=dict()
            CodeBytePlay[ClassLevelName][func.__name__]=Code.from_code(func.func_code) 
            func( *args, **kwargs )
        return inner
    return decorator
