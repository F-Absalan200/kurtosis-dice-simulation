import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from core.simulation_v2 import run_dice_simulation 

st.title("🎲 Dice Game Paradox & Kurtosis")

iterations = st.slider("Number of iterations:", 100, 100000, 50000, step=500)

if st.button("Run Simulation"):
    cash_seq = run_dice_simulation(num_simulations=iterations)
    final_cash = cash_seq[-1]
    
    st.metric("Final Capital", f"${final_cash}")
    
    fig, ax = plt.subplots()
    ax.plot(cash_seq, color='crimson')
    ax.set_xlabel("Steps")
    ax.set_ylabel("Cash")
    ax.grid(True, linestyle='--', alpha=0.5)
    
    st.pyplot(fig)