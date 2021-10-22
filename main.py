from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    home = "this is my home page"
    return render_template('index.html', home1= home)
@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')
  



if __name__ == "__main__":
    app.run(debug=True)