#  coding: utf-8
# adding javascript and CSS support

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)

'''
in the template file, 
A special endpoint ‘static’ is used to generate URL for static files.

The HTML script of ./templates/index.html

<html>
   <head>
      <script type = "text/javascript" 
         src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
   </head>
   
   <body>
      <input type = "button" onclick = "sayHello()" value = "Say Hello" />
   </body>
</html>


a javascript function defined in hello.js is called 
on OnClick event of HTML button in index.html, 
which is rendered on ‘/’ URL of the Flask application.


./static/hello.js contains sayHello() function.

function sayHello() {
   alert("Hello World")
}
'''