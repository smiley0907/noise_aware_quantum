# ============================================================
# CELL 6 — MEASUREMENT ERROR MITIGATION SETUP
# ============================================================

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import ReadoutError

# Calibration storage
calibration_matrices = {}

for n in QUBIT_SIZES:
    # Single-qubit calibration matrix
    calibration_circuit_0 = QuantumCircuit(1, 1)
    calibration_circuit_0.measure(0, 0)

    calibration_circuit_1 = QuantumCircuit(1, 1)
    calibration_circuit_1.x(0)
    calibration_circuit_1.measure(0, 0)

    calibration_matrices[n] = {
        "zero_state": calibration_circuit_0,
        "one_state": calibration_circuit_1
    }

    print(f"{n} qubits -> measurement calibration prepared")

print("\nMeasurement mitigation calibration prepared successfully.")
