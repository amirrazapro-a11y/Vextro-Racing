
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "vextro-secret-key"  # needed for flash messages

# Basic site info (edit here or in templates)
SITE = {
    "name": "Vextro Racing",
    "year": datetime.now().year,
    "colors": {"primary": "#800000", "accent": "#c8102e", "bg": "#fdfaf7"}
}

@app.context_processor
def inject_site():
    return dict(SITE=SITE)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/car')
def car():
    return render_template("car.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        if not (name and email and message):
            flash("Please fill out all fields before sending.")
            return render_template("contact.html", success=False)
        print(f"📩 New message - Name: {name} | Email: {email}\n{message}")
        flash("Your message has been sent! We'll get back to you soon.")
        return render_template("contact.html", success=True)
    return render_template("contact.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)
