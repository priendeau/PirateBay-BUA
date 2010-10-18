# Copyright (c) Copyright (c) 2005-2010 re-edited by Maxiste Deams, Patrick Riendeau, Rheault Etccy for 
# Upcoming Security audit in Canada.
# See LICENSE for details.

### This is the code Analysis section, which is intented to analyse both Elf, windows PE
### Code-linking, and producing information over 
###

### FileName : ObjectCodeAnalysis.py

import uuid, datetime, time, logging, GenericCache, pylibelf
from GenericCache.GenericCache import GenericCache
from GenericCache.decorators import cached
from uuid import uuid4
from decorator import *
#from PirateBayBUA import StructReference
import StructReference

class NotImplementedYet( Warning ):
  Msg='NotImplementedYet raised for Future developpment or schema not completed from function %s, class: %s'
  MsgClass='NotImplementedYet raised for Future developpment or schema not completed No Member Are registered in class %s'
  FuncName, ClassName, ObjectNotYetList = None, None, None

  class ValueTransfertException( Exception ):
    Msg='ValueTransfertException raised , invalid number of Key transferred, lower than %d.'
    IntMinArgAgree=3
    IntScanValue=None
    def __init__(self, value ):
      self.IntScanValue=len(value)
      if self.IntScanValue < self.IntMinArgAgree:
        Exception.__init__( self, self.Msg % ( self.IntMinArgAgree ) )
      else:
        pass
  
  def __init__( self, value ):
    raise NotImplementedYet.ValueTransfertException, value
    self.FuncName, self.ClassName, self.ObjectNotYetList = value
    if not self.ClassName in self.ObjectNotYetList.keys():
        Warning.__init__( self, self.MsgClass % ( value ) )
    else:
        if not self.FuncName in self.ObjectAllPass[self.ClassName]:
          Warning.__init__( self, self.Msg % ( self.FuncName, self.ClassName ) )
        else:
          pass

class GenericCacheCodecImplement(  ):
  CodeBytePlay = dict()
  __allPass__={ 'GenericCacheCodecImplement':[],
                'GenericCacheCodecFactory':[] }
  
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

  class GenericCacheCodecFactory( object ):
    CodeBytePlay = dict()
    #DefaultNotImplemented=GenericCacheCodecImplement.NotImplementedYet
    #DefaultNotImplemented=GenericCacheCodecImplement.NotImplementedYet

    @BytePlayEncoder( CodeBytePlay, 'GenericCacheCodecFactory' )
    def OpenCache( self ):
      raise NotImplementedYet, [ self.OpenCache.__name__, self.__class__.__name__ , self.__allPass__ ]
      """
        OpenCache Proc
      """
      print "Function %s" % ( self.OpenCache.__name__ )

  @BytePlayEncoder( CodeBytePlay, 'GenericCacheCodecImplement' )
  def GetPathTopologyKey( self , DefaultKey = 'uniformPath' ):
    raise NotImplementedYet, [self.GetPathTopologyKey.__name__, self.__class__.__name__, self.__allPass__]
    if self.EnvType == None:
      self.PathStoreLogThisNode=self.FileNode[DefaultKey]['thisnode']
    else:
      for ItemKey in self.FileNode.keys():
        if self.EnvType in self.FileNode[ItemKey]['list']:
          self.PathStoreLogThisNode=self.FileNode[ItemKey]['thisnode'] 
          
      
  @BytePlayEncoder( CodeBytePlay, 'GenericCacheCodecImplement' )
  def StartLog( self ):
    raise NotImplementedYet, [self.StartLog.__name__, self.__class__.__name__, self.__allPass__]
    if not self.StartLog.__name__ in __allPass__:
      raise self.NotImplementedYet, self.StartLog.__name__
    self.UUIDLogInstance=str(uuid4())
    
    ListMainLogFormat=( Atime[0],Atime[1],Atime[2],Atime[3],Atime[4],Atime[5], self.UUIDLogInstance )
    if self.PathStoreLog == None:
      logging.basicConfig(filename=DictReference['log']( Atime[0],Atime[1],Atime[2],Atime[3],Atime[4],Atime[5],str(uuid4())),level=logging.DEBUG)

  @BytePlayEncoder( CodeBytePlay, 'GenericCacheCodecImplement' )
  def __init__( self, **Kargs ):
    raise NotImplementedYet, [ self.__init__.__name__, self.__class__.__name__ ,self.__allPass__]
    self.CachedInstance=self.GenericCacheCodecFactory( )
    for ItemKey in Kargs.keys():
      setattr( self.file, ItemKey , Kargs[ItemKey] )
    if not self.__init__.__name__ in __allPass__:
      raise self.NotImplementedYet, self.__init__.__name__

