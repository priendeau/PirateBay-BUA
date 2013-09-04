# Copyright (c) Alexander Borgerth 2010, Copyright (c) 2005-2010 re-edited by Maxiste Deams, Patrick Riendeau, Rheault Etccy for 
# Upcoming Security audit in Canada.
# See LICENSE for details.

from urllib2                  import Request, urlopen
from urllib                   import urlencode
from os                       import path, getcwd
from random                   import choice
from fake_useragent           import UserAgent
from piratebaybua.exceptions  import UserAgentExceptionError


class RequestObject( object ):

  BrowserName         = None
  BrowserCall         = None
  BrowserValue        = None 

  StrAgentdeTokenize  = None
  VerMin              = None
  VerMax              = None
  VerKeyZip           = None
  VerKeyZipFormat     = None
  VerRangeKeyName     = None
  VerAgentKeyName     = None
    
  user_agents = UserAgent()

  AgentSpecification={
    'name':{
      'ie':{
        'on_plateform':[ 'unix', 'windows','mac' ] },
      'msie':{
        'on_plateform':[ 'unix', 'windows','mac' ] },
      'google':{
        'on_plateform':[ 'unix', 'windows','mac' ] },
      'chrome':{
        'on_plateform':[ 'unix', 'windows','mac' ] },
      'googlechrome':{
        'on_plateform':[ 'unix', 'windows','mac' ] },
      'ff':{
        'on_plateform':[ 'unix', 'windows','mac' ] },
      'firefox':{
        'on_plateform':[ 'unix', 'windows','mac' ] },
      'safari':{
        'on_plateform':[ 'windows','mac' ] }
      },
    'plateform':{
      'unix':[ 'Linux', 'Unix', 'Bsd', 'FreeBsd', 'NetBsd',  'Sco/Unix',
               'OSX',  'Solaris', 'AIX', 'IS', 'Irix' ],
      'windows':[],
      'mac':[]
      },
    'langchart':{
      'en':[ 'en-US', 'en-CA', 'en-US' ],
      'fr':[ 'en-CA', 'fr-CA', 'fr-FR' ],
      'fr_ca':[ 'en-CA', 'fr-CA', 'fr-FR' ],
      'en_uk':[ 'en-US' ],
      },
    'processor':[ 'i386','i486','i586','i686','x86_64',
                  'core2','prescott','pentium','armv1',
                  'armv2','armv3','armv5','armv7','armv9',
                  'mips', 'xscale','strongarm' ],
  }

  @property
  def GetBrowserType( self ):
    return self.AgentSpecification['name'].keys()

  def GetAgentName( self ):
    return self.BrowserName

  def SetAgentName( self, value ):
    if value not in self.GetBrowserType :
      raise UserAgentExceptionError( 'Requesting agent type {}'.format( value ) )
    else:
      self.BrowserName = value
      self.BrowserCall = getattr( self.user_agents , value )
      #self.Attr['agent']['value']   = getattr( self, self.Attr['agent']['call']  )
      #self.Attr['agent']['value']  = self.Attr['agent']['call']

  AgentName = property( GetAgentName , SetAgentName )

  @property 
  def GetAgent( self ):
    return self.Attr['agent']['value']
    

  def SetVerRange( self, Value ):
    print "Calling %s" % self.SetVerRange.__name__
    self.VerRangeKeyName, self.VerAgentKeyName = Value
    self.VerKeyZip=self.VersionRange[self.VerRangeKeyName]['zip']['value']
    self.VerKeyZipFormat=self.VersionRange[self.VerRangeKeyName]['zip']['format']
    self.VerMin=self.VersionRange[self.VerRangeKeyName]['min']
    self.VerMax=self.VersionRange[self.VerRangeKeyName]['max']
        
  def GetVerRange( self ):
    print """Calling {}\n,NumberSegment: {}\nformatting RangeKey :{},\nFormat Rule: {}""".format( self.GetVerRange.__name__, self.VerKeyZip , self.VerRangeKeyName, self.VerKeyZipFormat )
    IntCount=0
    for aInt in range( self.VerMin, self.VerMax ):
      ListSeg=list()
      NumberTuple=tuple(str(aInt))
      print "[ %d ] Number Sequence %s " % ( IntCount , NumberTuple )
      self.AgentItemRepl[self.VerAgentKeyName]['data'].append( self.VerKeyZipFormat % ( NumberTuple ) )
      print "List:[ %s ]" % ( self.AgentItemRepl[self.VerAgentKeyName]['data'] )
      IntCount+=1

  def SetParseRandomAgentKeyValue( self , AgentToken ):
    print "Calling %s" % self.SetParseRandomAgentKeyValue.__name__
    AgentString=AgentToken
    for ItemKey in self.AgentItemRepl.keys():
      DataChoice=choice( self.AgentItemRepl[ItemKey]['data'] )
      TagName=self.AgentItemRepl[ItemKey]['tag']
      AgentString=AgentString.replace( TagName, DataChoice )
    self.StrAgentdeTokenize=AgentString

  def GetParseRandomAgentKeyValue( self ):
    print "Calling %s" % self.GetParseRandomAgentKeyValue.__name__
    return self.StrAgentdeTokenize
    
  PropertyRange=property( GetVerRange, SetVerRange )
  AgentString=property( GetParseRandomAgentKeyValue , SetParseRandomAgentKeyValue )
        
  def __init__(self):
    pass
  
  def get_random_user_agent(self):
    """Create a random user-agent string."""
    pass
    
  def __call__(self, url, form_data=None, get_request=True):
    """Create an urllib2.Request object.
    
    A smart method, creates a GET request if get_request is True
    otherwise a POST. If form_data isn't None, pass it along with
    the request.
    """
    header = { 'User-agent': self.get_random_user_agent() }
    if form_data is not None:
      if get_request:
        return Request( url=url+urlencode(form_data), headers=header )
        return Request( url=url, data=urlencode(form_data), headers=header )
    return Request( url=url, headers=header )
    create_request_object = RequestObject()

def open_url_with_request(url, form_data=None, get_request=True):
    """Open an url with our own special request object."""
    return urlopen(create_request_object(url, form_data=form_data, get_request=get_request))

def download_file(url, location=getcwd()):
    """Download specified file from the web.
    
    If no location is given or '.' is given as location, use current dir as path.
    """
    remote_file = urlopen(url)
    local_file = path.join(location, path.split(url)[-1])
    with open(local_file, "w") as f:
      f.write(remote_file.read())

if __name__.__eq__( '__main__' ):
  Areq=RequestObject()
  Areq.get_random_user_agent()
