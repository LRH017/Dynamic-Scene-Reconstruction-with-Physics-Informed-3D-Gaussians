import cv2
import numpy as np
import os

# --- Please modify the paths below ---
path_base = "output/mutant_baseline/test/ours_40000/renders/00000.png"
path_ours = "output/mutant_final/test/ours_40000/renders/00000.png"
# -------------------------------------

if not os.path.exists(path_base) or not os.path.exists(path_ours):
    print("Error: Image files not found. Check your paths!")
    exit()

img_base = cv2.imread(path_base)
img_ours = cv2.imread(path_ours)

# Define cropping region (y, x, size)
# For the mutant dataset, you may need to adjust these coordinates 
# to find the best area showing the "artifacts" or details.
crop_y, crop_x = 300, 500  # Starting coordinates
size = 150                 # Crop size (150x150)

# Crop and zoom in (2x magnification)
patch_base = img_base[crop_y:crop_y+size, crop_x:crop_x+size]
patch_base = cv2.resize(patch_base, (0,0), fx=2, fy=2)

patch_ours = img_ours[crop_y:crop_y+size, crop_x:crop_x+size]
patch_ours = cv2.resize(patch_ours, (0,0), fx=2, fy=2)

# Add a red border for Baseline and a green border for Ours
# (B, G, R) format: Red is (0, 0, 255), Green is (0, 255, 0)
cv2.rectangle(patch_base, (0,0), (size*2-1, size*2-1), (0,0,255), 5)
cv2.rectangle(patch_ours, (0,0), (size*2-1, size*2-1), (0,255,0), 5)

# Overlay the zoomed patches onto the bottom-right corner of the original images
h, w, _ = img_base.shape
# Overlay Baseline patch
img_base[h-size*2:h, w-size*2:w] = patch_base
# Overlay Ours patch
img_ours[h-size*2:h, w-size*2:w] = patch_ours

# Concatenate images horizontally and save
combined = np.hstack((img_base, img_ours))
cv2.imwrite("vis_zoom.png", combined)
print("✅ Zoom-in comparison image generated: vis_zoom.png")