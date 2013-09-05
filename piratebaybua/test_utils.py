#!/usr/bin/env python
# -*- coding: utf-8 -*-

import piratebaybua
from  piratebaybua        import utils
from  piratebaybua.utils  import RequestObject

if __name__ == '__main__':
  ### Example to setup a permanent Agent before doing PirateBayBUA request.
  print "\nTesting Agent thru piratebaybua.utils.RequestObject"
  Arq = RequestObject()
  print "All Browser supported: {}".format( Arq.GetBrowserType )
  print "Selecting firefox as default Agent-markup."
  Arq.BrowserName = 'firefox'
  print "A New Agent was choosed: {}".format( Arq.BrowserAgent )
  
  print "\nTesting RequestObject, get_random_user_agent()"
  Arq1 = RequestObject()
  print "Random User Agent: {}".format( Arq1.get_random_user_agent() ) 
  
