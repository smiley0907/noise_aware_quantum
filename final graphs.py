# ============================================================
# CELL 10 — FINAL GRAPHS
# ============================================================

# ------------------------------------------------------------
# Figure 1 — Computational Distribution Fidelity
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

for n in QUBIT_SIZES:
    subset = final_results[final_results["Qubits"] == n]

    plt.plot(
        subset["Noise_Level"],
        subset["NPC_Fidelity"],
        marker="o",
        label=f"{n}Q NPC"
    )

    plt.plot(
        subset["Noise_Level"],
        subset["NMC_Fidelity"],
        marker="s",
        linestyle="--",
        label=f"{n}Q NMC"
    )

plt.xlabel("Noise Level")
plt.ylabel("Computational Distribution Fidelity")
plt.title("Computational Distribution Fidelity Under Increasing Noise")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Figure 2 — Fidelity Recovery
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

for noise_level in NOISE_LEVELS:
    subset = final_results[
        final_results["Noise_Level"] == noise_level
    ]

    plt.plot(
        subset["Qubits"],
        subset["Fidelity_Recovery_Percent"],
        marker="o",
        label=f"Noise = {noise_level}"
    )

plt.axhline(0, linestyle="--")

plt.xlabel("Qubit Configuration")
plt.ylabel("Fidelity Recovery (%)")
plt.title("Fidelity Recovery Across Qubit Configurations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Figure 3 — Error Rate
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

for noise_level in NOISE_LEVELS:
    subset = final_results[
        final_results["Noise_Level"] == noise_level
    ]

    plt.plot(
        subset["Qubits"],
        subset["NPC_Error_Rate_Percent"],
        marker="o",
        label=f"NPC, Noise = {noise_level}"
    )

    plt.plot(
        subset["Qubits"],
        subset["NMC_Error_Rate_Percent"],
        marker="s",
        linestyle="--",
        label=f"NMC, Noise = {noise_level}"
    )

plt.xlabel("Qubit Configuration")
plt.ylabel("Error Rate (%)")
plt.title("Noise Induced Error Rate Across Qubit Configurations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("All final graphs generated successfully.")
