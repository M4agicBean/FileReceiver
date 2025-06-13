import asyncio
import asyncssh
import os, sys
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ssh_server, sftp_server

from utils.utils import *
from observers.observer import start_observation

async def start_server() -> None:
    print("_______________________________________________________________________")
    print(f"[LOG] Starting server {HOST}:{PORT}...")
    
    if not os.path.exists(SFTP_ROOT):
        os.makedirs(SFTP_ROOT)
    
    if not os.path.exists(HOST_KEY_FILE):
        logging.info(f"[LOG] Generating keys for: {HOST_KEY_FILE}")
        key = asyncssh.generate_private_key('ssh-ed25519')
        key.write_private_key(HOST_KEY_FILE)

    logging.info(f"[LOG] Starting SFTP server {HOST}:{PORT}...")
    logging.info(f"[LOG] User logged in='{USERNAME}'")
    print("_______________________________________________________________________")

    await asyncssh.create_server(
        ssh_server.MySSHServer, 
        host=HOST, 
        port=PORT,
        server_host_keys=[HOST_KEY_FILE],
        sftp_factory=sftp_server.MySFTPServer
    )
    
    await asyncio.get_event_loop().create_future()

async def main() -> None:
    await asyncio.gather(
            start_server(),
            start_observation()
    )
            
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    
    try:
        asyncio.run(main())
    except (OSError, asyncssh.Error) as exc:
        logging.error(f'[ERROR] Connection error: {exc}')
    except KeyboardInterrupt:
        logging.info("[LOG] Connection closed")