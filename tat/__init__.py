# tat/__init__.py
# Unified API for TAT-ONE-TAP ecosystem

from tat_monitor import TATMonitor
from tat_defense import adaptive_tat_detect, compute_tat_metrics
from tat_diff import tat_diff

class TAT:
    """Unified API for TAT modules."""
    def __init__(self, mode='monitor'):
        self.mode = mode
        if mode == 'monitor':
            self.monitor = TATMonitor()
        elif mode == 'defense':
            self.defense = adaptive_tat_detect
            self.metrics = compute_tat_metrics
        elif mode == 'diff':
            self.diff = tat_diff
        else:
            raise ValueError(f"Unknown mode: {mode}")

    def detect_anomaly(self, data, **kwargs):
        if self.mode == 'monitor':
            return self.monitor.detect(data, **kwargs)
        elif self.mode == 'defense':
            return self.defense(data, **kwargs)
        else:
            raise NotImplementedError("Detection not supported for diff mode")

    def compute_metrics(self, data, **kwargs):
        if self.mode == 'defense':
            return self.metrics(data, **kwargs)
        else:
            raise NotImplementedError("Metrics only available in defense mode")

    def diff(self, state1, state2):
        if self.mode == 'diff':
            return self.diff(state1, state2)
        else:
            raise NotImplementedError("Diff only available in diff mode")
