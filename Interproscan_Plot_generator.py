##########################################
### Interproscan Annotation Plotter ######
##########################################

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Set font
rcParams['font.family'] = 'Times New Roman'

df = pd.read_csv("function_output.tsv", sep="\t", header=None)
df.columns = [
    "Protein", "MD5", "Length", "Analysis", "Signature",
    "Sig_Desc", "Start", "End", "Score", "Status",
    "Date", "IPR_ID", "IPR_Desc", "GO", "Pathway"
]

df_unique = df.drop_duplicates(subset=["Protein", "IPR_ID", "Signature"], keep="first")

# ===== Top 20 InterPro domains =====
ipr = df_unique[df_unique["IPR_ID"] != "-"] \
    .groupby("IPR_Desc").size().reset_index(name="Count") \
    .sort_values("Count", ascending=False).head(20)

plt.figure(figsize=(10,8))
plt.barh(ipr["IPR_Desc"], ipr["Count"], color="steelblue")
plt.gca().invert_yaxis()
plt.title("Top 20 InterPro Domains", fontsize=18)
plt.xlabel("Frequency")
plt.tight_layout()
plt.show()

# ===== Top 20 Pfam =====
pfam = df_unique[df_unique["Analysis"] == "Pfam"] \
    .groupby("Sig_Desc").size().reset_index(name="Count") \
    .sort_values("Count", ascending=False).head(20)

plt.figure(figsize=(10,7))
plt.barh(pfam["Sig_Desc"], pfam["Count"], color="darkorange")
plt.gca().invert_yaxis()
plt.title("Top 20 Pfam Domains", fontsize=18)
plt.xlabel("Frequency")
plt.tight_layout()
plt.show()

# ===== Top 20 Sites =====
sites = df_unique[df_unique["IPR_Desc"].str.contains("site", case=False, na=False)] \
    .groupby("IPR_Desc").size().reset_index(name="Count") \
    .sort_values("Count", ascending=False).head(20)

plt.figure(figsize=(10,7))
plt.barh(sites["IPR_Desc"], sites["Count"], color="purple")
plt.gca().invert_yaxis()
plt.title("Top 20 InterPro Sites", fontsize=18)
plt.xlabel("Frequency")
plt.tight_layout()
plt.show()

# ===== Top 20 Analysis (Database sources) =====
analysis = df_unique.groupby("Analysis").size().reset_index(name="Count") \
    .sort_values("Count", ascending=False).head(20)

plt.figure(figsize=(10,5))
plt.bar(analysis["Analysis"], analysis["Count"],
        color=["tomato","mediumseagreen","dodgerblue","orchid","gold"])
plt.xticks(rotation=60)
plt.title("Annotation Databases", fontsize=18)
plt.ylabel("Count")
plt.tight_layout()
plt.show()
