import os
import re

def update_manifest(js_filename="index.js"):
    if not os.path.exists(js_filename):
        print(f"{js_filename} isn't in this folder!")
        return

    # 1. Get all files in the current folder
    current_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            # Get relative path (e.g., "mus/acid_tunnel.ogg")
            rel_path = os.path.relpath(os.path.join(root, file), ".").replace("\\", "/")
            
            # Ignore the JS file, this script, and any split game.unx parts
            if (file == js_filename or 
                file == os.path.basename(__file__) or 
                "game.unx.part" in file):
                continue
                
            current_files.append(rel_path)

    # Sort them nicely
    current_files.sort()

    # 2. Read the original index.js
    with open(js_filename, "r", encoding="utf-8") as f:
        content = f.read()

    # 3. Use regex to find and replace the files inside manifestFiles()
    pattern = r'(function manifestFiles\s*\(\s*\)\s*\{\s*return\s*\[)(.*?)(\]\.join\(\s*";"\s*\);)'
    
    if not re.search(pattern, content, re.DOTALL):
        print("I couldn't find the manifestFiles function! Did you mess up the code?!")
        return

    # Format the new file list string for JS
    formatted_files = " " + ",\n".join(f'"{f}"' for f in current_files) + " "
    
    # Replace it!
    new_content = re.sub(pattern, r'\1\n' + formatted_files + r'\3', content, flags=re.DOTALL)

    # 4. Save the updated index.js
    with open(js_filename, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"I updated {js_filename} with {len(current_files)} files.")

if __name__ == "__main__":
    update_manifest()