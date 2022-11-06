from flask import Flask , jsonify , request


app = Flask(__name__)

contacts = [
    {
        'id'      : '1' ,
        'name'    : u'Raj' ,
        'contact' : u'+91 9837531687' ,
        'done'    : False
    } ,
    {
        'id'      : '2' ,
        'name'    : u'Raju' ,
        'contact' : u'+91 9837531687' ,
        'done'    : False
    } ,
    {
        'id'      : '3' ,
        'name'    : u'Rajesh' ,
        'contact' : u'+91 9837531687' ,
        'done'    : False
    } ,
    {
        'id'      : '4' ,
        'name'    : u'Rajni' ,
        'contact' : u'+91 9837531687' ,
        'done'    : False
    } ,
    {
        'id'      : '5' ,
        'name'    : u'Rajvender' ,
        'contact' : u'+91 9837531687' ,
        'done'    : False
    } 
]

@app.route('/')
def hello():
    return 'Contact List :'

@app.route('/app-data' , methods = ['POST'])
def add_task():
    if not request.json :
        return jsonify({
            'status' : 'error' , 
            'msg'    : 'Please provide the correct data :)'
        } , 400)
   
    contact = {
        'id'       : contacts[-1]['id']+1 ,
        'name'     : request.json['name'] , 
        'conatact' : request.json('contact') , 
        'done'     : False
        }
    contacts.append(contact)

    return jsonify({
        'status' : 'Sucess' ,
        'msg'    : 'Conatct Added Sucessfully'
    })

@app.route('/get-data')
def get_contact():
    return jsonify({
        'data' : 'contacts'
    })

if __name__ == '__main__':
    app.run(debug = True)