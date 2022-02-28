#from crypt import methods
from flask import Flask, render_template, request

# We are going to tell python that from here downlards we have a flask app 
app = Flask(__name__)

@app.route('/')
def my_function():
    return "Welcome to my personal page, I'm José"

@app.route('/student')
def second_function():
    return "I can change pages/routes"


@app.route('/home', methods = ['POST', 'GET'])
def homepage():
    
    if request.method == "POST":
        
        ## here you do your logic with the inputs from user
        param = request.form['parameter 1']

        if param.isdigit():

            param = int(param) + 10

            return render_template("main.html", value = param)
        
        else:
            
            return render_template("main.html", value="no logic")

    else:
        return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True, port=4552)