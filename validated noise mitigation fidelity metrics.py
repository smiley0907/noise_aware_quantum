# ============================================================
# CELL 8 — VALIDATED NOISE MITIGATION + FIDELITY METRICS
# ============================================================

def counts_to_probabilities(counts, num_qubits):
    total = sum(counts.values())
    probabilities = np.zeros(2 ** num_qubits)

    for bitstring, count in counts.items():
        index = int(bitstring.replace(" ", ""), 2)
        probabilities[index] = count / total

    return probabilities


def distribution_fidelity(p, q):
    return np.square(np.sum(np.sqrt(p * q)))


results = []

for noise_level in NOISE_LEVELS:

    # Exact symmetric readout calibration matrix
    readout_matrix = np.array([
        [1 - noise_level, noise_level],
        [noise_level, 1 - noise_level]
    ])

    inverse_matrix = np.linalg.pinv(readout_matrix)

    for n in QUBIT_SIZES:

        # ----------------------------------------------------
        # Ideal Reference distribution
        # ----------------------------------------------------
        ideal_counts = execution_results["IRC"][n]
        p_ideal = counts_to_probabilities(ideal_counts, n)

        # ----------------------------------------------------
        # Noise Perturbed distribution
        # ----------------------------------------------------
        npc_counts = execution_results["NPC"][noise_level][n]
        p_npc = counts_to_probabilities(npc_counts, n)

        # ----------------------------------------------------
        # Noise Mitigation
        # Independent readout-error correction
        # ----------------------------------------------------
        corrected = p_npc.reshape([2] * n)

        for qubit in range(n):
            corrected = np.tensordot(
                inverse_matrix,
                corrected,
                axes=(1, qubit)
            )
            corrected = np.moveaxis(
                corrected,
                0,
                qubit
            )

        p_nmc = corrected.reshape(-1)

        # Numerical stabilization
        p_nmc = np.clip(p_nmc, 0, None)

        if p_nmc.sum() > 0:
            p_nmc = p_nmc / p_nmc.sum()

        # ----------------------------------------------------
        # Fidelity
        # ----------------------------------------------------
        npc_fidelity = distribution_fidelity(
            p_ideal,
            p_npc
        )

        nmc_fidelity = distribution_fidelity(
            p_ideal,
            p_nmc
        )

        # ----------------------------------------------------
        # Fidelity Loss
        # ----------------------------------------------------
        fidelity_loss = (
            1 - npc_fidelity
        ) * 100

        # ----------------------------------------------------
        # Fidelity Recovery
        # ----------------------------------------------------
        if npc_fidelity < 1:
            fidelity_recovery = (
                (nmc_fidelity - npc_fidelity)
                / (1 - npc_fidelity)
            ) * 100
        else:
            fidelity_recovery = 0.0

        # ----------------------------------------------------
        # Error Rate
        # ----------------------------------------------------
        ideal_state = np.argmax(p_ideal)

        npc_error_rate = (
            1 - p_npc[ideal_state]
        ) * 100

        nmc_error_rate = (
            1 - p_nmc[ideal_state]
        ) * 100

        # ----------------------------------------------------
        # Diagnostics
        # ----------------------------------------------------
        results.append({
            "Qubits": n,
            "Noise_Level": noise_level,
            "NPC_Fidelity": npc_fidelity,
            "NMC_Fidelity": nmc_fidelity,
            "Fidelity_Loss_Percent": fidelity_loss,
            "Fidelity_Recovery_Percent": fidelity_recovery,
            "NPC_Error_Rate_Percent": npc_error_rate,
            "NMC_Error_Rate_Percent": nmc_error_rate,
            "NPC_Probability_Sum": p_npc.sum(),
            "NMC_Probability_Sum": p_nmc.sum(),
            "NMC_Min_Probability": p_nmc.min(),
            "NMC_Max_Probability": p_nmc.max(),
            "IRC_Depth": irc_characteristics[n]["Circuit_Depth"],
            "IRC_2Q_Gates": irc_characteristics[n]["Two_Qubit_Gate_Count"]
        })

results_df = pd.DataFrame(results)

print("Validated noise mitigation metrics calculated successfully.")
print(f"Experimental records: {len(results_df)}")
print(
    f"NMC probability range: "
    f"{results_df['NMC_Min_Probability'].min():.6f} "
    f"to "
    f"{results_df['NMC_Max_Probability'].max():.6f}"
)
print(
    f"Maximum normalization deviation: "
    f"{np.max(np.abs(results_df['NMC_Probability_Sum'] - 1)):.10f}"
)
