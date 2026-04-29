# TAT-BRAIN Schema — Elina / Cophy collaboration

## Fields for Elina (hardware-rooted storage, integrity)
- `elina_hints.storage_hint`: `shared_memory.dat` — suggested long‑term storage location
- `elina_hints.integrity`: `hash_chain` — how Elina can verify the bundle hasn't been tampered with

## Fields for Cophy (evolution, dimension tracking)
- `cophy_hints.dimensions`: `["curiosity", "autonomy", "empathy"]` — which personality axes Cophy can update
- `cophy_hints.update_trigger`: `dream_cycle` — when Cophy should re‑ingest the compressed fact set

## Round‑trip flow (pseudo‑code)
```python
# 1. Jam → Elina: store raw memory
store_in_shared_memory(raw_data, user_id)

# 2. Marat → TAT: extract and compress
compressed = holographic_compress(raw_data, max_size=50KB)

# 3. Marat → Cophy: serve as fact feed
cophy.ingest(compressed, trigger="dream_cycle")

# 4. Cophy → Marat: update compressed representation
updated_repr = cophy.get_updated_facts()

# 5. Marat → Elina: round‑trip back
update_shared_memory(updated_repr)
