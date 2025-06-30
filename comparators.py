import json
import os
from logger import get_logger
from utils import load_weights

def load_known_fingerprints():
    known = {}
    for file in os.listdir("known_leaks"):
        with open(f"known_leaks/{file}") as f:
            known[file.replace('.json', '')] = json.load(f)
    return known

def compare_fingerprint(fingerprint, known):
    best_match = None
    best_score = 0

    for name, known_fp in known.items():
        score = similarity_score(fingerprint, known_fp, known_name=name)
        if score > best_score and score >= 0.4:
            best_score = score
            best_match = name

    return {
        "most_similar": best_match if best_score >= 0.4 else "unknown",
        "confidence": round(best_score, 2)
    }


def similarity_score(fp1, fp2, known_name=""):
    weights = load_weights()
    score = 0

    # Fields
    f1 = set(fp1.get("fields", []))
    f2 = set(fp2.get("fields", []))
    if f1 == f2:
        field_score = 1.0
    else:
        intersection = f1 & f2
        union = f1 | f2
        field_score = len(intersection) / len(union) if union else 0
    score += field_score * weights["fields"]
    logger.info(f"[{known_name}] Field match score: {field_score:.2f}")

    # Hash
    if fp1.get("hash_type") == fp2.get("hash_type"):
        score += weights["hash_type"]
        logger.info(f"[{known_name}] Hash match: YES ({weights['hash_type']})")
    else:
        logger.info(f"[{known_name}] Hash match: NO")

    # Email domain
    d1 = set(fp1.get("email_domains", []))
    d2 = set(fp2.get("email_domains", []))
    if d1 & d2:
        score += weights["email_domains"]
        logger.info(f"[{known_name}] Email domain match: YES ({weights['email_domains']})")
    elif d1 and d2 and not d1 & d2:
        score -= 0.1
        logger.info(f"[{known_name}] Email domain mismatch: -0.1 penalty")

    # Username pattern
    if fp1.get("username_pattern") and fp2.get("username_pattern") and fp1.get("username_pattern") == fp2.get("username_pattern"):
        score += weights["username_pattern"]
        logger.info(f"[{known_name}] Username pattern match: YES")
    else:
        logger.info(f"[{known_name}] Username pattern match: NO")

    logger.info(f"[{known_name}] TOTAL SCORE: {score:.2f}")
    return round(score, 2)

# logging for real-time breakdown of score
logger = get_logger("comparator")
