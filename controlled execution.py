# ============================================================
# CELL 7 — CONTROLLED EXECUTION
# ============================================================

execution_results = {
    "IRC": {},
    "NPC": {},
    "Calibration": {}
}

# ------------------------------------------------------------
# Ideal Reference Circuit execution
# ------------------------------------------------------------

for n, qc in ideal_reference_circuits.items():
    measured_qc = qc.copy()
    measured_qc.measure_all()

    result = simulator.run(
        measured_qc,
        shots=SHOTS
    ).result()

    execution_results["IRC"][n] = result.get_counts()

    print(f"IRC -> {n} qubits executed")


# ------------------------------------------------------------
# Noise Perturbed Circuit execution
# ------------------------------------------------------------

for noise_level in NOISE_LEVELS:
    execution_results["NPC"][noise_level] = {}

    for n, qc in noise_perturbed_circuits[noise_level].items():
        measured_qc = qc.copy()
        measured_qc.measure_all()

        result = simulator.run(
            measured_qc,
            noise_model=noise_models[noise_level],
            shots=SHOTS
        ).result()

        execution_results["NPC"][noise_level][n] = result.get_counts()

        print(
            f"NPC -> noise {noise_level} -> "
            f"{n} qubits executed"
        )


# ------------------------------------------------------------
# Calibration execution
# ------------------------------------------------------------

for n in QUBIT_SIZES:
    execution_results["Calibration"][n] = {}

    for state in [0, 1]:
        calibration_qc = QuantumCircuit(1, 1)

        if state == 1:
            calibration_qc.x(0)

        calibration_qc.measure(0, 0)

        result = simulator.run(
            calibration_qc,
            noise_model=noise_models[0.01],
            shots=SHOTS
        ).result()

        execution_results["Calibration"][n][state] = (
            result.get_counts()
        )

    print(f"Calibration -> {n} qubits executed")


print("\nControlled execution completed successfully.")
