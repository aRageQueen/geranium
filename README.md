# geranium
a python CLI to help analysts investigate anonymously surfaced data leaks by building a "structural fingerprint" of the known data (column format, username patterns, field types, etc.), then comparing it against known or scraped leaks to find probable sources or related breaches.

## Features
- Generate structured "fingerprints" from unknown CSV or JSON data
- Match unknown leaks against a library of known breach structures
- Scoring system based on fields, hash types, email domains, and username patterns
- Lightweight and extensible Python codebase
- Configurable scoring weights via `weights.json`
- CLI-based interface with structured JSON output
- Logging of comparison decisions (field match, hash match, etc.)

## Testing
Run the tool with included test files in sample_leaks/ and check output against known_leaks/.

Unit tests coming soon.

## Structure
```python
geranium/
├── geranium.py              # CLI entrypoint
├── parser.py                # Handles file loading and parsing
├── fingerprint.py           # Creates fingerprint JSON from data
├── comparators.py           # Compares new leaks to known samples
├── known_leaks/             # Store sample fingerprints of known breaches
│   ├── linkedin_2012.json
│   ├── adobe_2013.json
├── sample_leaks/            # Stored test leak files (CSV/JSON)
├── utils.py                 # Helper functions (regex, hash checks, etc.)
├── weights.json             # Scoring configuration
├── logger.py                # Logger setup 
└── README.md
```