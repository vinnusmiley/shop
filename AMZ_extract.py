import re
wsize=200
wsize=str(wsize)
hsize=200
hsize=str(hsize)


'''
if element00:
    asin = item.attrs['data-asin']
    # print 'ASIN : ',asin
else:
    asin = "No ASIN"
'''
def fprod_asin(item):
    try:
        element00 = item.find("h2", "s-access-title")
        prod_asin = item.attrs['data-asin']

        #print prod_asin
    except:
        prod_asin = 'No ASIN Info'
    return prod_asin

def fprod_url(item):
    try:
        element00 = item.find("a", "a-link-normal a-text-normal")
        fprod_url = element00.attrs['href']
        #print fprod_url
    except:
        fprod_url = 'No Url Info'
    return fprod_url

def fprod_title(item):
    try:
        element00 = item.find("h2", "s-access-title")
        prod_title = element00.attrs['data-attribute']
        #print prod_Title
    except:
         prod_title = 'No Title Info'
    return prod_title

def fprod_price(item):
    try:
        element01 = item.find('span', attrs={'class': 'a-size-base a-color-price s-price a-text-bold'})
        #print element01
        element01 = str(element01)
        prod_price = re.match(r'.*?n>(.*?)</', element01).group(1)
        #print rtng_avg
    except:
        prod_price = 'No Prod Price Info'
    return prod_price


def fprod_imgUrl(item):
    try:
        element01 = item.find('a', attrs={'class': 'a-link-normal a-text-normal'})
        element02 = element01.find_next('img')
        prod_imgUrl = element02.attrs['src']

        #print prod_imgUrl

    except:
        prod_imgUrl = 'No Img Url'
    return prod_imgUrl

'''
img_sub_dict={'{@width}':wsize,'{@height}':hsize,'?q={@quality}':''}



def fprod_stock(items):
    try:
        prod_stock = items['productInfo']['value']['availability']['displayState']
        #print prod_stock
    except:
        prod_stock = 'No Stock Info'
    return prod_stock


def frtng_avg(items):
    try:
        rtng_avg = items['productInfo']['value']['rating']['average']
        #print rtng_avg
    except:
        rtng_avg = 'No Rating_Avg Info'
    return rtng_avg




def fdelvry_price(items):
    try:
        delvry_price = items['productInfo']['value']['pricing']['deliveryCharge']['decimalValue']
        #print delvry_price
    except:
        delvry_price = 'No Delvry Price Info'
    return delvry_price


def ffinal_price(items):
    pp = fprod_price(items)
    dp = fdelvry_price(items)
    try:
        final_price = pp + dp
        #print delvry_price
    except:
        final_price = 'No Final Price Info'
    return final_price

def fprod_img(items):
    img_list = []
    try:
        img_iter = items['productInfo']['value']['media']['images']
        for img in img_iter:
            # printimg['url']
            img_list.append(reduce(lambda a, kv: a.replace(*kv), img_sub_dict.iteritems(), img['url']))
        #print img_list
    except:
        img_list = 'No Images are retrieved'
    return img_list[0]

def fprod_warnty(items):
    try:
        prod_warnty= items['productInfo']['value']['warrantySummary']
        #print prod_warnty
    except:
        prod_warnty = 'No Prod Warranty Info'
    return prod_warnty

'''