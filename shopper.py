from AMZ_scraper import amain
from FLPK_scraper import fmain

'''
app = Flask("__name_")

@app.route('/')
def search():
    rendered = render_template('iShopper.html')
    return rendered,


@app.route("/results", methods=['POST'])
def results():
    try:
        rendered = render_template('res00.html')
    except:
        msg = "Looks like, The Network is slow"
    return rendered

if __name__ == '__main__':
    app.run()
'''

def shop(sq):

    search_query = sq
    try:
        fprod_list = fmain(search_query)
    except:
        print "Check output of FLPK_scraper"

    try:
        aprod_list = amain(search_query)
    except:
        print "Check output of AMZ_scraper"

    print 'fprod_list'
    for item in fprod_list:
        print item
    f = len(fprod_list)
    print '==============================================='
    print 'aprod_list'
    for item in aprod_list:
        print item
    a = len(aprod_list)
    print 'flen', f
    print 'alen', a
    return fprod_list, aprod_list

#sq = 'Timex Watch'
#fplist, aplist = shop(sq)
text = 'Timex Watches'

#print '30303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303'

#fplist, aplist = fsort(fplist,aplist) #Fuzzy Sort

#fsplist = fplist
#asplist = aplist



#print '30303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303'
#fplist, aplist = fimg_tag_gen(fplist, aplist) #coverting img url to html img tag


#if len(fplist)!=len(aplist):
#    elist, glist = flistSetter(fplist, aplist)


#print '30303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303'
#if len(fplist)!=len(aplist):
#    ftlist = flistVertConcat(elist,glist)
#else:
#    ftlist = flistVertConcat(fplist, aplist)


#print 'ftlist'

#print len(ftlist)

#print ftlist

#ftable_gen(ftlist)