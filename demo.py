"""
demo.py — generate Disney-flavored visuals for README.md
Creates four PNGs in the repo root:
  - workflow_diagram.png
  - character_frequency.png
  - tempo_ai_vs_human.png
  - collaboration_heatmap.png
"""

import numpy as np
import matplotlib.pyplot as plt

# 1) Orchestration Workflow (boxes + arrows, Disney labels)
stages = [
    "Music Score Prompt",
    "Agent Negotiation\n(Game Theory)",
    "Aligned Scene Plan",
    "Mickey (Sorcerer)",
    "Brooms",
    "Dancing Hippos",
    "Lion King Ensemble",
    "Fantasia-style Preview"
]

fig, ax = plt.subplots(figsize=(12, 3.2))
ax.axis('off')
xs = np.linspace(0.05, 0.95, len(stages))

for i, (label, x) in enumerate(zip(stages, xs)):
    rect = plt.Rectangle((x-0.06, 0.45), 0.12, 0.28, fill=False)
    ax.add_patch(rect)
    ax.text(x, 0.59, label, ha='center', va='center', fontsize=9)
    if i < len(stages)-1:
        ax.annotate("", xy=(xs[i+1]-0.06, 0.59), xytext=(x+0.06, 0.59),
                    arrowprops=dict(arrowstyle="->", lw=1.2))

plt.title("Orchestration Workflow (Fantasia-inspired)", pad=10)
plt.tight_layout()
plt.savefig("workflow_diagram.png", dpi=200)
plt.close()

# 2) Character Presence (Bar) — Disney entities
characters = ["Mickey", "Brooms", "Hippos", "Centaurs", "Lion King", "Beast"]
counts = np.array([52, 44, 37, 29, 48, 33])

plt.figure(figsize=(8, 5))
plt.bar(characters, counts)
plt.title("Character Presence in Collaborative Scenes")
plt.xlabel("Character")
plt.ylabel("Scene Count")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("character_frequency.png", dpi=200)
plt.close()

# 3) Tempo Shifts — Human vs AI
t = np.linspace(0, 180, 181)
np.random.seed(42)
human = 100 + 8*np.sin(t/12) + 3*np.sin(t/3.5) + np.random.normal(0, 0.6, size=t.size)
ai    =  98 + 9*np.sin((t+7)/13) + 2.5*np.sin((t+11)/4.0) + np.random.normal(0, 0.6, size=t.size)

plt.figure(figsize=(8, 5))
plt.plot(t, human, label="Human Conductor")
plt.plot(t, ai, label="AI Orchestrator")
plt.title("Tempo Shifts: Human vs AI")
plt.xlabel("Time (s)")
plt.ylabel("Tempo (BPM)")
plt.legend()
plt.tight_layout()
plt.savefig("tempo_ai_vs_human.png", dpi=200)
plt.close()

# 4) Collaboration Heatmap — influence between Disney entities
labels = ["Mickey", "Brooms", "Hippos", "Centaurs", "Lion King"]
rng = np.random.default_rng(11)
M = rng.uniform(0.05, 0.95, size=(len(labels), len(labels)))
for i in range(len(labels)):
    M[i, i] = 0.9  # self-stability emphasis

plt.figure(figsize=(6, 5))
plt.imshow(M, aspect='auto')
plt.title("Collaboration Heatmap (Agent Influence)")
plt.xticks(range(len(labels)), labels, rotation=25)
plt.yticks(range(len(labels)), labels)
plt.colorbar()
plt.tight_layout()
plt.savefig("collaboration_heatmap.png", dpi=200)
plt.close()

print("Generated: workflow_diagram.png, character_frequency.png, tempo_ai_vs_human.png, collaboration_heatmap.png")
