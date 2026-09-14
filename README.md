# 🧭 SafePath AI

### Intelligent Route Search for Safer and Accessible Mobility

SafePath AI is an AI-assisted route planning and comparison system that finds routes between locations while considering different user requirements such as normal travel, wheelchair accessibility, and women's safety.

The project combines traditional graph-search algorithms with machine-learning-based road risk classification to demonstrate how intelligent routing can be used for safer and more accessible mobility.

---

## 🚀 Live Demo

🔗 **Live Application:**  
https://safepath-ai-7cf8.onrender.com

> The application is deployed using Render and can be accessed directly through the browser.

---

## 🎯 Project Objective

Traditional shortest-path systems mainly focus on distance or travel cost.

SafePath AI extends this idea by considering additional road characteristics such as:

- Accessibility
- Lighting
- Isolation
- Public activity
- Stairs
- Ramps
- Sidewalk availability
- Road safety risk

The system then compares two popular pathfinding algorithms:

- **Dijkstra's Algorithm**
- **A* (A-Star) Algorithm**

This allows users to see not only the selected route but also how efficiently each algorithm searches the road network.

---

## 🧠 How SafePath AI Works

The system follows these main steps:

```text
User selects Start & Destination
              ↓
       Select Route Mode
              ↓
     Build / Load Road Graph
              ↓
  Apply Accessibility / Safety Costs
              ↓
       Run Dijkstra Algorithm
              ↓
          Run A* Algorithm
              ↓
      Compare Search Results
              ↓
    Classify Road Risk using ML
              ↓
       Display Recommended Route