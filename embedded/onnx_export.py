# Copyright (C) 2026 Marat Sultanov
# SPDX-License-Identifier: AGPL-3.0-only

import torch
import torch.nn as nn
import torch.nn.functional as F

class Triplenet5D(nn.Module):
    def __init__(self, input_dim=384, hidden_dim=256, vector_dim=64):
        super().__init__()
        self.shared = nn.Linear(input_dim, hidden_dim)
        self.heads = nn.ModuleList([
            nn.Sequential(nn.Linear(hidden_dim, hidden_dim//2), nn.ReLU(),
                          nn.Linear(hidden_dim//2, vector_dim))
            for _ in range(5)
        ])
        self.classifier = nn.Linear(5 * vector_dim, 1)
    def forward(self, x):
        shared = F.relu(self.shared(x))
        head_vecs = [head(shared) for head in self.heads]
        concat = torch.cat(head_vecs, dim=1)
        return self.classifier(concat)

# Экспорт в ONNX
model = Triplenet5D()
model.eval()
dummy_input = torch.randn(1, 384)
torch.onnx.export(model, dummy_input, "half_vampire.onnx",
                  input_names=['input'], output_names=['logit'],
                  dynamic_axes={'input': {0: 'batch_size'},
                                'logit': {0: 'batch_size'}})
print("✅ ONNX model saved as half_vampire.onnx")
