
from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "vextro-secret-key"

SITE = {
    "name": "Vextro Racing",
    "tagline": "Speed. Precision. Glory.",
    "year": datetime.now().year,
    "colors": {"primary": "#800000", "accent": "#c8102e", "bg": "#fdfaf7"}
}

@app.context_processor
def inject_site():
    return dict(SITE=SITE)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name","").strip()
        email = request.form.get("email","").strip()
        message = request.form.get("message","").strip()
        if not (name and email and message):
            flash("Please fill out all fields.")
            return redirect(url_for("contact"))
        flash("Thanks! Your message has been sent.")
        return redirect(url_for("contact"))
    return render_template("contact.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("base.html", content="<section class='page container'><h2>Page not found</h2></section>"), 404

if __name__ == "__main__":
    app.run(debug=True)
