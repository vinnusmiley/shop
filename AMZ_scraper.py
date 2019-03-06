import re
import multiprocessing
from time import sleep, time
from AMZ_navigator import burl, conn, pages, purl
from AMZ_extract import fprod_asin, fprod_title, fprod_price, fprod_imgUrl,fprod_url

def amain(sq):
    item_no = 0
    url_list = []
    AMZ_final_prod_list = []

    search_query = sq
    from AMZ_navigator import burl
    burl, burl_list = burl(search_query)
    resp_status, response = conn(burl)
    #print burl

    c_page, t_page, items_list = pages(response)

    #print c_page, ':', t_page
    #print len(items_list)
    #print type(c_page)
    #print type(t_page)
    for cp in range(int(c_page), t_page + 1):
        url_list = purl(cp, t_page, search_query, burl)

    #print url_list

    for urlx in url_list:
        c_page, t_page, items_list = pages(response)
        for items in items_list:
            if item_no <= 39:
                prod_ASIN = fprod_asin(items)
                #print prod_ASIN
                p1 = multiprocessing.Process(target=fprod_title, args=(items,))
                prod_Title = fprod_title(items)
        #        print prod_Title
                prod_Price = fprod_price(items)
                fprod_Price = fprod_price(items) + ' INR'
                #print 'AMZ prod price',prod_Price
                prod_ImgUrl = fprod_imgUrl(items)
                #print prod_ImgUrl
                prod_Url = fprod_url(items)
                #print prod_Url
                #print item_no
                final_prod = {'Title': prod_Title,'Price': prod_Price, 'Image_url': prod_ImgUrl, 'Prod_Url':prod_Url}
                if final_prod['Price'] == 'No Prod Price Info':
                    pass
                elif re.match('^http*.?',final_prod['Prod_Url']):
                    item_no+=1
                    final_list = [prod_Title, fprod_Price, prod_ImgUrl, prod_Url]
                    AMZ_final_prod_list.append(final_list)
        sleep(5)

    print len(AMZ_final_prod_list)
#    for prod in AMZ_final_prod_list:
#        print prod
    print AMZ_final_prod_list
    return AMZ_final_prod_list


sq = 'Timex Watch'
start = time()
amain(sq)
end = time()
print end - start