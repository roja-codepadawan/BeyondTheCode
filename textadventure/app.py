import json
from flask import Flask, render_template

app = Flask(__name__)

# Lade die Story-Daten

with open('data/story.json', 'r', encoding='utf-8') as file:
    story = json.load(file)

print(story)  # Überprüfe die Struktur der geladenen Daten

@app.route("/play/<int:chapter_id>")
def play(chapter_id):
    print(f"Chapter requested: {chapter_id}")  # Debug-Ausgabe
    chapter = next((ch for ch in story['chapters'] if ch['chapter_id'] == chapter_id), None)
    if chapter is None:
        print(f"Chapter {chapter_id} not found.")  # Debug-Ausgabe
        return f"Kapitel mit der ID {chapter_id} wurde nicht gefunden.", 404
    return render_template("chapter.html", chapter=chapter)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('kapitel_nicht_gefunden.html'), 404

if __name__ == "__main__":
    app.run(debug=True)