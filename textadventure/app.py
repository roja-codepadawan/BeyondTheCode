# app.py
from flask import Flask, render_template, redirect, url_for, abort
import json

app = Flask(__name__)

# Lade die Story und baue ein Dict mit string-Keys
with open("data/story_fixed.json", encoding="utf-8") as f:
    data = json.load(f)

# Erwartet: data["chapters"] ist eine Liste von Kapiteln mit "chapter_id" (int oder str)
chapters = { str(ch["chapter_id"]) : ch for ch in data["chapters"] }

@app.route("/")
def index():
    # Weiterleitung aufs erste Kapitel (ID=1)
    return redirect(url_for("play", chapter_id="1"))

@app.route("/play/<chapter_id>")
def play(chapter_id):
    chapter = chapters.get(chapter_id)
    if not chapter:
        # KeyError wird hier als 404 ausgegeben
        abort(404, description=f"Kapitel mit der ID {chapter_id} wurde nicht gefunden.")
    return render_template("chapter.html", chapter=chapter)

if __name__ == "__main__":
    app.run(debug=True)
