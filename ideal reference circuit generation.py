# ============================================================
# CELL 2 — IDEAL REFERENCE CIRCUIT (IRC) GENERATION
# ============================================================

ideal_reference_circuits = {}

for n in QUBIT_SIZES:
    qc = QuantumCircuit(n)

    # Grover-style search circuit
    qc.h(range(n))

    # Oracle
    qc.cz(0, n - 1)

    # Diffusion operator
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)
    qc.x(range(n))
    qc.h(range(n))

    ideal_reference_circuits[n] = qc

    print(f"{n} qubits -> IRC generated")

print("\nAll Ideal Reference Circuits generated successfully.")
