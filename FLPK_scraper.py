from time import  sleep
from FLPK_navigator import burl, conn, pages, purl
from FLPK_navigator import burl
from FLPK_extract import fprod_title, fprod_stock, frtng_avg, fprod_price, fdelvry_price, ffinal_price, fprod_img, \
     fprod_warnty, fprod_url, fprod_specs
import re
final_list = []

def fmain(sq):
    item_no = 0
    url_list = []
    FLPK_final_prod_list = []

    search_query = re.sub(r'%','%25',sq)

#    max_items = 10
#   item_no = 0
    from FLPK_navigator import burl
    burl , burl_list = burl(search_query)
    resp_status, response = conn(burl)
    c_page, t_page, basejson = pages(response)
    #print len(basejson)
    #print c_page, ':',t_page
    t_page = 1 # to limit the total pages to 1

    if c_page == t_page:
        url_list = burl_list
    else:
        for cp in range(c_page, t_page+1):
            url_list = purl(cp, t_page, search_query, burl)

    #for item in url_list:
    #    print item



    for urlx in url_list:
        c_page, t_page, basejson = pages(response)
        for j in range(len(basejson)):
            #print 'jfor',j
            if j>0 and j<len(basejson):
                    #print 'jif',j
                    #print'len_basejson[j]',len(basejson[j]['widget']['data']['products'])
                    try:
                        for items in basejson[j]['widget']['data']['products']:
                            if item_no <= 39:
                                prod_Title = fprod_title(items)
                                prod_Stock = fprod_stock(items)
                                rtng_Avg = frtng_avg(items)
                                prod_Price = fprod_price(items)
                                prod_Specs = fprod_specs(items)
                                #print prod_Specs
                                #print type(prod_Specs)
                                #print prod_Price
                                delvry_Price = fdelvry_price(items)
                                fin_Price = ffinal_price(items)
                                final_Price = re.match(r'([0-9]*).*?', fin_Price).group() + ' INR'
                                #print 'flpk final price',final_Price
                                img_url = fprod_img(items)
                                prod_Warnty = fprod_warnty(items)
                                prod_Url = fprod_url(items)
                                final_prod = {'Title':prod_Title,'Price':fin_Price,'Image_url': img_url,
                                              'Prod_Url':prod_Url}
                                if final_prod['Price'] == 'No Prod Price Info':
                                    pass
                                else:
                                    item_no+=1
                                    final_list = [prod_Title + "  " +prod_Specs + "  " + prod_Stock, final_Price, img_url, prod_Url]
                                    FLPK_final_prod_list.append(final_list)
                    except:
                         print 'Handling key error'
        sleep(5)


    #print 'flpkproduct'
    print len(FLPK_final_prod_list)
    #for prod in FLPK_final_prod_list:
    #    print prod
    print FLPK_final_prod_list
    return FLPK_final_prod_list

#sq = 'Lindt Excellence 70% Cocoa Dark Chocolate'

#fplist = fmain(str(sq))
#print len(fplist)