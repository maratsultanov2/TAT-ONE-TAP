class TATPriority:
    LEVELS = ['critical', 'normal', 'archive']
    def __init__(self):
        self.priorities = {}
    def set(self, dialog_id, level):
        if level in self.LEVELS:
            self.priorities[dialog_id] = level
    def get(self, dialog_id):
        return self.priorities.get(dialog_id, 'normal')
