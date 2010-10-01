# Copyright (c) Alexander Borgerth 2010, Copyright (c) 2005-2010 re-edited by Maxiste Deams, Patrick Riendeau, Rheault Etccy for 
# Upcoming Security audit in Canada.
# See LICENSE for details.



class PirateException(Exception):
    pass

class TableError(PirateException):
    pass
    
class TableNotFound(TableError):
    pass

class InvalidTable(TableError):
    pass

class InvalidRow(TableError):
    pass

class ElementNotFound(PirateException):
    pass
