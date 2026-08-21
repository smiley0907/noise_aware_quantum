# ============================================================
# CELL 1 — ENVIRONMENT AND EXPERIMENT CONFIGURATION
# ============================================================

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Experimental configurations
QUBIT_SIZES = [3, 5, 7, 9, 11]
SHOTS = 1024

# Controlled depolarizing noise probabilities
NOISE_LEVELS = [0.001, 0.005, 0.010, 0.020]

# Repeated execution configuration
WARMUP_RUNS = 2
MEASUREMENT_RUNS = 10

# Simulator
SIMULATOR_NAME = "aer_simulator"
simulator = AerSimulator()

print("Environment initialized successfully.")
print(f"Qubit sizes: {QUBIT_SIZES}")
print(f"Shots: {SHOTS}")
print(f"Noise levels: {NOISE_LEVELS}")
print(f"Warm-up runs: {WARMUP_RUNS}")
print(f"Measurement runs: {MEASUREMENT_RUNS}")
print(f"Simulator: {SIMULATOR_NAME}")
