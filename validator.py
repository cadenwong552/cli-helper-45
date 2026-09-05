import re

def validate_game_input(user_input, min_len=2, max_len=20):
    """Checks if input fits gaming-specific schema."""
    # Strips everything but alphanumeric and underscores, 
    # keeping names clean for command parsers
    clean = re.sub(r'[^a-zA-Z0-9_]', '', user_input)
    if not (min_len <= len(clean) <= max_len):
        return False, "Input length outside gaming bounds"
    if clean.lower() in ['admin', 'root', 'null']:
        return False, "Restricted alias detected"
    return True, clean

def process_loop():
    # Unusual approach: registry pattern using a functional dictionary
    handlers = {
        'play': lambda x: print(f"Initializing {x}..."),
        'quit': lambda x: exit(0)
    }
    
    while True:
        raw = input("cli-helper-45 > ").strip()
        parts = raw.split()
        if not parts: continue
        
        cmd = parts[0].lower()
        is_valid, result = validate_game_input(parts[1] if len(parts) > 1 else "")
        
        if cmd in handlers:
            if is_valid or cmd == 'quit':
                handlers[cmd](result)
            else:
                print(f"[!] Validation failure: {result}")
        else:
            print("[!] Unknown command syntax")