from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")  # Ensure templates folder is correctly set

@app.route("/")
def dashboard():
    return render_template("dashboard.html")  # Ensure this file exists in the templates folder

if __name__ == "__main__":
    app.run(debug=True)
