# ============================================================
# CELL 5 — NOISE PERTURBED CIRCUIT (NPC) GENERATION
# ============================================================

noise_perturbed_circuits = {}

for noise_level in NOISE_LEVELS:
    noise_perturbed_circuits[noise_level] = {}

    for n, qc in ideal_reference_circuits.items():
        npc = qc.copy()

        noise_perturbed_circuits[noise_level][n] = npc

        print(
            f"Noise {noise_level} -> "
            f"{n} qubits -> NPC generated"
        )

print("\nAll Noise Perturbed Circuits generated successfully.")
