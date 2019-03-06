import os

imga = '<img src="'
imgb = '">'

th_list = ['Product@Flipkart', 'Price', 'Image', 'Product@Amazon', 'Price', 'Image']

def fimg_tag_gen(fplist, aplist):
    #Image tag Generator for Flipkart output
    for i in range(0,len(fplist)):
        fplist[i][2] = imga + fplist[i][2] + imgb
        fplist[i][0] = '<a href="'+fplist[i][3] + '" target="_blank">' + fplist[i][0]+'</a>'
        del fplist[i][-1]

    #Image tag Generator for Amazon output
    for i in range(0,len(aplist)):
        aplist[i][2] = imga + aplist[i][2] + imgb
        aplist[i][0] = '<a href="' + aplist[i][3] + '" target="_blank">' + aplist[i][0] + '</a>'
        del aplist[i][-1]
    return fplist, aplist

def ftable_gen(td_list):
    #print '===65465465465465465465465465465465465464645654654654654654==========='
    #print len(td_list)
    #for item in td_list:
        #print item[0],item[3]
    os.remove('templates/res00.html')
    fd = open('templates/htmlstart.txt', 'r')
    html_start = fd.read()
    #print html_start
    fd = open('templates/res00.html', 'a')
    fd.write(html_start)
    #print "<table>"
    #print "<tr>"
    fd.write("<table>")
    fd.write("<tr>")
    for j in range(0, len(th_list)):
        fd.write('<th>' + th_list[j].encode('utf-8') + '</th>')
        #print '<th>' + th_list[j].encode('utf-8') + '</th>'
    fd.write('</tr>')
    #print '</tr>'
    for items in td_list:
        fd.write('<tr>')
        #print '<tr>'
        for j in range(0, len(items)):
            fd.write('<td>' + items[j].encode('utf-8') + '</td>')
            #print '<td>' + items[j].encode('utf-8') + '</td>'
    fd.write('</tr>')
    fd.write('</table>')
    #print "</tr>"
    #print "</table>"
