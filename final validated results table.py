# ============================================================
# CELL 9 — FINAL VALIDATED RESULTS TABLE
# ============================================================

final_results = results_df[
    [
        "Qubits",
        "Noise_Level",
        "NPC_Fidelity",
        "NMC_Fidelity",
        "Fidelity_Loss_Percent",
        "Fidelity_Recovery_Percent",
        "NPC_Error_Rate_Percent",
        "NMC_Error_Rate_Percent",
        "IRC_Depth",
        "IRC_2Q_Gates"
    ]
].copy()

display(
    final_results.round({
        "NPC_Fidelity": 6,
        "NMC_Fidelity": 6,
        "Fidelity_Loss_Percent": 3,
        "Fidelity_Recovery_Percent": 3,
        "NPC_Error_Rate_Percent": 3,
        "NMC_Error_Rate_Percent": 3
    })
)

print("\nFinal validated results table generated successfully.")
print(f"Total records: {len(final_results)}")
