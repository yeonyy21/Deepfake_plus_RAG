# File: build_passages.py
import json
import os
from config import RAW_TEXT_DIR, PASSAGES_PATH

def build_passages():
    with open(PASSAGES_PATH, "w", encoding="utf-8") as fout:
        for fname in os.listdir(RAW_TEXT_DIR):
            if not fname.endswith(".txt"):
                continue
            title = fname.replace(".txt","")
            with open(os.path.join(RAW_TEXT_DIR, fname), "r", encoding="utf-8") as fin:
                text = fin.read()
            for idx, paragraph in enumerate(text.split("\n\n")):
                if len(paragraph) < 50:
                    continue
                entry = {"title": title, "text": paragraph}
                fout.write(json.dumps(entry, ensure_ascii=False)+"\n")

if __name__ == "__main__":
    os.makedirs(os.path.dirname(PASSAGES_PATH), exist_ok=True)
    build_passages()
