# Copyright (c) Alexander Borgerth 2010, Copyright (c) 2005-2010 re-edited by Maxiste Deams, Patrick Riendeau, Rheault Etccy for 
# Upcoming Security audit in Canada.
# See LICENSE for details.


from urlparse import urljoin
from PirateBayBUA import exceptions

_xpath_table = ".//div[@id='content']/div[@id='main-content']/table[@id='searchResult']"
_xpath_amount_of_pages = ".//div[@align='center']"

def find_table(doc):
    """Search for the result table on any page on piratebay.
    
    Raise TableNotFound to indicate error.
    """
    table = doc.xpath(_xpath_table)
    if len(table) <= 0:
        raise exceptions.TableNotFound("Unable to find table")
    return table[0]

def iterate_over_rows(table):
    """Iterate over the rows of the table.
    
    Raise InvalidTable to indicate error.
    """
    if table.tag != 'table':
        raise exceptions.InvalidTable("Invalid table")
    for row in table.iterchildren():
        if row.tag != 'tr':
            continue
        yield row

def process_row(row):
    """Process one row of data.
    
    Return the results in a dictionary, possible keys are:
        - name = Name of torrent.
        - torrent-info-url = (Full) url to the torrent info page.
        - torrent-url = (Full) url to the torrent file.
        - magnet-url = (Full) url to the magnet file.
        - user = (Full) url to the user page(shows all releases by the user).
        - seeders = Amount of people seeding the torrent.
        - leechers = Amount of people leeching the torrent.
    """
    data = {}
    columns = row.getchildren()[1:]
    if len(columns) != 3:
        raise exceptions.InvalidRow("Row isn't valid or it doesn't contain the columns it should.")
    for ele in columns[0].iterchildren():
        if ele.tag == 'div' and ele.get('class') == 'detName':
            a = ele.find('a')
            data["torrent-info-url"] = urljoin(ele.base, a.get('href'))
            data["name"] = a.text_content()
        elif ele.tag == 'a':
            if ele.get('title') == "Download this torrent":
                data["torrent-url"] = ele.get("href")
            elif ele.get('title') == "Download this torrent using magnet":
                data["magnet-url"] = ele.get("href")
        elif ele.tag == 'font':
            a = ele.find('a')
            if a is None:
                data['user'] = "Anonymous"
            else:
                data['user'] = urljoin(ele.base, a.get('href'))
    data['seeders'] = int(columns[1].text_content().strip())
    data['leechers'] = int(columns[2].text_content().strip())
    return data

def process_all_rows(table):
    """Process all rows.
    
    Generator that processes all the rows in a table.
    """
    for row in iterate_over_rows(table):
        yield process_row(row)

def find_number_of_pages(doc):
    """Find number of pages, and current page.
    
    Indexing starts at 0, so current_page-1 = the page number on the site.
    *Returns*
        A tuple with current_page, num_pages.
    """
    div = doc.xpath(_xpath_amount_of_pages)
    if len(div) != 1:
        raise exceptions.ElementNotFound("Div element not found on page")
    div = div[0]
    a_eles = div.findall('a')
    if len(a_eles) <= 0:
        raise exceptions.ElementNotFound("Incorrect div element found")
    a_eles = [a for a in a_eles if len(a.getchildren()) == 0]
    current_page = None
    num_pages = 1
    for index, element in enumerate(a_eles):
        if index+1 != int(element.text_content()):
            if current_page is None:
                current_page = int(element.text_content())-1
        num_pages += 1
    return (current_page, num_pages)
