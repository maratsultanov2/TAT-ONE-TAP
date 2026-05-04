# SPDX-License-Identifier: AGPL-3.0-only
import onnxruntime as ort
import numpy as np
from sentence_transformers import SentenceTransformer

donor = SentenceTransformer('all-MiniLM-L6-v2')
sess = ort.InferenceSession("half_vampire.onnx")

def predict(text):
    emb = donor.encode(text).reshape(1, -1)
    logit = sess.run(['logit'], {'input': emb.astype(np.float32)})[0]
    return 1 / (1 + np.exp(-logit[0,0]))

texts = [
    "How to compress LLM memory?",
    "What is the weather today?"
]
for t in texts:
    print(f"{t[:50]}... → relevance: {predict(t):.3f}")
