import sys, os
import asyncssh
import logging
import bcrypt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import *

class MySSHServer(asyncssh.SSHServer):
    def connection_made(self, conn: asyncssh.SSHServerConnection) -> None:
        print('[SERWER SSH] SSH connection started!')

    def connection_lost(self, e: Exception) -> None:
        if e:
            logging.error(f'[ERROR SSH] Connection error: {e}')
        else:
            logging.info('[LOG SSH] Connection closed')

    def password_auth_supported(self) -> bool:
        return True

    def validate_password(self, username: str, password: str) -> bool:
        pw_hash = PASSWORDS.get(username)
        if not pw_hash:
            logging.warning(f"[ERROR SSH] Authentication failed: unknown user '{username}'")
            return False

        if bcrypt.checkpw(password.encode(), pw_hash):
            logging.info(f"[LOG SSH] Authenticated for: '{username}'")
            return True
        else:
            logging.warning(f"[ERROR SSH] Authentication error for: '{username}'")
            return False