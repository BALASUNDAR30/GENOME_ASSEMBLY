import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ---------------------------------------
# Font setup
# ---------------------------------------
rcParams['font.family'] = 'Times New Roman'

# ---------------------------------------
# Load GO TSV file
# ---------------------------------------
go = pd.read_csv("GO.tsv", sep="\t")
go.columns = ["Gene_Name", "GO_ID", "GO_Name", "GO_Annotation", "GO_Aspect"]

# ---------------------------------------
# Bar plot: GO Aspect distribution (BP/MF/CC)
# ---------------------------------------
aspect_counts = go.groupby("GO_Aspect").size().reset_index(name="Count") \
                  .sort_values("Count", ascending=False)

plt.figure(figsize=(8,6))
plt.bar(aspect_counts["GO_Aspect"], aspect_counts["Count"],
        color=["steelblue", "orange", "seagreen"])
plt.title("GO Aspect Distribution", fontsize=18)
plt.ylabel("Gene Count", fontsize=14)
plt.tight_layout()
plt.show()

# ---------------------------------------
# TOP 20 Biological Process (BP)
# ---------------------------------------
bp = go[go["GO_Aspect"] == "biological_process"]
bp_count = bp.groupby("GO_Name").size().reset_index(name="Count") \
             .sort_values("Count", ascending=False).head(20)

plt.figure(figsize=(10,8))
plt.barh(bp_count["GO_Name"], bp_count["Count"], color="tomato")
plt.gca().invert_yaxis()
plt.title("Top 20 Biological Process (BP)", fontsize=18)
plt.xlabel("Gene Count", fontsize=14)
plt.tight_layout()
plt.show()

# ---------------------------------------
# TOP 20 Molecular Function (MF)
# ---------------------------------------
mf = go[go["GO_Aspect"] == "molecular_function"]
mf_count = mf.groupby("GO_Name").size().reset_index(name="Count") \
             .sort_values("Count", ascending=False).head(20)

plt.figure(figsize=(10,8))
plt.barh(mf_count["GO_Name"], mf_count["Count"], color="mediumseagreen")
plt.gca().invert_yaxis()
plt.title("Top 20 Molecular Function (MF)", fontsize=18)
plt.xlabel("Gene Count", fontsize=14)
plt.tight_layout()
plt.show()

# ---------------------------------------
# TOP 20 Cellular Component (CC)
# ---------------------------------------
cc = go[go["GO_Aspect"] == "cellular_component"]
cc_count = cc.groupby("GO_Name").size().reset_index(name="Count") \
             .sort_values("Count", ascending=False).head(20)

plt.figure(figsize=(10,8))
plt.barh(cc_count["GO_Name"], cc_count["Count"], color="royalblue")
plt.gca().invert_yaxis()
plt.title("Top 20 Cellular Component (CC)", fontsize=18)
plt.xlabel("Gene Count", fontsize=14)
plt.tight_layout()
plt.show()
