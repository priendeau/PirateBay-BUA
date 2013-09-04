# Copyright (c) Alexander Borgerth 2010, Copyright (c) 2005-2013 re-edited by Maxiste Deams, Patrick Riendeau, Rheault Etccy for 
# Upcoming Security audit in Canada.
# See LICENSE for details.

import operator
from lxml import html
from piratebaybua.utils import open_url_with_request
from piratebaybua.parser import find_table, process_all_rows, find_number_of_pages
from piratebaybua import exceptions

url_addr=[ 'thepiratebay.org', 'thepiratebay.sx' ]

search_page_url = "http://{}/s/?"
user_page_url = "http://{}/user/%s"

order = {
    'name': 1,
    'uploaded': 3,
    'size': 5,
    'uploader': 11,
    'seeders': 7,
    'leechers': 9
}

def search_main(term, category=0, page=0, order_by=order["seeders"]):
    """Search the main piratebay website for the term 'term'.
    
    A Page object is given in return.
    """
    form_data = { "q": term, "category": category,
                "page": page, "orderby": order_by }
    ### 
    ### Detect which version of piratebay is working 
    ### 
    ###
    UrlRespond = [ ]
    for URI in url_addr:
      URequest = Request( url=search_page_url.format( URI ) )
      UConnect = urllib2.urlopen( URequest )
      UrlRespond.append( [URI, UConnect.get_code() ] )
    IsUriAccess = 0
    UriName = None 
    for Uri, UCode in UrlRespond:
      if UCode == 200 :
        UriName = Uri
        IsUriAccess = 1
    if IsUriAccess == 0 :
      raise URIExeption( "All URI in url_addr not returning HTTP_CODE: 200" )
    
    url = open_url_with_request( search_page_url.format( UriName ), form_data=form_data)
    doc = html.parse(url).getroot()
    return Page(doc, term, category, page, order_by)

class Page(object):
    """The Page class.
    
    A Page object is returned by each search on the piratebay website,
    it lets you easily handle all the data. Each item returned by either
    all() or search() is a dictionary, with the possible keys being:
        - name = Name of torrent.
        - torrent-info-url = (Full) url to the torrent info page.
        - torrent-url = (Full) url to the torrent file.
        - magnet-url = (Full) url to the magnet file.
        - user = (Full) url to the user page(shows all releases by the user).
        - seeders = Amount of people seeding the torrent.
        - leechers = Amount of people leeching the torrent.
    
    So to print all torrent-urls followed by the uploader you could do this:
    page = piratebay.search_main("some search term")
    for row in page.all():
        print "%s => %s" % (row["torrent-url"], row["user"])
    """
    def __init__(self, document, term, category, page, order_by):
        self.document = document
        self.search_term = term
        self.category = category
        self.current_page = page
        self.order_by = order_by
        self.list_of_rows = None
        self.max_page = 0
        self._process_document()
    
    def search(self, key, value, comparator=None, order_by=None, reversed=True):
        """Searched through each record in the dictionary, and yields the result(s).
        
        You can search for any 'value' in the dictionary with 'key', using
        operator.eq(==) by doing: page.search("user", "...") as simple as that.
        Or you could use your own comparator method, as an example:
        def compare_user(dict_value, your_search_term):
            user = dict_value.encode("utf-8").split("/")
            if len(user) >= 2:
                user = user[-2]
            if user == your_search_term:
                return True
            return False
        page.search("user", "some_user", comparator=compare_user, order_by="seeders")
        would yield all result(s), and order them by seeders, having highest value first.
        """
        if order_by is not None:
            self.list_of_rows = sorted(self.list_of_rows, key=operator.itemgetter(order_by), reverse=reversed)
        if comparator is None:
            comparator = operator.eq
        for row in self.list_of_rows:
            if comparator(row[key], value):
                yield row
    
    def all(self, order_by=None, reversed=True):
        """A generator that yields all torrents in turn."""
        if order_by is not None:
            self.list_of_rows = sorted(self.list_of_rows, key=operator.itemgetter(order_by), reverse=reversed)
        for row in self.list_of_rows:
            yield row
    
    def _process_document(self):
        """Updates the current document. INTERNAL USE ONLY!"""
        try:
            self.current_page, self.max_page = find_number_of_pages(self.document)
        except exceptions.ElementNotFound as err:
            self.current_page, self.max_page = 0,0
        self.list_of_rows = []
        table = find_table(self.document)
        for row in process_all_rows(table):
            self.list_of_rows.append(row)
    
    def update(self):
        """Update the current page.
        
        Updates the current page object, by getting new data from
        thepiratebay website. Re-using your old search criteria.
        """
        search_main(self.term, self.category, self.page, self.orderby)
        self._process_document()

    def get_current_page(self):
        """Return the current page you're visiting."""
        return self.current_page
    
    def get_number_of_pages(self):
        """Return maximum number of pages available for your search."""
        return self.max_page
