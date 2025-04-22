import json

# Datei-Pfade
INPUT_PATH  = "story.json"
OUTPUT_PATH = "story_fixed.json"

# Hier das Endkapitel angeben, auf das alle ungültigen Verweise zeigen sollen:
REPLACEMENT_END_CHAPTER = 55

def load_story(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_story(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def fix_next_chapters(story, replacement_id):
    # Alle gültigen Kapitel-IDs sammeln
    valid_ids = {ch["chapter_id"] for ch in story["chapters"]}

    # Jedes Choice-Objekt prüfen und ggf. ersetzen
    for ch in story["chapters"]:
        for choice in ch.get("choices", []):
            if choice["next_chapter_id"] not in valid_ids:
                print(f"Kapitel {ch['chapter_id']} → ungültig {choice['next_chapter_id']} → ersetze mit {replacement_id}")
                choice["next_chapter_id"] = replacement_id

    return story

if __name__ == "__main__":
    story = load_story(INPUT_PATH)
    fixed = fix_next_chapters(story, REPLACEMENT_END_CHAPTER)
    save_story(fixed, OUTPUT_PATH)
    print(f"\nFertig! Gefixtes Story-JSON gespeichert als: {OUTPUT_PATH}")
