import os

def split_file(filename="data.win", chunk_size_mb=16):
    if not os.path.exists(filename):
        print(f"{filename} isn't here!")
        return
    
    # 16MB chunk size
    chunk_size = chunk_size_mb * 1024 * 1024
    part_num = 1
    
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            part_name = f"game.unx.part{part_num}"
            with open(part_name, 'wb') as p:
                p.write(chunk)
            part_num += 1
            
    print("Done!")

if __name__ == "__main__":
    split_file()