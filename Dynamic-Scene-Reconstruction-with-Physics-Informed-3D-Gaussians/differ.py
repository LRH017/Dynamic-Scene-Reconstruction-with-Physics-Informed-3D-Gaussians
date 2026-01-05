import cv2
import numpy as np
import os

# Update these paths to match your actual file locations
# Assuming images are rendered in the test/renders directory
path_base = "output/mutant_baseline/test/ours_40000/renders/00000.png"
path_ours = "output/mutant_final/test/ours_40000/renders/00000.png"

if not os.path.exists(path_base) or not os.path.exists(path_ours):
    print("Images not found. Please check the file paths!")
    exit()

img1 = cv2.imread(path_base).astype(np.float32)
img2 = cv2.imread(path_ours).astype(np.float32)

# Calculate the absolute difference and amplify by 10x to make discrepancies visible
diff = np.abs(img1 - img2) * 10
diff = np.clip(diff, 0, 255).astype(np.uint8)

# Save the result
cv2.imwrite("difference_map.png", diff)
print("Difference map generated: difference_map.png")