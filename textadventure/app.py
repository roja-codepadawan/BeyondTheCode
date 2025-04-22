from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)

# Die Story wird aus der 'story.json' geladen
with open('data/story.json', 'r', encoding='utf-8') as f:
    story = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/<chapter>')
def play(chapter):
    # Überprüfe, ob das Kapitel existiert
    if chapter not in story['chapters']:
        return redirect(url_for('index'))  # Gehe zurück zum Anfang, falls Kapitel nicht existiert

    # Lade das Kapitel
    current_chapter = story['chapters'][chapter]
    return render_template('play.html', chapter=current_chapter)

if __name__ == '__main__':
    app.run(debug=True)