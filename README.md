# 🎲 Dice Game Paradox & Kurtosis Simulation

An interactive statistical simulation demonstrating how a seemingly highly profitable 100-sided dice game inevitably leads to net losses over long iterations. This project illustrates the concepts of **Fat Tails**, **Black Swan events**, and **Kurtosis** in probability.

## 📝 Game Logic
- **99% Chance:** You roll a standard 6-sided dice and **WIN** the amount shown ($1 to $6).
- **1% Chance:** You immediately **LOSE** $350.

While the expected value per roll looks positive at first glance, long-term repetitions trigger the negative impact of high kurtosis (extreme rare events), resulting in unavoidable overall bankruptcy.

---

## 💻 Code Architecture & Versions

This repository contains two different implementations to show progression in coding styles:

### 1. Manual Approach (`simulation_v1.py`)
- Uses a manual choice array to pick between the 1% and 99% probability.
- Great for step-by-step logic visualization.

### 2. Pythonic & Optimized (`simulation_v2.py`)
- Rewritten using direct NumPy random integer range (`1-100`).
- Cleaner, faster, and more memory-efficient code structure.

### 3. Interactive Web App (`app.py`)
- Built with **Streamlit** and **Matplotlib**.
- Provides a UI with a slider to test different iteration numbers dynamically.