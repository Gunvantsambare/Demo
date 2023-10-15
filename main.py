from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1 style='color:red'>Wellcome to My world a world of Advanture My name is Gunvant Sambhare <h1>"

@app.route('/about')
def about():
    return "<h1 style='color:yellow'> About page"

if __name__=='__main__':
    app.run(debug=True)


