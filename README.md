# 🎼 Disney AI: Dynamic Collaboration — Game-Theory Orchestration

> Fantasia-inspired, **Carnegie Hall Pillar: Dynamic Collaboration**.  
> Advanced multi-agent negotiation for orchestral storytelling where **music, animation, and dialogue** act as negotiating agents.

## 🔬 Technical Highlights (Advanced Only)
- **Bargaining Suite**: Alternating Offers (Rubinstein), **Nash Bargaining** (convex program), **Stackelberg** leader–follower scenes, **Regret Matching** for tempo.
- **MARL**: Centralized critic (toy) for stability + decentralized policies (tabular softmax) for cues.
- **Concurrency**: Parallel cue evaluation via Python `concurrent.futures` + **C++** tempo kernel (threads) + **Kotlin** coroutine stubs.
- **Metrics**: Collaboration Efficiency (CE), Fairness Δ (Nash gap), Temporal Stability (TS), and Audience Sentiment Proxy (ASP).
- **Reproducible Pipelines**: `pyproject.toml`, unit tests, deterministic seeds, GitHub Actions CI, and containerized run (Dockerfile).
- **Dashboards**: JS **Chart.js** “conductor’s screen” + Python Matplotlib exports.

## 🧭 Repo Map
```
disney-ai-dynamic-collab/
├─ python/
│  ├─ core/agents.py
│  ├─ core/negotiation.py
│  ├─ game/simulate_story.py
│  ├─ viz/plots.py
│  └─ tests/test_negotiation.py
├─ cpp/tempo_sim.cpp
├─ kotlin/Main.kt
├─ swift/Preview.swift
├─ js-chart/index.html
├─ sql/schema.sql
├─ data/prompts/example_scene.json
├─ pyproject.toml
├─ requirements.txt
├─ Dockerfile
├─ .github/workflows/ci.yml
└─ README.md
```

## 🚀 Quick Start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m python.game.simulate_story --scene data/prompts/example_scene.json --out out/run1
python -m python.viz.plots --csv out/run1/negotiation_log.csv --out out/run1
# open js-chart/index.html in a browser for dashboards
```

## 📐 Metrics
- **CE (Collaboration Efficiency)**: \( \textstyle CE = \frac{\sum_t R_t}{T} \) where rewards combine pacing, emotion, and sync.
- **Nash Gap**: distance to Nash product optimum.
- **TS (Temporal Stability)**: 1 − variance of tempo deltas (smoothed).
- **ASP (Proxy)**: linear blend of CE and TS with weights from survey priors.

## 🧩 Pillar Fit
This repo *demonstrates* the **Dynamic Collaboration** pillar with concrete implementations of bargaining + MARL to adapt **tempo / scene / dialogue** in real time.

---
© MIT License

