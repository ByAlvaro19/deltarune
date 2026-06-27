import os
import json

def update_json_manifest(json_filename="runner.json"):
    if not os.path.exists(json_filename):
        print(f"B-baka! {json_filename} isn't in this folder!")
        return

    # 1. Get all files in the current folder
    current_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), ".").replace("\\", "/")
            
            # Ignore the JSON file, this script, and any split game.unx parts
            if (file == json_filename or 
                file == os.path.basename(__file__) or 
                "game.unx.part" in file):
                continue
                
            current_files.append(rel_path)

    current_files.sort()

    # 2. Read, modify, and save the JSON structure safely
    try:
        with open(json_filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # Only update the manifestFiles list, keeping everything else exactly as it was!
        if "manifestFiles" in data:
            data["manifestFiles"] = current_files
        else:
            print("W-wait... I couldn't find 'manifestFiles' in the JSON structure!")
            return

        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            
        print(f"There! I updated 'manifestFiles' inside {json_filename}. Everything else is untouched!")
        
    except Exception as e:
        print(f"Ugh, something went wrong: {e}")

if __name__ == "__main__":
    update_json_manifest()