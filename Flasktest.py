from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import Data

app = Flask(__name__)

Data.call_to_data()

names = Data.name()
travel = Data.travel()
wait = Data.wait()
total = Data.total()

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/findAHospital.html/')
def about():
    #if request.method == "GET":
        #return render_template("findAHospital.html", testdata=testdata)
    return render_template('findAHospital.html', names=names, travel=travel, wait=wait, total=total)


@app.route('/text', methods=['GET', 'POST'])
def text(comments=[]):
    #if request.method == "GET":
    return render_template("index.html", names=names, travel=travel, wait=wait, total=total)
    #return redirect(url_for('text'))


if __name__ == '__main__':
    app.run(debug=True)
