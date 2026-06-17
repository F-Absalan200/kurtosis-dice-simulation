# 🎲 Dice Game Paradox & Kurtosis Simulation

An interactive statistical simulation demonstrating how a seemingly highly profitable 100-sided dice game inevitably leads to net losses over long iterations. This project illustrates the concepts of **Fat Tails**, **Black Swan events**, and **Kurtosis** in probability.

## 📝 Game Logic
- **99% Chance:** You roll a standard 6-sided dice and **WIN** the amount shown ($1 to $6).
- **1% Chance:** You immediately **LOSE** $350.

<img width="1408" height="768" alt="Black_swan" src="https://github.com/user-attachments/assets/998e61d9-6fc4-48e6-ac86-6f87791f3916" />


While the expected value per roll looks positive at first glance, long-term repetitions trigger the negative impact of high kurtosis (extreme rare events), resulting in unavoidable overall bankruptcy.

---

## 💻 Code Architecture & Versions

This repository contains two different implementations to show progression in coding styles:

### 1. Manual Approach (`core/simulation_v1.py`)
- Simulates the 99% vs 1% odds by manually creating a 100-element list (99 zeros and one 1).
- Loops through the list and rolls a standard dice based on custom conditions.

### 2. Vectorized & Optimized (`core/simulation_v2.py`)
- Uses NumPy's probabilistic capabilities (`np.random.choice` with a `p` parameter).
- Provides a cleaner, more readable, and faster simulation structure.

### 3. Interactive Web App (`app.py`)
- Built with **Streamlit** and **Matplotlib**.
- Imports the core simulation logic to provide a UI with a slider for dynamic testing.
