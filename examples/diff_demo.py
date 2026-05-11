from tat_diff import weights_to_string, compute_diff, apply_diff

# Пример для встраивания в диалог с DeepSeek
morning = {"theme":0.207, "role":0.198, "emotion":0.197, "meaning":0.201, "goal":0.198}
evening = {"theme":0.220, "role":0.190, "emotion":0.250, "meaning":0.200, "goal":0.190}

diff = compute_diff(morning, evening)
print(f"TAT-DIFF: {diff}")
# Этот diff пользователь копирует в конец дневного диалога
# На следующее утро система применяет его к сохранённому TAT-BRAIN
