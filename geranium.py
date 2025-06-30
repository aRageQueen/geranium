import argparse
from parser import load_file
from fingerprint import generate_fingerprint
from comparators import load_known_fingerprints, compare_fingerprint
import json

def main():
    parser = argparse.ArgumentParser(description="geranium: a lightweight leak fingerprinting tool.")
    parser.add_argument("file", help="Please add path to leak file (CSV or JSON)")
    args = parser.parse_args()

    df = load_file(args.file)
    fingerprint = generate_fingerprint(df)
    known = load_known_fingerprints()
    match = compare_fingerprint(fingerprint, known)

    fingerprint["match"] = match
    print(json.dumps(fingerprint, indent=2))


if __name__ == "__main__":
    main()
