from flask import Flask, render_template, redirect


app = Flask(__name__)



@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html")

@app.route("/scrape")
def scrape():
   

if __name__ == "__main__":
    app.run(debug=True)
    