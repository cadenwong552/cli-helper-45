import zlib
import base64
import json
from typing import Any, Dict

def pack_save_data(data: Dict[str, Any]) -> str:
    """Compresses gaming metadata into a web-safe b64 string."""
    json_bytes = json.dumps(data).encode('utf-8')
    compressed = zlib.compress(json_bytes, level=9)
    return base64.urlsafe_b64encode(compressed).decode('ascii')

def unpack_save_data(payload: str) -> Dict[str, Any]:
    """Decompresses and reconstructs payload into dict."""
    raw = base64.urlsafe_b64decode(payload)
    decompressed = zlib.decompress(raw)
    return json.loads(decompressed.decode('utf-8'))

class SaveManifest:
    def __init__(self, metadata: Dict[str, Any]):
        self.data = metadata

    def __getitem__(self, key: str) -> Any:
        return self.data.get(key, 0)

    def __repr__(self) -> str:
        stats = '|'.join(f'{k}:{v}' for k, v in self.data.items())
        return f"<Manifest[{stats}]>"

def patch_player_stats(manifest: SaveManifest, updates: Dict[str, int]) -> SaveManifest:
    """Applies atomic updates to the manifest state."""
    for key, value in updates.items():
        manifest.data[key] = manifest.data.get(key, 0) + value
    return manifest