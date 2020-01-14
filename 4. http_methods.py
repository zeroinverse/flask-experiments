#  coding: utf-8
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


'''
By default, the Flask route responds to the GET requests. 
However, this preference can be altered 
by providing methods argument to route() decorator.
'''

'''
Create an HTML form and use the POST method to send form data to a URL.
Save the following script as login.html

<html>
   <body>
      <form action = "http://localhost:5000/login/" method = "post">
         <p>Enter Name:</p>
         <p><input type = "text" name = "nm" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>
'''

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login/', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success', name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success', name = user))

if __name__ == '__main__':
   app.run(debug = True)

'''
Open login.html in the browser, enter name in the text field and click Submit.
Form data is POSTed to the URL in action clause of form tag.

http://localhost/login is mapped to the login() function. 
Since the server has received data by POST method, 
value of ‘nm’ parameter obtained from the form data is obtained by
        user = request.form['nm']

If data received on server is by the GET method, 
The value of ‘nm’ parameter is obtained by
        user = request.args.get(‘nm’)


note: args is dictionary object 
containing a list of pairs of form parameter and its corresponding value. 
'''

