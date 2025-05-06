# File: config.py
import os

# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_TEXT_DIR = os.path.join(DATA_DIR, "raw_text")
PASSAGES_PATH = os.path.join(DATA_DIR, "external_data_passages.jsonl")
INDEX_PATH = os.path.join(DATA_DIR, "faiss_index")
KNOWN_FACES_PATH = os.path.join(DATA_DIR, "known_faces.pkl")

# RAG Models
RAG_MODEL_NAME = "facebook/rag-sequence-nq"

# Deepfake Detection Model (HuggingFace)
DEEPFAKE_MODEL = "prithivMLmods/Deep-Fake-Detector-Model"