class ObjectCodeAnalysisImplement( object ):
  ObjectCached = GenericCacheCodecImplement()
  CodeBytePlay = dict()
  __allPass__={ 'ObjectCodeAnalysisImplement':[ ] ,
                'ObjectCodeAnalysisFactory':[],
                'AnalysisFactoryELF':[],
                'AnalysisFactoryPE':[]}
  
  class ObjectCodeAnalysisFactory( ObjectCodeAnalysisImplement ):
    CodeBytePlay = dict()
    
    class AnalysisFactoryELF( ObjectCodeAnalysisFactory ):
      CodeBytePlay = dict()

      DefaultNotImplemented=ObjectCodeAnalysisImplement().NotImplementedYet

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryELF' )
      def A( self ):
        raise self.DefaultNotImplemented, [self.A.__name__, self.__class__.__name__,self.__allPass__]

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryELF' )
      def AA( self ):
        raise self.DefaultNotImplemented, [self.AA.__name__, self.__class__.__name__,self.__allPass__]

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryELF' )
      def AB( self ):
        raise self.DefaultNotImplemented, [self.AB.__name__, self.__class__.__name__,self.__allPass__]

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryELF' )
      def B( self ):
        raise self.DefaultNotImplemented, [self.B.__name__, self.__class__.__name__,self.__allPass__]

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryELF' )
      def BB( self ):
        raise self.DefaultNotImplemented, [ self.BB.__name__, self.__class__.__name__,self.__allPass__ ]

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryELF' )
      def BA( self ):
        raise self.DefaultNotImplemented, [self.BA.__name__, self.__class__.__name__,self.__allPass__]
      


    class AnalysisFactoryPE( ObjectCodeAnalysisFactory ):
      CodeBytePlay = dict()
      DefaultNotImplemented=ObjectCodeAnalysisImplement().NotImplementedYet

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryPE' )
      def A( self ):
        raise self.DefaultNotImplemented, self.A.__name__, self.__class__.__name__

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryPE' )
      def AA( self ):
        raise self.DefaultNotImplemented, self.AA.__name__, self.__class__.__name__

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryPE' )
      def AB( self ):
        raise self.DefaultNotImplemented, self.AB.__name__, self.__class__.__name__

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryPE' )
      def B( self ):
        raise self.DefaultNotImplemented, self.B.__name__, self.__class__.__name__

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryPE' )
      def BB( self ):
        raise self.DefaultNotImplemented, self.BB.__name__, self.__class__.__name__

      @BytePlayEncoder( CodeBytePlay, 'AnalysisFactoryPE' )
      def BA( self ):
        raise self.DefaultNotImplemented, self.BA.__name__, self.__class__.__name__
      
  @BytePlayEncoder( CodeBytePlay, 'ObjectCodeAnalysisFactory' )
  def __init__( self , **Kargs ):
    raise self.NotImplementedYet, self.__init__.__name__
    self.CachedInstance=self.GenericCacheCodecFactory( )
    for ItemKey in Kargs.keys():
      setattr( self.file, ItemKey , Kargs[ItemKey] )
      
    
