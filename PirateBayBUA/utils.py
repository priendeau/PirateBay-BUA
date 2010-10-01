# Copyright (c) Alexander Borgerth 2010, Copyright (c) 2005-2010 re-edited by Maxiste Deams, Patrick Riendeau, Rheault Etccy for 
# Upcoming Security audit in Canada.
# See LICENSE for details.

from urllib2 import Request, urlopen
from urllib import urlencode
from os import path, getcwd
from random import choice

class RequestObject( object ):

    ### Comment: I see, some similarity between html5lib, or either come from a tiny update from 
    ### 199.182.x.x or 199.183.x.x... I guess it may become futur work in data/category sharing, rather
    ### than becoming progagnostic-downloadmatic of any warez in the backyard... 

    user_agents = (
        'Mozilla/{mozver} (Windows; U; Windows NT 5.1; {langchart}; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; {langchart})' ,
        'Mozilla/{mozver} (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)' ,
        'Mozilla/{mozver} (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)' ,
        'Mozilla/{mozver} (X11; {unix}; {proc}; {langcountry}; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12' ,
        'Lynx/{lynxver} libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9' )

    VersionRange={ 'mozilla':{ 'min':(10) ,
                               'max':(55),
                               'zip':{ 'value':(2),
                                       'format':('%s.%s') } },
                   'msie':{ 'min':(20),
                            'max':(84),
                            'zip':{ 'value':(2),
                                    'format':('%s.%s') } },
                   'lynx':{ 'min':(1000),
                            'max':(4000),
                            'zip':{ 'value':(4),
                                    'format':('%s.%s.%srel.%s') } }
                   }

    AgentItemRepl={ 'unix':{
                        'data':[ 'Linux',   'Unix',     'Bsd',  'FreeBsd',
                                 'NetBsd',  'Sco/Unix', 'OSX',  'Solaris',
                                 'AIX',     'IS',       'Irix'           ],
                        'tag':( '{unix}' ) } ,
                    'langchart':{
                        'data':[ 'en', 'fr', 'fr_ca', 'en_uk', 'en_en', 'it' ],
                        'tag':( '{langchart}' ) } ,
                    'langcountry':{
                        'data':[ 'en-US', 'en-CA', 'fr-CA', 'fr-FR', 'en-US' ],
                        'tag':( '{langcountry}' ) },
                    'proc':{
                        'data':[ 'i386','i486','i586','i686',
                                 'x86_64','core2','prescott','pentium',
                                 'armv1','armv2','armv3','armv5','armv7',
                                 'armv9', 'mips', 'xscale', 'strongarm' ],
                        'tag':('{proc}') },
                    'mozillaVer':{
                        'data':[],
                        'tag':'{mozver}' },
                    'msieVer':{
                        'data':[],
                        'tag':'{msiever}' },
                    'lynxVer':{
                        'data':[],
                        'tag':'{lynxver}' }
                    }

    StrAgentdeTokenize=None
    VerMin=None
    VerMax=None
    VerKeyZip=None
    VerKeyZipFormat=None
    VerRangeKeyName=None
    VerAgentKeyName=None

    def SetVerRange( self, Value ):
        print "Calling %s" % self.SetVerRange.__name__
        self.VerRangeKeyName, self.VerAgentKeyName = Value
        self.VerKeyZip=self.VersionRange[self.VerRangeKeyName]['zip']['value']
        self.VerKeyZipFormat=self.VersionRange[self.VerRangeKeyName]['zip']['format']
        self.VerMin=self.VersionRange[self.VerRangeKeyName]['min']
        self.VerMax=self.VersionRange[self.VerRangeKeyName]['max']
        
    def GetVerRange( self ):
        print """Calling %s,
    NumberSegment: %d
    formatting RangeKey :%s,
    Format Rule: %s""" % ( self.GetVerRange.__name__, self.VerKeyZip , self.VerRangeKeyName, self.VerKeyZipFormat )
        IntCount=0
        for aInt in range( self.VerMin, self.VerMax ):
            ListSeg=list()
            NumberTuple=tuple(str(aInt))
            print "[ %d ] Number Sequence %s " % ( IntCount , NumberTuple )
##            for IntZipNum in range(0,self.VerKeyZip):
##                print "[ %d ] Number Sequence %s " % ( IntZipNum , NumberTuple )
##                #zip( str( aInt ))[ IntZipNum ][ 0 ]
##                ListSeg.append( NumberTuple[IntZipNum] )
##                print "Resulting Key: %s" % ( ListSeg )
##            print "ListSeg Format %s" % ( ListSeg )
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
        self.last_user_agent = None
        self.PropertyRange='mozilla' , 'mozillaVer'
        self.PropertyRange
##        self.PropertyRange='msie', 'msieVer'
##        self.PropertyRange
##        self.PropertyRange='lynx', 'lynxVer'
##        self.PropertyRange
    
    def get_random_user_agent(self):
        """Create a random user-agent string."""
        
        agent = None
        while True:
            agent = choice(self.user_agents)
            if agent == self.last_user_agent:
                continue
            self.last_user_agent = agent
            break
        self.AgentString = agent
        return self.AgentString
    
    def __call__(self, url, form_data=None, get_request=True):
        """Create an urllib2.Request object.
        
        A smart method, creates a GET request if get_request is True
        otherwise a POST. If form_data isn't None, pass it along with
        the request.
        """
        header = { 'User-agent': self.get_random_user_agent() }
        if form_data is not None:
            if get_request:
                return Request( url=url+urlencode(form_data),
                                headers=header )
            return Request( url=url,
                            data=urlencode(form_data),
                            headers=header )
        return Request( url=url,
                        headers=header )
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
