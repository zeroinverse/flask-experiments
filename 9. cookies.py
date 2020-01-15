# coding: utf-8

from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index1.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']
   else:
      user = request.args.get('nm')
   
   resp = make_response(render_template('readCookie.html'))
   resp.set_cookie('userID', user)
   return resp



if __name__ == '__main__':
   app.run(debug = True)

'''
A Request object contains a cookie’s attribute. It is a dictionary object of 
all the cookie variables and their corresponding values, 
a client has transmitted. In addition to it, a cookie also 
stores its expiry time, path and domain name of the site.

In Flask, cookies are set on response object. 
Use make_response() function to get response object 
from return value of a view function. After that, use the set_cookie() 
function of response object to store a cookie.

Reading back a cookie is easy. 
The get() method of request.cookies attribute is used 
to read a cookie.
'''