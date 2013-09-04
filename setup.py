#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from distutils.core import setup

setup(name='piratebaybua',
      version='0.0.1r004-apha-chyctu',
      status='alpha',
      copyright='Copyright (c) Alexander Borgerth 2010, Copyright (c) 2005-2013 re-edited by Maxiste Deams, Patrick Riendeau, Rheault Etccy for Upcoming Security audit in Canada. See LICENSE for details.',
      author='P.Riendeau: Maxiste Deams <maxistedeams@gmail.com>, Rheault.Etccy <rheault.etccy@gmail.com>',
      author_email='maxistedeams@gmail.com',
      packages=['piratebaybua'],
      scripts=[],
      website='https://github.com/priendeau/PirateBay-BUA.git',
      url='https://pypi.python.org/pypi/PirateBayBUA',
      license=open('piratebaybua/license.txt').read(),
      description='PirateBay Json, Python Query analysis, implemented with Better User Agent and Aparatus in << Software Pirating Analysis >> know in detection of malware, virus and Evil intention.',
      long_description=open('piratebaybua/README.rst').read(),
      install_requires=[ "lxml >= 3.1", "fake_useragent == 0.0.4", ],
      )


