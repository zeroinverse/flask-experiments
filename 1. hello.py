# coding: utf-8

from flask import Flask
app = Flask(__name__)

# app.route(rule, options)
'''
    The rule parameter represents URL binding with the function.
    The options is a list of parameters to be forwarded to the underlying Rule object.
'''

@app.route('/')
def hello_world():
   s = "hello world"
   return s


'''
It is possible to build a URL dynamically, 
by adding variable parts to the rule parameter. 
This variable part is marked as <variable-name>. 
It is passed as a keyword argument to the function 
with which the rule is associated.
'''
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
# hence, http://localhost:5000/hello/zeroinverse will provide "hello zeroinverse"


if __name__ == '__main__':
   app.run(debug = True)

'''
app.run(host, port, debug, options)
host
Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally

port
Defaults to 5000

debug
Defaults to false. If set to true, provides a debug information

options
To be forwarded to underlying Werkzeug server.
'''
