# File: main.py
import argparse
from detect_and_verify import detect_and_verify

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image","-i", required=True, help="Path to image file")
    args = parser.parse_args()
    res = detect_and_verify(args.image)
    print(f"Person Identified: {res['person']}")
    print(f"Deepfake Detected: {res['deepfake']} (score: {res['score']:.2f})")
    if res["context"]:
        print("RAG Context Verification:")
        print(res["context"])
