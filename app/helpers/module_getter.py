import importlib
from typing import Callable, Optional

def get_action_module(file_name: str) -> Optional[Callable]:
    if len(file_name) < 4:
        return None
    
    action_name = file_name[:4]
    module_path = f"modules.{action_name}_handler"
    print(f"[DEBUG] Próbuję załadować: {module_path}")
    
    try:
        action_module = importlib.import_module(module_path)
        print(f"[Serwer] Znaleziono i załadowano moduł: {module_path}")
        return getattr(action_module, 'process_file')
    except (ImportError, AttributeError) as e:
        print(f"[ERROR] Nie udało się załadować modułu {module_path}: {e}")
        return None
