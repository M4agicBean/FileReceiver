import os
from watchfiles import awatch, Change, watch

from utils.utils import SFTP_ROOT
from helpers.module_getter import get_action_module


async def start_observation(path=SFTP_ROOT):
    print(f"[OBSERVER] Obserwuję katalog: {path}")
    async for changes in awatch(path):
        for change_type, file_path in changes:
            
            if change_type == Change.added:
                print(f"[OBSERVER] New file created: {file_path}")
                
                file_name = os.path.basename(file_path)
                handler = get_action_module(file_name)
                
                if handler:
                    await handler(file_name, file_path)
                else:
                    print(f"[OBSERVER] Brak handlera dla: {file_name}")
                
            elif change_type == Change.modified:
                print(f"[OBSERVER] File modified: {file_path}")
                
            elif change_type == Change.deleted:
                print(f"[OBSERVER] File deleted: {file_path}")