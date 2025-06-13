from hashlib import sha256

async def process_file(file_name: str, path: str) -> None:
    print("--------------------------------")
    print(f"File name: {file_name}")
    
    try:
        with open(path, "rb") as f:
            content = f.read()
            file_hash = sha256(content).hexdigest()
        print(f"Hash: {file_hash}")
        print("--------------------------------")
    except Exception as e:
        print(f"Read error {e}")
        print("--------------------------------")