from flask import Flask

app= Flask(__name__)

@app.route("/")
def home():
    return "sargun ji world"


@app.route("/about")
def about():
    return "hii i am " 

@app.route("/contact/<name>")
def contact(name):
    return f"hii this is new citys{name}"


@app.route("/student/<name>/<course>")
def student(name,course):
    return f"my name is {name} and course is {course}"
       

if __name__=="__main__":
    app.run(debug=True)