import os
import uuid
import flask
import flask.views
from flask import render_template
from flask import request, make_response,send_from_directory
from werkzeug import secure_filename
from flask.ext.httpauth import HTTPBasicAuth
from flask import jsonify , json
app = flask.Flask(__name__,static_url_path='')
print app.static_url_path
from flask.ext.mysql import MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '17576cube'
app.config['MYSQL_DATABASE_DB'] = 'forum'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
cursor = mysql.connect().cursor()
@app.route('/')
@app.route('/login',methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form['email']
    password = request.form['pass']
    return authenticate(user,password)

def authenticate(username, password):

    cursor.execute("SELECT * from user")
    print 'authenticate'
    val = jsonify(data = cursor.fetchall())
    data = ''
    if data is None:
     return 'unsuccessfull'
    else:
     return send_from_directory('templates/', 'abcd.html')

@app.route('/getposts')
def getposts():
        user_id = 1
        query = 'select  * from post where user_id = ' + str(user_id);
        cursor.execute(query)
        data = cursor.fetchall()
        id = {'id':1}
        id['name']=1
        print '<<',data,'>>'
        cc = make_response(json.dumps(id)).data
        print '<<',cc,'>>'
        print make_response(json.dumps(data)).data
        #return make_response(json.dumps(data))
        #print data
        ret = []
        #unusual kind of values returned in flask
        #while while querying for the sql query
        for i in data: 
            obj = {'id': i[0], 'post_value':i[1] , 'user_id':i[2]}
            ret.append(obj)
            print obj
        rett = jsonify(data = ret)
        return rett

@app.route('/addpost',methods=['POST'])
def addpost():
        print request.data
        parsed_json = json.loads(request.data)
        post_value = parsed_json['post_value'];
        user_id = parsed_json['user_id'];
        print user_id , ' ', post_value
        query = 'INSERT INTO post (post_value,user_id) VALUES("' + post_value + '"' + "," + str(user_id) + ");";
        print '<<<',query,'>>'
        cursor.execute(query)
        data = cursor.fetchall()
        print data
        id = [{'id':1}]
        print jsonify(data = id)
        return jsonify(data = id)

if __name__ == '__main__':
    #getposts()
    #authenticate('','')
    app.debug = True
    app.run(host='0.0.0.0')
