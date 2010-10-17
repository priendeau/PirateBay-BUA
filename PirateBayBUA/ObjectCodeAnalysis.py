# Copyright (c) Copyright (c) 2005-2010 re-edited by Maxiste Deams, Patrick Riendeau, Rheault Etccy for 
# Upcoming Security audit in Canada.
# See LICENSE for details.

### This is the code Analysis section, which is intented to analyse both Elf, windows PE
### Code-linking, and producing information over 
###

### FileName : ObjectCodeAnalysis.py

import GenericCache
import pylibelf
from GenericCache.GenericCache import GenericCache
from GenericCache.decorators import cached
import datetime, time
import logging
import uuid
from uuid import uuid4
from PirateBuy import StructReference




class GenericCacheCodecImplement( object ):
  __allPass__={ 'GenericCacheCodecImplement':[],
                'GenericCacheCodecFactory':[] }
  
  class NotImplementedYet( Warning ):
    Msg='NotImplementedYet raised for Future developpment or schema not completed from function %s, class: %s'
    MsgClass='NotImplementedYet raised for Future developpment or schema not completed No Member Are registered in class %s'
    def __init__(self, value ):
      if len( value ) == 2:
        self.FuncName, self.ClassName = value
      if not self.ClassName in ObjectCodeAnalysisImplement.__allPass__.keys():
        Warning.__init__( self, self.MsgClass % ( value ) )
      else:
        if not self.FuncName in ObjectCodeAnalysisImplement[self.ClassName]:
          Warning.__init__( self, self.Msg % ( self.FuncName, self.ClassName ) )
        else:
          pass

  __allPass__=[ ]

  DictReference = { 'log':'%sObjectCodeAnalysis-%s%s%s-%s%s%s-%s.log' }
  CachedInstance=None
  PathStoreLog=None
  PathStoreLogThisNode=None
  ThisTimeIndexStruct=time.localtime()
  ListEnv=[ 'windows', 'linux', 'unix', 'solaris', 'bsd', 'cygwin', 'mingw',
            'mks', 'msvc', 'darwin', 'dgux', 'irix', 'ncr', 'osf',
            'openvms', 'qnx', 'unixware' ]
  FileNode={ 'uniformPath':{ 'thisnode':'./' ,
                               'list':['linux', 'unix', 'solaris', 'bsd', 'cygwin', 'mingw', 'mks',
                                       'darwin', 'dgux', 'irix', 'ncr', 'osf', 'openvms', 'qnx', 'unixware'] },
             'diskFirst':{ 'thisnode':'' ,
                           'list':[ 'windows','msvc' ] } }
  EnvType=None

  class GenericCacheCodecFactory( GenericCacheCodecImplement ):

    def OpenCache( self ):
      """
        OpenCache Proc
      """
      print "Function %s" % ( self.OpenCache.__name__ )

  def GetPathTopologyKey( self , DefaultKey = 'uniformPath' ):
    if self.EnvType == None:
      self.PathStoreLogThisNode=self.FileNode[DefaultKey]['thisnode']
    else:
      for ItemKey in self.FileNode.keys():
        if self.EnvType in self.FileNode[ItemKey]['list']:
          self.PathStoreLogThisNode=self.FileNode[ItemKey]['thisnode'] 
          
      

  def StartLog( self ):
    if not self.StartLog.__name__ in __allPass__:
      raise self.NotImplementedYet, self.StartLog.__name__
    self.UUIDLogInstance=str(uuid4())
    
    ListMainLogFormat=( Atime[0],Atime[1],Atime[2],Atime[3],Atime[4],Atime[5], self.UUIDLogInstance )
    if self.PathStoreLog == None:

        
      
      logging.basicConfig(filename=DictReference['log']( Atime[0],Atime[1],Atime[2],Atime[3],Atime[4],Atime[5],str(uuid4())),level=logging.DEBUG)

  def __init__( self, **Kargs ):
    self.CachedInstance=self.GenericCacheCodecFactory( )
    for ItemKey in Kargs.keys():
      setattr( self.file, ItemKey , Kargs[ItemKey] )
    if not self.__init__.__name__ in __allPass__:
      raise self.NotImplementedYet, self.__init__.__name__

class ObjectCodeAnalysisImplement( object ):
  ObjectCached = GenericCacheCodecImplement()
  __allPass__={ 'ObjectCodeAnalysisImplement':[ ] ,
                'ObjectCodeAnalysisFactory',
                'AnalysisFactoryELF':[],
                'AnalysisFactoryPE':[]}
  
  class NotImplementedYet( Warning ):
    Msg='NotImplementedYet raised for Future developpment or schema not completed from function %s, class: %s'
    MsgClass='NotImplementedYet raised for Future developpment or schema not completed No Member Are registered in class %s'
    def __init__(self, value ):
      if len( value ) == 2:
        self.FuncName, self.ClassName = value
      if not self.ClassName in ObjectCodeAnalysisImplement.__allPass__.keys():
        Warning.__init__( self, self.MsgClass % ( value ) )
      else:
        if not self.FuncName in ObjectCodeAnalysisImplement[self.ClassName]:
          Warning.__init__( self, self.Msg % ( self.FuncName, self.ClassName ) )
        else:
          pass

  class ObjectCodeAnalysisFactory( ObjectCodeAnalysisImplement ):

    class AnalysisFactoryELF( ObjectCodeAnalysisFactory ):

      def A( self ):
        raise self.NotImplementedYet, self.A.__name__, self.__class__.__name__
          

      def AA( self ):
        raise self.NotImplementedYet, self.AA.__name__, self.__class__.__name__

      def AB( self ):
        raise self.NotImplementedYet, self.AB.__name__, self.__class__.__name__
        
      def B( self ):
        raise self.NotImplementedYet, self.B.__name__, self.__class__.__name__

      def BB( self ):
        raise self.NotImplementedYet, self.BB.__name__, self.__class__.__name__

      def BA( self ):
        raise self.NotImplementedYet, self.BA.__name__, self.__class__.__name__
      


    class AnalysisFactoryPE( ObjectCodeAnalysisFactory ):
      def A( self ):
        raise self.NotImplementedYet, self.A.__name__, self.__class__.__name__

      def AA( self ):
        raise self.NotImplementedYet, self.AA.__name__, self.__class__.__name__

      def AB( self ):
        raise self.NotImplementedYet, self.AB.__name__, self.__class__.__name__
        
      def B( self ):
        raise self.NotImplementedYet, self.B.__name__, self.__class__.__name__

      def BB( self ):
        raise self.NotImplementedYet, self.BB.__name__, self.__class__.__name__

      def BA( self ):
        raise self.NotImplementedYet, self.BA.__name__, self.__class__.__name__
      
      
  def __init__( self , **Kargs ):
    raise self.NotImplementedYet, self.__init__.__name__
    self.CachedInstance=self.GenericCacheCodecFactory( )
    for ItemKey in Kargs.keys():
      setattr( self.file, ItemKey , Kargs[ItemKey] )
      
    
