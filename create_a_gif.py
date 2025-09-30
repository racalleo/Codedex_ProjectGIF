import os
import imageio.v3 as io

# Source Folder
base_path = os.path.dirname(__file__)

# Pic files
filenames = [
    os.path.join(base_path, "frame1.png"),
    os.path.join(base_path, "frame2.png"),
    os.path.join(base_path, "frame3.png"),
    os.path.join(base_path, "frame4.png")
]

# Read pics
images = []
for f in filenames:
    if os.path.exists(f):
        images.append(io.imread(f))
    else:
        print(f"⚠️ No se encontró: {f}")

# Create GIF only if images were uploaded
if images:
    io.imwrite(os.path.join(base_path, "kickingrock.gif"),
               images, duration=500, loop=0)
    print("✅ GIF successfully created in", base_path)
else:
    print("❌ Could not create GIF (no images found).")
