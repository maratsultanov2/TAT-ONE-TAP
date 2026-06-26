import json
from datetime import datetime

class TATAchievements:
    def __init__(self, filepath='achievements.json'):
        self.filepath = filepath
        self.data = {'achievements': []}
    def add(self, name, description, benchmark=None, result=None, rank=None):
        self.data['achievements'].append({'date': datetime.now().isoformat(), 'name': name, 'description': description, 'benchmark': benchmark, 'result': result, 'rank': rank})
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
