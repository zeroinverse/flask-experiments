from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from flask import Flask, request
from datetime import datetime
import sqlite3
import enum

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The temp task identifier'),
    'task': fields.String(required=True, description='The temp task details'),
    'due': fields.Date(required=True, description='Due date of the task'),
    'status': fields.String(required=True, description='status of the task', enum = ['not_statrted', 'in_progress', 'finished'])
})

m_todo = api.model('m_todo', {
    'id': fields.Integer(readonly=False, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details'),
    'due': fields.Date(required=True, description='Due date of the task'),
    'status': fields.String(description='status of the task', enum = ['not_statrted', 'in_progress', 'finished']),
})



DB_PATH = './todo.db'   # Update this path accordingly
'''
CREATE TABLE "items" (
    "id" TEXT NOT NULL,
    "task" TEXT NOT NULL,
    "due" TEXT,
    "status" TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE "counter" (
    "counter_id" TEXT NOT NULL,
    "counter" TEXT NOT NULL,
    PRIMARY KEY("counter_id")
);
'''

def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)

        # Once a connection has been established, we use the cursor
        # object to execute queries
        c = conn.cursor()

        # Keep the initial status as Not Started
        print( 'INSERTING ITEM: ', item['id'], item['task'], item['due'], item['status'])
        c.execute('insert into items(id, task, due, status) values(?,?,?,?)', (item['id'], item['task'], item['due'], item['status']))

        # We commit to save the change
        conn.commit()
        r = {"id": item[id], "task": item['task'], "due_by": item['due'], "status": item['status']}
        print('ADDED', r)
        return r
    
    except Exception as e:
        print('Error: ', e)
        return None

