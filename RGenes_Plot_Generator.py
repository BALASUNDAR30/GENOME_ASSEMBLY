import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'Times New Roman'

# read whitespace-separated file
res = pd.read_csv("RG.tsv", sep=r"\s+", engine="python")
res.columns = ["Class", "Combined Subclass", "Gene"]

# Count by Class
class_count = res.groupby("Class").size().reset_index(name="Count") \
                 .sort_values("Count", ascending=False)

plt.figure(figsize=(10, 7))
plt.barh(class_count["Class"], class_count["Count"], color="royalblue")
plt.gca().invert_yaxis()
plt.title("Resistance Gene Classes", fontsize=18)
plt.xlabel("Gene Count")
plt.tight_layout()
plt.show()

# Count by Combined Subclass
subclass_count = res.groupby("Combined Subclass").size().reset_index(name="Count") \
                    .sort_values("Count", ascending=False)

plt.figure(figsize=(12, 8))
plt.barh(subclass_count["Combined Subclass"], subclass_count["Count"], color="crimson")
plt.gca().invert_yaxis()
plt.title("Resistance Gene Subclasses", fontsize=18)
plt.xlabel("Gene Count")
plt.tight_layout()
plt.show()

