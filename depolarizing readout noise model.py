# ============================================================
# CELL 4 — DEPOLARIZING + READOUT NOISE MODEL
# ============================================================

from qiskit_aer.noise import NoiseModel, depolarizing_error, ReadoutError

noise_models = {}

for noise_level in NOISE_LEVELS:
    noise_model = NoiseModel()

    # Gate errors
    single_qubit_error = depolarizing_error(noise_level, 1)
    two_qubit_error = depolarizing_error(noise_level, 2)

    noise_model.add_all_qubit_quantum_error(
        single_qubit_error, ["h", "x"]
    )

    noise_model.add_all_qubit_quantum_error(
        two_qubit_error, ["cz", "mcx"]
    )

    # Readout error
    readout_error = ReadoutError([
        [1 - noise_level, noise_level],
        [noise_level, 1 - noise_level]
    ])

    noise_model.add_all_qubit_readout_error(readout_error)

    noise_models[noise_level] = noise_model

    print(f"Noise level {noise_level} -> gate + readout model configured")

print("\nAll combined noise models configured successfully.")
