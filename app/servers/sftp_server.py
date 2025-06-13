import asyncssh
import os, sys
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers.module_getter import get_action_module
from utils.utils import *


class MySFTPServer(asyncssh.SFTPServer):

    def __init__(self, chan: asyncssh.SSHServerChannel) -> None:
        if not os.path.exists(SFTP_ROOT):
            os.makedirs(SFTP_ROOT)
        
        username = chan.get_extra_info('username')
        logging.info(f"[LOG SFTP] SFTP server started!")

        super().__init__(chan, chroot=SFTP_ROOT) # type: ignore
        