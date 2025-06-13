from hashlib import sha256

async def process_file(file_name, path):
    print("--------------------------------")
    print(f"Nazwa pliku: {file_name}")
    
    try:
        with open(path, "rb") as f:
            content = f.read()
            file_hash = sha256(content).hexdigest()
        print(f"Hash: {file_hash}")
        print("--------------------------------")
    except Exception as e:
        print(f"Błąd odczytu {e}")
        print("--------------------------------")