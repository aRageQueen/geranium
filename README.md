# geranium
a python CLI to help analysts investigate anonymously surfaced data leaks by building a "structural fingerprint" of the known data (column format, username patterns, field types, etc.), then comparing it against known or scraped leaks to find probable sources or related breaches.


## Structure
```python
geranium/
├── geranium.py              # CLI entrypoint
├── parser.py                # Handles file loading and parsing
├── fingerprint.py           # Creates fingerprint JSON from data
├── comparators.py           # Compares new leaks to known samples
├── known_leaks/             # Store sample fingerprints of known breaches
│   ├── linkedin_2012.json
│   ├── myspace_2008.json
├── sample_leaks/            # Place for test leak files (CSV/JSON)
├── utils.py                 # Helper functions (regex, hash checks, etc.)
└── README.md
```