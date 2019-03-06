import webbrowser
import time
from pymsgbox import *
from shopper import shop
from HTML_Table_Generator import fimg_tag_gen, ftable_gen
from list_manager import flistSetter, flistVertConcat
# importing flask modules
from flask import Flask, render_template, request, redirect, url_for

chrome = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s'
# firefox = '"C:\Program Files\Mozilla Firefox\\firefox.exe" %s'
# initializing a variable of Flask
app = Flask(__name__)

gurl = 'https://www.google.com/search?q='


# decorating index function with the app.route with url as /login
@app.route('/')
def index():
    return render_template('iShopper.html')


@app.route('/results', methods=['POST'])
def success():
    if request.method == 'POST':
        sq = request.form['searchquery']
        sqs = '+'.join(sq.split()) + ' reviews'
        gurl = 'https://www.google.com/search?q='
        fgurl = gurl + sqs
        # alert(text='While we are in search, pls feel free to play the GAME', title='PLAY', button='OK')
        webbrowser.open_new_tab(fgurl)
        f1plist, a1plist = shop(sq)
        # print fplist
        fplist, aplist = fimg_tag_gen(f1plist, a1plist)
        if len(fplist) != len(aplist):
            elist, glist = flistSetter(fplist, aplist)
        if len(fplist) != len(aplist):
            ftlist = flistVertConcat(elist, glist)
        else:
            ftlist = flistVertConcat(fplist, aplist)
        ftable_gen(ftlist)
        print sq
        webbrowser.open_new_tab('\home\\vikki\Shopper\\templates\\res00.html')
        return render_template('iShopper.html')
    else:
        pass


if __name__ == "__main__":
    app.run(debug=True)

