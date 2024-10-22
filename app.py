from flask import Flask,render_template



app = Flask(__name__)
@app.route("/",methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/arts',methods=["GET"])
def arts():
    return render_template('arts.html')


