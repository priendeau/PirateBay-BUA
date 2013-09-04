#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import piratebaybua
from piratebaybua import utils
from  piratebaybua.utils import RequestObject

if __name__ == '__main__':
  ### Example to setup a permanent Agent before doing PirateBayBUA request.
  print "Testing Agent thru piratebaybua.utils.RequestObject"
  Arq = RequestObject()
  print "All Browser supported: {}".format( Arq.GetBrowserType )
  print "Selecting firefox as default Agent-markup."
  Arq.AgentName = 'firefox'
  print "A New Agent was choosed: {}".format( Arq.BrowserCall )
  
