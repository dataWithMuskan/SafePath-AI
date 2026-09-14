\# 🧭 SafePath AI



\## Intelligent Route Search for Safer \& Accessible Mobility



SafePath AI is a web-based intelligent route search system that compares \*\*Dijkstra's algorithm\*\* and \*\*A\\\*\*\* algorithm to find routes between locations.



The system also considers different mobility requirements such as:



\- 🛣 Normal route

\- ♿ Wheelchair accessibility

\- 👩 Women safety



It uses an \*\*AI-based road risk classifier\*\* to estimate the risk level of roads based on road-related features.



\---



\## 🎯 Project Objective



The main objective of SafePath AI is to demonstrate how route-search algorithms can be combined with safety and accessibility information to provide more suitable routes.



The system:



1\. Accepts a starting location and destination.

2\. Allows the user to select a route mode.

3\. Runs Dijkstra and A\* algorithms.

4\. Compares the routes produced by both algorithms.

5\. Applies accessibility restrictions for wheelchair mode.

6\. Applies safety penalties for women-safety mode.

7\. Uses an AI classifier to predict road risk.

8\. Displays the selected route and explored nodes on an interactive map.



\---



\## ✨ Features



\### 🔎 Route Search



SafePath AI implements two pathfinding algorithms:



\- \*\*Dijkstra's Algorithm\*\*

\- \*\*A\\\* Search Algorithm\*\*



Both algorithms return:



\- Selected path

\- Route cost

\- Number of explored nodes



\### 🤖 AI Risk Classification



The project contains a machine-learning based road risk classifier.



The classifier uses road features such as:



\- Lighting

\- Isolation

\- Public activity

\- Stairs

\- Ramp

\- Sidewalk



The current demonstration classifier achieves:



\*\*Test Accuracy: 75%\*\*



Risk levels are:



\- Low

\- Medium

\- High



> The road feature values used in this project are demonstration values and are not real-world measurements.



\### ♿ Wheelchair Accessibility



Wheelchair mode checks whether a road is accessible.



A road containing:



\- Stairs

\- No ramp



is treated as inaccessible and is avoided by the route search.



\### 👩 Women Safety



Women Safety mode applies additional cost penalties based on predicted road risk.



| Risk | Safety Penalty |

|------|----------------|

| Low | 0 |

| Medium | 5 |

| High | 10 |



This allows the route search to prefer safer roads when possible.



\---

# 🧭 SafePath AI

Intelligent Route Search for Safer & Accessible Mobility

## 🌐 Live Demo

[Open SafePath AI](https://safepath-ai-7cf8.onrender.com)

## 💻 GitHub Repository

This repository contains the complete source code of SafePath AI.



\## 🗂️ Project Structure



```text

SafePath-AI-Muskan/

│

├── accessibility.json

├── app.py

├── classifier.py

├── requirements.txt

├── results.json

├── road\\\_profiles.py

├── scoring.py

├── test.py

├── test\\\_classifier.py

│

├── algorithms/

│   ├── astar.py

│   ├── dijkstra.py

│   └── graph.py

│

├── data/

│   └── road\\\_data.csv

│

├── frontend/

│   ├── app.js

│   ├── index.html

│   └── style.css

│

└── safety/

\&#x20;   └── safety.json


