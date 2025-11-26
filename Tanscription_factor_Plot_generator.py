import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ======================
# Font Setup
# ======================
rcParams['font.family'] = 'Times New Roman'

# ======================
# Load TF Data (2-column file: Gene_ID    TF_Family)
# ======================
tf = pd.read_csv("TF.tsv", sep="\t", header=None)
tf.columns = ["Gene_ID", "TF_Family"]

# ======================
# Count TF families
# ======================
tf_count = tf.groupby("TF_Family").size().reset_index(name="Count") \
             .sort_values("Count", ascending=False)

# ======================
# Bar plot: ALL TF families
# ======================
plt.figure(figsize=(12, 10))
plt.barh(tf_count["TF_Family"], tf_count["Count"], color="mediumseagreen")
plt.gca().invert_yaxis()
plt.title("Transcription Factor Families", fontsize=18)
plt.xlabel("Gene Count", fontsize=14)
plt.ylabel("TF Family", fontsize=14)
plt.tight_layout()
plt.show()

# ======================
# Pie chart: ALL TF families
# ======================
plt.figure(figsize=(8, 8))
plt.pie(tf_count["Count"], labels=tf_count["TF_Family"],
        autopct="%1.1f%%", startangle=140)
plt.title("TF Family Distribution", fontsize=18)
plt.tight_layout()
plt.show()
