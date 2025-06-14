from flask import Flask, render_template, jsonify

# Create an instance of the Flask web application
app = Flask(__name__)

# --- DATA SOURCE ---
# The lists of chemicals now live in our Python back-end.
# This is now the single source of truth.
ACIDS = [
    {"name": "Hydrochloric Acid", "formula": "HCl", "ph": 1, "color": "#f25b77"},
    {"name": "Sulphuric Acid", "formula": "H₂SO₄", "ph": 1, "color": "#fb799c"},
    {"name": "Nitric Acid", "formula": "HNO₃", "ph": 2, "color": "#f7c38b"},
    {"name": "Acetic Acid", "formula": "CH₃COOH", "ph": 3, "color": "#ffc69e"},
    {"name": "Lemon Juice", "formula": "", "ph": 3, "color": "#fff47a"},
    {"name": "Carbonic Acid", "formula": "H₂CO₃", "ph": 4, "color": "#bff0e0"},
    {"name": "Citric Acid Sol.", "formula": "", "ph": 2, "color": "#ffec90"}
]

BASES = [
    {"name": "Sodium Hydroxide", "formula": "NaOH", "ph": 13, "color": "#9fe8c7"},
    {"name": "Potassium Hydroxide", "formula": "KOH", "ph": 14, "color": "#4ee6a7"},
    {"name": "Calcium Hydroxide", "formula": "Ca(OH)₂", "ph": 12, "color": "#63ffe1"},
    {"name": "Ammonium Hydroxide", "formula": "NH₄OH", "ph": 11, "color": "#adf1e6"},
    {"name": "Baking Soda", "formula": "NaHCO₃", "ph": 9, "color": "#e7fdcb"},
    {"name": "Soap Water", "formula": "", "ph": 10, "color": "#e6f1ff"},
    {"name": "Milk of Magnesia", "formula": "Mg(OH)₂", "ph": 10, "color": "#b1f8f9"}
]


# --- HTML PAGE ROUTES (The "Dining Room") ---

@app.route("/")
def main_menu():
    """Serves the main menu page."""
    return render_template("index.html")

@app.route("/ph-lab")
def ph_lab_page():
    """Serves the pH lab experiment page."""
    return render_template("ph_lab.html")


# --- API ROUTES (The "Kitchen") ---
# NEW: These routes provide the chemical data as JSON.

@app.route("/api/acids")
def get_acids():
    """Returns the list of acids as JSON data."""
    return jsonify(ACIDS)

@app.route("/api/bases")
def get_bases():
    """Returns the list of bases as JSON data."""
    return jsonify(BASES)


# This part allows us to run the server directly
if __name__ == "__main__":
    app.run(debug=True)
