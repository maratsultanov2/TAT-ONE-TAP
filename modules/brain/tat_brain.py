import json
import hashlib
from datetime import datetime

class TATBrain:
    def __init__(self, max_size=50000):
        self.max_size = max_size
        self.data = {'version': '2.0', 'type': 'tat_brain', 'created': datetime.now().isoformat(), 'persona': {}, 'key_concepts': [], 'current_state': {}, 'last_dialogue_hash': None}

    def to_json(self):
        return json.dumps(self.data, indent=2, ensure_ascii=False)

    def get_hash(self):
        return hashlib.sha256(self.to_json().encode()).hexdigest()
