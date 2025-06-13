# FileReceiver

### Uruchamianie:

#### Terminal 1

1. Wejdź do folderu app
2. Odpal serwer z komendą:
   ```powershell
   python .\servers\server.py
   ```

#### Terminal 2 (po odpaleniu serwera)

1. Wejdź do folderu app
2. Połącz się z serwerem komendą:
   ```powershell
   sftp -P 8222 user@127.0.0.1
   ```

**Hasło**: user

### Testowanie

Aby przetestować działanie, wpisz w Terminalu 2:

```bash
put A1B2C3D4E5F6.txt
```

Można utowrzyć własny plik dla testu, jednak musi on zawierać przedrostek `A1B2` lub `COD1`, inaczej żaden moduł nie będzie załadowany.

**Zmiany obserwuj w Terminalu 1.**
