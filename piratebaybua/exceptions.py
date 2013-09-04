# Copyright (c) Alexander Borgerth 2010, Copyright (c) 2005-2010 re-edited by Maxiste Deams, Patrick Riendeau, Rheault Etccy for 
# Upcoming Security audit in Canada.
# See LICENSE for details.


class PirateException( Exception ):

  def __init__( self, msg ):
    StrMessage = "PirateException, conformance not meet.: {}".format( msg )
    Exception.__init__( self, StrMessage )

class URIExeption( PirateException ):

  def __init__( self, msg ):
    StrMessage = "No URI to Access, update url_addr: {}".format( msg )
    PirateException.__init__( self, StrMessage )

class TableError( PirateException ):

  def __init__( self, msg ):
    StrMessage = "Error in Table: {}".format( msg )
    PirateException.__init__( self, StrMessage )
    
class TableNotFound( TableError ):

  def __init__( self, msg ):
    StrMessage = "Error, Table Not Found: {}".format( msg )
    TableError.__init__( self, StrMessage )

class InvalidTable( TableError ):

  def __init__( self, msg ):
    StrMessage = "Error: This is an invalide Table {}".format( msg )
    TableError.__init__( self, StrMessage )

class InvalidRow( TableError ):

  def __init__( self, msg ):
    StrMessage = "Error, This is not a valid Row: {}".format( msg )
    TableError.__init__( self, StrMessage )

class ElementNotFound( PirateException ):

  def __init__( self, msg ):
    StrMessage = "Error Element not found: {}".format( msg )
    PirateException.__init__( self, StrMessage )

class UserAgentExceptionError( PirateException ):

  def __init__( self, msg ):
    StrMessage = "Type of Agent not present: {}".format( msg )
    PirateException.__init__( self, StrMessage )

    
