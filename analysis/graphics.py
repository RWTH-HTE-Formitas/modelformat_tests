import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns;
sns.set()

org_size = [2.6, 18.1, 125, 19.4, 18.2, 32.1, 527.5]

obj_sizes = [2.5, 25.7, 861, 63, 52.8, 3100, -1]
obj_gltf_sizes = [1.5, 17.2, -1, 23.1, 30.5, 25.8, -1]
obj_gltf_trimmed = [1.5, 17.2, -1, 23.1, 30.5, 25.8, -1]

obj_glb_sizes = [1.1, 12.3, -1, 17.1, 22.7, 19.3, -1]

dae_sizes = [2.3, 27.1, 784.2, 33.1, 60.8, 52.5, 1440]
dae_gltf = [1.6, 19.6, 302.5, 22.7, 21.7, 20.6, 403.8]
dae_gltf_trimmed = [1.5, 18.1, 295.8, 22.1, 21.3, 20.4, 387]

dae_glb_sizes = [1.1, 12.4, 216.1, 16.2, 15.6, 15.1, 264.2]

obj_gltf_load = [0.14, 1.72, 0, 1.64, 1.66, 1.56, 0]
obj_gltf_load_trimmed = [0.14, 1.72, 0, 1.62, 1.66, 1.56, 0]

dae_gltf_load = [0.14, 1.47, 20.08, 1.13, 1.80, 1.43, 27.8]
dae_gltf_load_trimmed = [0.14, 1.22, 18.33, 0.86, 1.05, 1.33, 25.3]

obj_glb_load = [0.13, 1.19, 0, 0.89, 0.93, 0.87, 0]
dae_glb_load = [0.11, 1.22, 9.44, 0.94, 0.82, 0.74, 21.89]

data_size = np.zeros((8,7))
data_size[0] = np.divide(obj_sizes, org_size)
data_size[1] = np.divide(obj_gltf_sizes, org_size)
data_size[2] = np.divide(obj_gltf_trimmed, org_size)
data_size[3] = np.divide(dae_sizes, org_size)
data_size[4] = np.divide(dae_gltf, org_size)
data_size[5] = np.divide(dae_gltf_trimmed, org_size)
data_size[6] = np.divide(obj_glb_sizes, org_size)
data_size[7] = np.divide(dae_glb_sizes, org_size)

data_size[data_size < 0] = float('inf')
yLabels = ["obj", "obj2gltf", "obj2gltf_trimmed", "dae", "dae2gltf", "dae2gltf_trimmed", "obj2glb", "dae2glb"]
ax = sns.heatmap(data_size, annot=True, vmin=0, vmax=3, cmap="summer", yticklabels=yLabels)
plt.xlabel("model id")
plt.ylabel("data format")
plt.tight_layout()
plt.savefig("heatmap.pdf")

plt.figure()
plt.plot(range(len(org_size)), obj_gltf_load, "b-.", label = "obj2gltf")
plt.plot(range(len(org_size)), obj_gltf_load_trimmed, "r:", label = "obj2gltf_trimmed")
plt.plot(range(len(org_size)), dae_gltf_load, "y", label = "obj2gltf")
plt.plot(range(len(org_size)), dae_gltf_load_trimmed, "g", label = "dae2gltf_trimmed")
plt.plot(range(len(org_size)), dae_gltf_load_trimmed, "c", label = "dae2gltf_trimmed")
plt.plot(range(len(org_size)), obj_glb_load, "m", label = "obj_glb")
plt.plot(range(len(org_size)), dae_glb_load, "k", label = "dae_glb")
plt.plot([2,6], [0,0], "xb")
plt.plot([2,6], [0,0], "xr")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig("loading_comparison.pdf")
plt.show()

print(data_size)
