import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Font setup
rcParams['font.family'] = 'Times New Roman'

# Load file
df = pd.read_csv("PATHWAY.tsv", sep="\t")

# ===== Top 20 Pathways =====
path_count = df.groupby("Pathway").size().reset_index(name="Count") \
               .sort_values("Count", ascending=False).head(20)

plt.figure(figsize=(10,8))
plt.barh(path_count["Pathway"], path_count["Count"], color="steelblue")
plt.gca().invert_yaxis()
plt.title("Top 20 KEGG Pathways", fontsize=18)
plt.xlabel("Gene Count", fontsize=14)
plt.tight_layout()
plt.show()

# ===== Top 20 Pathway Functions =====
func_count = df.groupby("Pathway Function").size().reset_index(name="Count") \
                .sort_values("Count", ascending=False).head(20)

plt.figure(figsize=(10,8))
plt.barh(func_count["Pathway Function"], func_count["Count"], color="darkorange")
plt.gca().invert_yaxis()
plt.title("Top 20 KEGG Functional Categories", fontsize=18)
plt.xlabel("Gene Count", fontsize=14)
plt.tight_layout()
plt.show()
