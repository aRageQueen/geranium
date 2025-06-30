import re

def is_hex(s):
    return bool(re.fullmatch(r"[0-9a-fA-F]+", s))

def detect_hash_type(samples):
    samples = list(set(samples))[:10]
    if all(len(x) == 32 and is_hex(x) for x in samples):
        return "MD5"
    elif all(len(x) == 40 and is_hex(x) for x in samples):
        return "SHA1"
    elif all(len(x) == 64 and is_hex(x) for x in samples):
        return "SHA256"
    elif all(x.startswith("$2b$") or x.startswith("$2a$") for x in samples):
        return "bcrypt"
    return "unknown"

def infer_field_type(series):
    sample = series.dropna().astype(str).head(20)

    if all("@" in x and "." in x for x in sample):
        return "email"
    elif all(is_hex(x) and len(x) in (32, 40, 64) for x in sample):
        return "hashed_password"
    elif all(re.match(r"^[a-zA-Z0-9_\-\.]{3,}$", x) for x in sample):
        return "username"
    elif all(len(x.split()) < 5 for x in sample):  # Short hints, common pattern
        return "hint"
    else:
        return "unknown"
