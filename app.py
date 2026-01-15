from flask import Flask, render_template, request
import pyfiglet

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        if text:
            output = pyfiglet.figlet_format(text)

    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
