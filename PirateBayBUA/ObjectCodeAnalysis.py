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
    self.UUIDLogInstance=str(uuid4())
    
    ListMainLogFormat=( Atime[0],Atime[1],Atime[2],Atime[3],Atime[4],Atime[5], self.UUIDLogInstance )
    if self.PathStoreLog == None:

        
      
      logging.basicConfig(filename=DictReference['log']( Atime[0],Atime[1],Atime[2],Atime[3],Atime[4],Atime[5],str(uuid4())),level=logging.DEBUG)

  def __init__( self, **Kargs ):
    self.CachedInstance=self.GenericCacheCodecFactory( )
    for ItemKey in Kargs.keys():
      setattr( self.file, ItemKey , Kargs[ItemKey] )


class ObjectCodeAnalysisImplement( object ):
  ObjectCached = GenericCache()

  class ObjectCodeAnalysisFactory( object ):


    class AnalysisFactoryELF( object ):


    class AnalysisFactoryPE( object )
