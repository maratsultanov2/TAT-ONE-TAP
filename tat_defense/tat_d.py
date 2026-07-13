# =============================================================================
# TAT-D: Structural Anomaly Detection Module
# Version: 1.0.0
# Author: Marat Sultanov
# License: PROPRIETARY
# =============================================================================

import numpy as np
import torch
import torch.nn as nn

__version__ = "1.0.0"
__author__ = "Marat Sultanov"
__license__ = "Proprietary"

class TAT7Layer(nn.Module):
    def __init__(self, input_dim=3, hidden_dim=32, n_heads=7, head_dim=16,
                 low=0.35, high=0.75, phase_shift=0, theta=1.987, imag_scale=0.3):
        super().__init__()
        self.n_heads = n_heads
        self.head_dim = head_dim
        self.theta = theta
        self.imag_scale = imag_scale
        self.noise = 0.007
        self.low = low
        self.high = high
        self.phase_shift = phase_shift
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.heads = nn.ModuleList([nn.Linear(hidden_dim, head_dim) for _ in range(n_heads)])
        self.harmony_matrix = nn.Parameter(torch.randn(n_heads, head_dim, head_dim) * 0.1)
        self.temperature = nn.Parameter(torch.tensor(0.7))

    def forward(self, x):
        e = self.encoder(x) + torch.randn_like(self.encoder(x)) * self.noise
        h = torch.stack([head(e) for head in self.heads], dim=1)
        ch = self.to_complex(h)
        coh = self.complex_coherence(ch)
        pos = h[:, 0].norm(dim=1).unsqueeze(1)
        pos = torch.where(pos < self.low, self.low + (pos - self.low)*0.5,
                         torch.where(pos > self.high, self.high + (pos - self.high)*0.5, pos))
        div = pos - coh
        features = h.reshape(h.size(0), -1)
        return div, features

    def to_complex(self, h):
        phase = self.theta + self.phase_shift
        return h + 1j * (h * self.imag_scale * torch.sin(phase))

    def complex_coherence(self, ch):
        coh = torch.zeros(ch.size(0), device=ch.device)
        p = 0
        for a in range(self.n_heads):
            for b in range(a+1, self.n_heads):
                dot = torch.abs((ch[:, a, :] * ch[:, b, :].conj()).sum(dim=1))
                norm = torch.sqrt((ch[:, a, :].abs()**2).sum(1) * (ch[:, b, :].abs()**2).sum(1) + 1e-8)
                coh += dot / norm
                p += 1
        return coh / p

def adaptive_tat_detect(X, window=10, threshold_div=0.95, threshold_harm=0.05, block_sizes=None):
    n = len(X)
    div, harm = compute_tat_metrics(X, window, block_sizes)
    preds = np.zeros(n)
    for i in range(n):
        if div[i] > np.percentile(div, threshold_div*100) or harm[i] < np.percentile(harm, threshold_harm*100):
            preds[i] = 1
    return preds

def compute_tat_metrics(X, window=10, block_sizes=None):
    n = len(X)
    div = np.zeros(n)
    harm = np.zeros(n)
    if block_sizes is None:
        block_sizes = [X.shape[1]]
    for i in range(n):
        start = max(0, i - window//2)
        end = min(n, i + window//2)
        if end - start < 5:
            div[i] = 0.5
            harm[i] = 0.5
            continue
        window_data = X[start:end]
        distances = np.linalg.norm(window_data - X[i], axis=1)
        nbrs = np.argsort(distances)[1:6]
        if len(nbrs) < 3:
            div[i] = 0.5
            harm[i] = 0.5
            continue
        div[i] = np.mean(distances[nbrs])
        vectors = window_data[nbrs] - X[i]
        if len(vectors) > 1:
            sims = []
            for j in range(len(vectors)):
                for k in range(j+1, len(vectors)):
                    sim = 0
                    pos = 0
                    for block_size in block_sizes:
                        vj = vectors[j, pos:pos+block_size]
                        vk = vectors[k, pos:pos+block_size]
                        if np.linalg.norm(vj) > 0 and np.linalg.norm(vk) > 0:
                            sim += np.dot(vj, vk) / (np.linalg.norm(vj) * np.linalg.norm(vk))
                        pos += block_size
                    sims.append(sim / len(block_sizes))
            if sims:
                harm[i] = np.mean(sims)
            else:
                harm[i] = 0
        else:
            harm[i] = 0
    div = (div - div.min()) / (div.max() - div.min() + 1e-8)
    harm = (harm - harm.min()) / (harm.max() - harm.min() + 1e-8)
    return div, harm
