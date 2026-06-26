from modules.brain.tat_brain import TATBrain
from modules.index.tat_index import TATIndex
from modules.diff.tat_diff import TATDiff
from modules.priority.tat_priority import TATPriority
from modules.achievements.tat_achievements import TATAchievements

class TATMemory:
    def __init__(self):
        self.brain = TATBrain()
        self.index = TATIndex()
        self.diff = TATDiff()
        self.priority = TATPriority()
        self.achievements = TATAchievements()

    def save_session(self, dialog):
        self.brain.data['current_state'] = dialog
        self.index.add(dialog.get('id'), dialog.get('topics'), dialog.get('summary'))

    def restore(self):
        return self.brain.to_json()
