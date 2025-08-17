import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

# Create save directory
save_dir = os.path.expanduser("~/Desktop/Mandelbrot Zoom")
os.makedirs(save_dir, exist_ok=True)

# Original parameters
pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
p_center, q_center = -0.793191078177363, 0.16093721735804
max_iterations = 300
infinity_border = 10

def mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints,
               max_iterations=300, infinity_border=10):
    image = np.zeros((ppoints, qpoints))
    p, q = np.mgrid[pmin:pmax:(ppoints*1j), qmin:qmax:(qpoints*1j)]
    c = p + 1j*q
    z = np.zeros_like(c)
    for k in range(max_iterations):
        z = z**2 + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k
        z[mask] = np.nan
    return -image.T

# Create 60 zoom levels (30 in, 30 out)
zoom_levels = np.concatenate([
    np.geomspace(1/30000, 1/1000, 30),  # Zoom in
    np.geomspace(1/1000, 3, 30)          # Zoom out
])

plt.ioff()  # Disable automatic showing

for i, scale in enumerate(tqdm(zoom_levels)):
    # Calculate new bounds
    pmin_ = (pmin - p_center) * scale + p_center
    pmax_ = (pmax - p_center) * scale + p_center
    qmin_ = (qmin - q_center) * scale + q_center
    qmax_ = (qmax - q_center) * scale + q_center
    
    # Render at 800x800 resolution (like original)
    image = mandelbrot(pmin_, pmax_, 800, qmin_, qmax_, 800)
    
    # Create figure with your original style
    fig = plt.figure(figsize=(10, 10))
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image, cmap='flag', interpolation='none')  # Your original style
    
    # Save with sequential numbering
    plt.savefig(f"{save_dir}/mandelbrot_{i:03d}.png", 
               bbox_inches='tight', pad_inches=0, dpi=100)
    plt.close(fig)

print(f"Saved 60 images to {save_dir}")