def add_counter(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('insert into counter(counter_id, counter) values(?,?)', ('1', str(item)))
        conn.commit()
        r = {"id": item[id], "task": item['task']}
        print('added', r)
        return r

    except Exception as e:
        print('Error: ', e)
        return None

def get_all_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        r = []
        print(rows)
        for i in range(len(rows)):
            m_todo = {'task': str(rows[i][1]), 'due': str(rows[i][2]), 'status':str(rows[i][3])}
            m_todo['id'] = str(rows[i][0])
            r.append(m_todo)
        return r

    except Exception as e:
        print('Error: ', e)

def get_all_items_due(due):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from items where due = '%s'" % due)
        rows = c.fetchall()
        r = []
        print(rows)
        for i in range(len(rows)):
            m_todo = {'task': str(rows[i][1]), 'due': str(rows[i][2]), 'status':str(rows[i][3])}
            m_todo['id'] = str(rows[i][0])
            r.append(m_todo)
        return r

    except Exception as e:
        print('Error: ', e)

def get_overdue_items(due):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from items where due < '%s' and status != 'finished'" % due)
        rows = c.fetchall()
        r = []
        print(rows)
        for i in range(len(rows)):
            m_todo = {'task': str(rows[i][1]), 'due': str(rows[i][2]), 'status':str(rows[i][3])}
            m_todo['id'] = str(rows[i][0])
            r.append(m_todo)
        return r

    except Exception as e:
        print('Error: ', e)

def get_finished_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from items where status = 'finished'")
        rows = c.fetchall()
        r = []
        print(rows)
        for i in range(len(rows)):
            m_todo = {'task': str(rows[i][1]), 'due': str(rows[i][2]), 'status':str(rows[i][3])}
            m_todo['id'] = str(rows[i][0])
            r.append(m_todo)
        return r

    except Exception as e:
        print('Error: ', e)


def get_item_task(item_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select task from items where id='%s'" % item_id)
        status = c.fetchone()[0]
        return status
    
    except Exception as e:
        print('Error: ', e)

def get_item(item_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from items where id='%s'" % item_id)
        status = c.fetchone()[0]
        return status
    
    except Exception as e:
        print('Error: ', e)

def get_item_due(item_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select due from items where id='%s'" % item_id)
        status = c.fetchone()[0]
        return status
    
    except Exception as e:
        print('Error: ', e)

def get_item_status(item_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select status from items where id='%s'" % item_id)
        status = c.fetchone()[0]
        return status
    
    except Exception as e:
        print('Error: ', e)

def get_counter():
    item_id = '1'
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select counter from counter where counter_id='%s'" % item_id)
        status = c.fetchone()[0]
        return status
    
    except Exception as e:
        print('Error: ', e)

def update_status(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('update items set (task, due,status)=(?,?,?) where id=?', (item['task'], item['due'], item['status'], item['id']))
        conn.commit()
        print('Suceess, updated %s' % item['id'])
        return item
    
    except Exception as e:
        print('Error: ', e)
        return None

def update_counter(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('update counter set counter=? where counter_id=?', (item, '1'))
        conn.commit()
        print('Suceess, updated %s' % str(item))
    
    except Exception as e:
        print('counter Error: ', e)

def delete_item(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from items where id=?', (item['id'],))
        conn.commit()
        print('deleted %s' % item['id'])
        return item
    
    except Exception as e:
        print('Error: ', e)
        return None


class TodoDAO(object):
    def __init__(self):
        
        self.counter = 0
        # initialize counter
        item = get_counter()
        print('RECIEVED COUNTER', item)
        if item is not None:
            # fetch the counter from the database
            item = int(item) + 1
            self.counter = int(item)
            print('CURRENT COUNTER', self.counter)
        else:
            # counter not already present
            r = add_counter(self.counter)
            if r is not None:
                print('COUNTER INITIALIZED')

    def get(self, id):
        # get todo from the database
        item_task = get_item_task(id)
        item_due = get_item_due(id)
        item_status = get_item_status(id)
        if item_task is not None:
            m_todo = {'task':item_task, 'due':item_due, 'status':item_status}
            m_todo['id'] = id
            return m_todo
        # if we reach here, some error occured
        api.abort(404, "Todo {} doesn't exist".format(id))

    def get_all(self):
        return get_all_items()
    
    def get_overdue(self):
        return get_overdue_items(datetime.today().strftime('%Y-%m-%d'))
    
    def get_finished(self):
        return get_finished_items()

    def get_all_due(self):
        due = request.args.get('due_date')
        return get_all_items_due(due)


    def create(self, data):
        m_todo = data
        m_todo['id'] = self.counter
        r = add_to_list(m_todo)
        self.counter += 1
        update_counter(self.counter)
        return m_todo

    def update(self, id, data):
        item_task = get_item_task(id)
        item_due = get_item_due(id)
        item_status = get_item_status(id)
        if item_task is not None:
            m_todo = data
            if m_todo['due'] == " ":
                m_todo['due'] = item_due
            if m_todo['status'] == " ":
                m_todo['status'] = item_status
            if m_todo['task'] == " ":
                m_todo['task'] = item_task
            m_todo['id'] = id
            m_todo = update_status(m_todo)
        return m_todo
    
    def update_status(self, id, stat):
        try:
            m_todo = {'task': get_item_task(id), 'due': get_item_due(id), 'status': stat}
            m_todo['id'] = id
            m_todo = update_status(m_todo)
            return m_todo
        except:
            return None

    def delete(self, id):
        m_todo = self.get(id)
        r = delete_item(m_todo)


DAO = TodoDAO()


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return DAO.get_all()

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201

@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)

@ns.route('/<int:id>/<string:stat>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
@ns.param('stat', 'Updated status of the task')
class TodoStatus(Resource):
    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    def put(self, id, stat):
        '''Update a task status given its identifier'''
        return DAO.update_status(id, stat)


# /due?due_date=yyyy-mm-dd
@ns.route('/due', endpoint='due')
@ns.response(404, 'No todo found for specified date')
@ns.param('due', 'due date')
@ns.doc(params={ 'due_date': '<due>' })
class TodoDue(Resource):
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks due on given date'''
        return DAO.get_all_due()

# "GET /overdue"
@ns.route('/overdue/')
@ns.response(404, 'Error - see debugger logs')
class Overdue(Resource):
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all overdue tasks'''
        return DAO.get_overdue()

# "GET /finished"
@ns.route('/finished/')
@ns.response(404, 'Error - see debugger logs')
class Finished(Resource):
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all finished tasks'''
        return DAO.get_finished()


if __name__ == '__main__':
    app.run(debug=True)

# MILESTONE: completed task 4