# coding: utf-8

from flask import Flask, redirect, url_for
app = Flask(__name__)

'''
The url_for() function is very useful for 
dynamically building a URL for a specific function.
'''

'''
The functions below accept the name of a function as first argument, 
and one or more keyword arguments, 
each corresponding to the variable part of URL.
'''
@app.route('/admin/')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>/')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

# ----------- magic happens here -----------
@app.route('/user/<name>/')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

'''
    function user(name) accepts a value to its argument from the URL
    The User() function checks if an argument received matches ‘admin’ or not. 
    If it matches, the application is redirected to the hello_admin() function using url_for(), 
    otherwise to the hello_guest() function passing the received argument as guest parameter to it.
'''

if __name__ == '__main__':
   app.run(debug = True)