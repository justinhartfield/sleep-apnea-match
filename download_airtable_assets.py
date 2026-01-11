#!/usr/bin/env python3
"""
Download all image assets from Airtable and create a mapping file.
"""

import json
import os
import requests
from pathlib import Path

# Create assets directory
ASSETS_DIR = Path("assets/images/airtable")
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# Load the Airtable image assets
with open("api/airtable/tblyxWUg8pDotWkus.json", "r") as f:
    data = json.load(f)

# Mapping for later use
image_mapping = []

for record in data["records"]:
    fields = record.get("fields", {})

    image_name = fields.get("Image Name", "Unknown")
    category = fields.get("Category", "General")
    description = fields.get("Description", "")
    related_procedure = fields.get("Related Procedure", "General")
    image_files = fields.get("Image File", [])
    source_url = fields.get("Source URL", "")

    if not image_files:
        continue

    # Get the first image file
    img = image_files[0]
    url = img.get("url", "")
    filename = img.get("filename", "")

    if not url or not filename:
        continue

    # Create a clean filename based on image name
    clean_name = image_name.lower().replace(" ", "-").replace("/", "-")
    clean_name = "".join(c for c in clean_name if c.isalnum() or c in "-_")

    # Get file extension
    ext = filename.split(".")[-1] if "." in filename else "jpg"
    local_filename = f"{clean_name}.{ext}"
    local_path = ASSETS_DIR / local_filename

    # Download the image
    print(f"Downloading: {image_name}")
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(response.content)
            print(f"  Saved to: {local_path}")
        else:
            print(f"  Failed: HTTP {response.status_code}")
            continue
    except Exception as e:
        print(f"  Error: {e}")
        continue

    # Add to mapping
    image_mapping.append({
        "name": image_name,
        "category": category,
        "description": description,
        "related_procedure": related_procedure,
        "local_path": str(local_path),
        "original_source": source_url
    })

# Save mapping file
mapping_path = ASSETS_DIR / "image-mapping.json"
with open(mapping_path, "w") as f:
    json.dump(image_mapping, f, indent=2)

print(f"\nDownloaded {len(image_mapping)} images")
print(f"Mapping saved to: {mapping_path}")

# Print summary by category
categories = {}
for img in image_mapping:
    cat = img["category"]
    categories[cat] = categories.get(cat, 0) + 1

print("\nImages by category:")
for cat, count in sorted(categories.items()):
    print(f"  {cat}: {count}")
