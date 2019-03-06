
ntav = 'End of Search'
from itertools import chain

def flistSetter(fplist, aplist):
    slist = list(chain(*[fplist if len(fplist) < len(aplist) else aplist]))
    slen = len(slist)

    #print 'slen',slen
    #print 'slist'
    #print '============================================================================='
    #for item in slist:
        #print item
    #print '==================================================='

    glist = list(chain(*[fplist if len(fplist) > len(aplist) else aplist]))
    glen = len(glist)
    #print 'glen',glen
    #print 'glist'
    #print '============================================================================='
    #print glist


    if slen != glen:
        for i in range(len(glist) - len(slist)):
            slist.append([ntav, ntav, ntav])
    print len(slist),':After ntav:',len(glist)
    return slist, glist

def flistVertConcat(elist, glist):
    tlist = []
    if len(elist) == len(glist):
        for i in range(0, len(elist)):
            tlist.append(list(chain(elist[i], glist[i])))
        return tlist
    else:
        print 'len of elist{0} is not equal to glist{1}'.format(len(elist), len(glist))