from flask import Flask, render_template   
app = Flask(__name__)

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)