import sys, os
import asyncssh
import logging
import bcrypt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import *

class MySSHServer(asyncssh.SSHServer):
    def connection_made(self, conn: asyncssh.SSHServerConnection) -> None:
        print('[SERWER SSH] Połączenie SSH nawiązane.')

    def connection_lost(self, e: Exception) -> None:
        if e:
            logging.error(f'[ERROR SSH] Błąd połączenia: {e}')
        else:
            logging.info('[LOG SSH] Połączenie zamknięte.')

    def password_auth_supported(self) -> bool:
        return True

    def validate_password(self, username: str, password: str) -> bool:
        pw_hash = PASSWORDS.get(username)
        if not pw_hash:
            logging.warning(f"[ERROR SSH] Błąd uwierzytelniania: Nieznany użytkownik '{username}'")
            return False

        if bcrypt.checkpw(password.encode(), pw_hash):
            logging.info(f"[LOG SSH] Uwierzytelniono dla: '{username}'")
            return True
        else:
            logging.warning(f"[ERROR SSH] Bład uwierzytelniania dla: '{username}'")
            return False