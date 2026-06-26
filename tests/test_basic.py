# ============================================================
# TAT-ONE-TAP: БАЗОВЫЕ ТЕСТЫ
# ============================================================
import sys
sys.path.insert(0, '.')

from src.tat_memory import TATMemory

def test_memory():
    memory = TATMemory()
    memory.save_session({'id': 'test', 'topics': 'test', 'summary': 'test'})
    brain = memory.restore()
    assert 'test' in brain
    print('✅ Тест пройден')

if __name__ == '__main__':
    test_memory()
