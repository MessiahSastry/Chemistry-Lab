from flask import Flask, render_template

# Create an instance of the Flask web application
app = Flask(__name__)


# This tells Flask what to do when someone visits the main homepage ("/")
@app.route("/")
def main_menu():
    # It will serve the index.html file from the 'templates' folder.
    return render_template("index.html")


# This creates the page for our pH lab experiment ("/ph-lab")
@app.route("/ph-lab")
def ph_lab_page():
    # It will serve the ph_lab.html file.
    return render_template("ph_lab.html")


# This part allows us to run the server directly
if __name__ == "__main__":
    app.run(debug=True)