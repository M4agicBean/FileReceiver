import asyncio
import asyncssh
import os, sys
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ssh_server, sftp_server

from utils.utils import *
from observers.observer import start_observation

async def start_server():
    print("_______________________________________________________________________")
    print(f"[LOG] Uruchamianie serwera na {HOST}:{PORT}...")
    
    if not os.path.exists(SFTP_ROOT):
        os.makedirs(SFTP_ROOT)
    
    if not os.path.exists(HOST_KEY_FILE):
        logging.info(f"[LOG] Generowanie klucza dla: {HOST_KEY_FILE}")
        key = asyncssh.generate_private_key('ssh-ed25519')
        key.write_private_key(HOST_KEY_FILE)

    logging.info(f"[LOG] Uruchamianie serwera SFTP na {HOST}:{PORT}...")
    logging.info(f"[LOG] Zalogowano użytkownika='{USERNAME}' z hasłem='{PASSWORD}'")
    print("_______________________________________________________________________")

    await asyncssh.create_server(
        ssh_server.MySSHServer, 
        host=HOST, 
        port=PORT,
        server_host_keys=[HOST_KEY_FILE],
        sftp_factory=sftp_server.MySFTPServer
    )
    
    await asyncio.get_event_loop().create_future()

async def main():
    await asyncio.gather(
            start_server(),
            start_observation()
    )
            
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    
    try:
        asyncio.run(main())
    except (OSError, asyncssh.Error) as exc:
        logging.error(f'[ERROR] Błąd uruchamiania serwera: {exc}')
    except KeyboardInterrupt:
        logging.info("[LOG] Serwer zatrzymany przez użytkownika.")