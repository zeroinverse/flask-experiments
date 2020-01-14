from flask import Flask, render_template
app = Flask(__name__)


'''
you can do something like this:
@app.route('/')
def index():
   return '<html><body><h1>Hello World</h1></body></html>'

# However, generating HTML content from Python code is cumbersome, 
# especially when variable data and Python language elements 
# like conditionals or loops need to be put. 
# This would require frequent escaping from HTML.

'''


'''
Alternatively, We can take advantage of Jinja2 template engine, on which Flask is based. 
Instead of returning hardcode HTML from the function, 
a HTML file can be rendered by the render_template() function.
'''

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)
# hello.html should be contained in ./templates/ directory
'''
OUR hello.html:

<!doctype html>
<html>
   <body>
   
      <h1>Hello {{ name }}!</h1>
      
   </body>
</html>
'''

if __name__ == '__main__':
   app.run(debug = True)    



'''
# More examples:

<!doctype html>
<html>
   <body>
      {% if marks>50 %}
         <h1> Your result is pass!</h1>
      {% else %}
         <h1>Your result is fail</h1>
      {% endif %}
   </body>
</html>

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)



<!doctype html>
<html>
   <body>
      <table border = 1>
         {% for key, value in result.iteritems() %}
            <tr>
               <th> {{ key }} </th>
               <td> {{ value }} </td>
            </tr>
         {% endfor %}
      </table>
   </body>
</html>

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
'''