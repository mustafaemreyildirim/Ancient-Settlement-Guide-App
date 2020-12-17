from flask import Flask, render_template
from wtform import *

app = Flask(__name__)
app.secret_key="later"

@app.route("/",methods=["GET", "POST"])
def index():

    reg_form = RegForm()
    if reg_form.validate_on_submit():
        return "good, you are in"

    return render_template("index.html",form=reg_form)

if __name__=="__main__":
    app.run(debug=True)

