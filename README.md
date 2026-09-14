# 🧭 SafePath AI

### Intelligent Route Search for Safer & Accessible Mobility

SafePath AI is an AI-assisted route planning and comparison system that combines
traditional graph-search algorithms with machine-learning-based road risk
classification.

The system compares **Dijkstra's Algorithm** and **A\* Algorithm** to find
routes between locations while adapting the route according to the selected
mobility requirement:

- 🛣️ Normal Route
- ♿ Wheelchair Accessibility
- 👩 Women Safety

The project also provides a visual representation of explored nodes and the
selected route, making the search behaviour of both algorithms easy to understand.

---

## 🌐 Live Demo

🚀 **Try SafePath AI online:**

👉 https://safepath-ai-7cf8.onrender.com

## 💻 Source Code

The complete project source code is available on GitHub:

👉 https://github.com/dataWithMuskan/SafePath-AI

---

# 🎯 Project Objective

Traditional shortest-path algorithms mainly focus on minimizing distance or
travel cost.

However, the shortest route is not always the most suitable route.

For example:

- A road may contain stairs and be unsuitable for wheelchair users.
- A poorly lit or isolated road may have a higher safety risk.
- A route with slightly higher cost may be preferable because it provides
  better accessibility or safety.

SafePath AI addresses this idea by combining:

**Graph Search + Accessibility Constraints + Safety Information + Risk Classification**

to produce a more context-aware route recommendation.

---

# 🧠 How SafePath AI Works

The system follows a simple pipeline:

```text
User selects Start & Destination
              ↓
       Selects Route Mode
              ↓
     Road Network / Graph
              ↓
   ┌──────────┴──────────┐
   ↓                     ↓
Dijkstra                A*
   ↓                     ↓
Shortest Path        Heuristic Search
   └──────────┬──────────┘
              ↓
     Route Comparison
              ↓
    Risk Classification
              ↓
      Final Route Result
              ↓
      Visual Map Display