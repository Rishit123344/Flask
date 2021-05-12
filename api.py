from flask import Flask,request,jsonify

tasks = [
    {
        'id':1,
        'title':u'buy groceries',
        'description':u'milk,cheese,chocolate,chips',
        'done':False,

    },
       {
        'id':2,
        'title':u'learn java',
        'description':u'search for tutorials on web',
        'done':False,
        
    }
]
app = Flask(__name__)
@app.route('/')
def helloWorld():
    return 'hello World'
@app.route('/add-data',methods = ['POST'])
def addtask():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide data'
        },400)
    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        'status':'success',
        'message':'task added successfully'
    })
@app.route('/getdata')
def gettask():
    return jsonify({
        'data':tasks
    })
if (__name__ == '__main__'):
    app.run(debug = True)
    