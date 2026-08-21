# ============================================================
# CELL 3 — IRC STRUCTURAL CHARACTERIZATION
# ============================================================

irc_characteristics = {}

for n, qc in ideal_reference_circuits.items():
    total_gates = len(qc.data)
    two_qubit_gates = sum(
        1 for instruction in qc.data
        if instruction.operation.num_qubits == 2
    )
    circuit_depth = qc.depth()

    irc_characteristics[n] = {
        "Total_Gate_Count": total_gates,
        "Two_Qubit_Gate_Count": two_qubit_gates,
        "Circuit_Depth": circuit_depth
    }

    print(
        f"{n} qubits -> "
        f"Total Gates: {total_gates}, "
        f"2Q Gates: {two_qubit_gates}, "
        f"Depth: {circuit_depth}"
    )

print("\nIRC structural characterization completed successfully.")
