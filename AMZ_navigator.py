import json
import requests
import re
from bs4 import BeautifulSoup
burl_list = []
purl_list = []
total_page = 3

low2high = 'ref=sr_st_price-asc-rank?'
featured = 'ref=sr_st_relevancerank?'
high2low = 'ref=sr_st_price-desc-rank?'
avg_cust_review = 'ref=sr_st_review-rank?'
new_arrivals = 'ref=sr_st_date-desc-rank?'
new_popular = 'ref=sr_st_popularity-rank?'


headers={'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10_10_1)AppleWebKit/537.36(KHTML,likeGecko)Chrome/39.0.2171.95Safari/537.36'}



def burl(sq):
    b00 = 'https://www.amazon.in/s/'
    pref = featured
    b01 = 'keywords='
    b11 = re.sub(' ', '+', sq)
    burl = b00 + pref + b01 + b11
    burl_list.append(burl)
    return burl, burl_list

def conn(url):
    try:
        response = requests.get(url, headers=headers)
        resp_status = re.match(r'(.*?)\[(.*?)\]>', str(response)).group(2)
        if int(resp_status) == 200:
            return 'Connection OK code:200', response
        else:
            return resp_status
    except:
        print "Check Internet Connection"

        # cp =
        # tp = soup.find('span',"pagnRA")

def pages(response, tp=3):
    # type: (object, object) -> object
    data = response.content
    soup = BeautifulSoup(data, "lxml")
    allitems_list = soup.findAll("li", "s-result-item")
    try:
        current_page = soup.find('span',"pagnCur").text
    except:
        current_page = 1
        print 'Single Page'
    if type(current_page) is int:
        total_page = 1
    else:
        total_page = tp
    return current_page, total_page, allitems_list

''''
    try:
        tp = soup.find('span',"pagnRA")
        tpch = tp.findchild('a')
        tphref = tp.attrs['href']
        print 'tphref',tphref
    except:
        total_page = 1
        print 'tp',"Single Page"
    return current_page, total_page, allitems_list
'''


def purl(cp, tp, sq, burl):
    purl_list.append(burl)
    cp = cp + 1
    np = str(cp)
    #print np
    if cp <= tp:
        p00 = burl
        p11 = '&page='
        pno = np
        purl = p00 + p11 + pno
        purl_list.append(purl)
        #print purl
    return purl_list

