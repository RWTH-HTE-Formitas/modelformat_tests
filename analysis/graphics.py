import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns;
sns.set()

org_size = [2.6, 18.1, 125, 19.4, 18.2, 32.1, 527.5]

obj_sizes = [2.5, 25.7, 861, 63, 52.8, 3100, -1]
obj_gltf_sizes = [1.5, 17.2, -1, 23.1, 30.5, 25.8, -1]
obj_gltf_trimmed = [1.5, 17.2, -1, 23.1, 30.5, 25.8, -1]

dae_sizes = [2.3, 27.1, 784.2, 33.1, 60.8, 52.5, 2532]
dae_gltf = [1.6, 19.6, 302.5, 22.7, 21.7, 20.6, 1332]
dae_gltf_trimmed = [1.5, 18.1, 295.8, 22.1, 21.3, 20.4, -1]

dae_gltf_load = [0.14, 1.22, 18.33, 0.86, 1.05, 1.33, 25.3]

data_size = np.zeros((6,7))
data_size[0] = np.divide(obj_sizes, org_size)
data_size[1] = np.divide(obj_gltf_sizes, org_size)
data_size[2] = np.divide(obj_gltf_trimmed, org_size)
data_size[3] = np.divide(dae_sizes, org_size)
data_size[4] = np.divide(dae_gltf, org_size)
data_size[5] = np.divide(dae_gltf_trimmed, org_size)

data_size[data_size < 0] = float('inf')
yLabels = ["obj", "obj2gltf", "obj2gltf_trimmed", "dae", "dae2gltf", "dae2gltf_trimmed"]
ax = sns.heatmap(data_size, annot=True, vmin=0, vmax=3, cmap="summer", yticklabels=yLabels)
plt.xlabel("model id")
plt.ylabel("data format")
plt.tight_layout()
plt.savefig("heatmap.pdf")

print(data_size)
