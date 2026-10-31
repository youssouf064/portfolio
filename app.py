import os
from flask import Flask, render_template

app = Flask(__name__)

# Fichier local pour enregistrer le nombre total de vues
COUNTER_FILE = "views.txt"

def get_and_increment_views():
    """Lit et incrémente le nombre de vues dans un fichier texte."""
    count = 1
    if os.path.exists(COUNTER_FILE):
        try:
            with open(COUNTER_FILE, "r") as f:
                content = f.read().strip()
                if content:
                    count = int(content) + 1
        except Exception:
            count = 1

    try:
        with open(COUNTER_FILE, "w") as f:
            f.write(str(count))
    except Exception:
        pass

    return count

# Injecte automatiquement la variable 'views_count' dans toutes les pages HTML
@app.context_processor
def inject_views():
    return dict(views_count=get_and_increment_views())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/formations")
def formations():
    return render_template("formations.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)