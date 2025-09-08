#!/usr/bin/env python3
import json
import re
import sys
from urllib.parse import urlparse

def safe_label(s):
    # lowercase, replace invalid chars with '-'
    return re.sub(r'[^a-z0-9-]', '-', s.lower())

def generate_aliases(entry):
    # entry: dict parsed from nlm-entry.schema.json instance
    service = entry.get('service', '')
    operation = entry.get('operation', '')
    version = entry.get('version', '')
    namespace = entry.get('namespace', '')
    # long alias: <operation>.<version>.<service>.<namespace>.org.uk
    long_alias = ".".join([safe_label(operation), safe_label(version), safe_label(service), safe_label(namespace), "org", "uk"])
    # short alias: <operation>.<service>.<namespace>.svc.local (example)
    short_alias = ".".join([safe_label(operation), safe_label(service), safe_label(namespace), "svc", "local"])
    return [long_alias, short_alias]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: generate_aliases.py nlm-entry.json")
        sys.exit(2)
    with open(sys.argv[1]) as f:
        entry = json.load(f)
    for a in generate_aliases(entry):
        print(a)
