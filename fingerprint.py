import re
from utils import detect_hash_type, infer_field_type

def generate_fingerprint(df):
    fingerprint = {
        "fields": [],
        "email_domains": set(),
        "hash_type": None,
        "username_pattern": None
    }

    for col in df.columns:
        sample = df[col].dropna().astype(str).head(20)
        field_type = infer_field_type(sample)
        fingerprint["fields"].append(field_type)

        if field_type == "email":
            fingerprint["email_domains"].update(
                [x.split('@')[-1] for x in sample if "@" in x]
            )
        elif field_type == "hashed_password":
            fingerprint["hash_type"] = detect_hash_type(sample)
        elif field_type == "username":
            lengths = [len(x) for x in sample]
            pattern = re.compile(r"[a-z]{3}\d{3}")
            if all(pattern.fullmatch(x) for x in sample):
                fingerprint["username_pattern"] = pattern.pattern

    fingerprint["email_domains"] = list(fingerprint["email_domains"])
    return fingerprint
