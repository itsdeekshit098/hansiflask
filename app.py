from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    x=request.args.get("dsa")
    return render_template("index.html",abc=x)

if __name__ == "__main__":
    app.run(debug=True)
