from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/blog/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

'''
@app.route('/<name>/', defaults={'ints': None, 'floats': None})
@app.route('/<name>/<int:ints>/', defaults={'floats': None})
@app.route("/<name>/<int:ints>/<float:floats>/")
def web(name, ints, floats):
    if ints!=None and floats!=None:
        return "Welcome Back: %s, Your Int: %d, Your Float: %f" % (name, ints, floats)
    elif ints!=None and floats==None:
        return "Welcome Back: %s, Your Int: %d" % (name, ints)
    return "Welcome Back: %s" % (name)
'''

if __name__ == '__main__':
   app.run()