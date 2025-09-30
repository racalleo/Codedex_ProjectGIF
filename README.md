#GIF Generator with Python 🖼️➡️🎞️

A lightweight Python script that generates GIFs from multiple images with just a few lines of code.
Using os and imageio.v3, it reads PNG frames, validates their existence, and stitches them together into a smooth animation at 500ms per frame.

Simple, efficient, and beginner-friendly! ✨
📦 Features
📂 Reads PNG images directly from your project folder.
✅ Verifies if files exist before processing.
⏱️ Customizable frame duration (default: 500ms).
🔁 Exports a looping GIF automatically.
🧩 Written in clear, minimal Python code for easy learning.

🛠️ Installation
Clone this repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Install the required dependency:
pip install imageio
(The script also uses Python’s built-in os module, which requires no installation.)

▶️ Usage
Place your image frames (frame1.png, frame2.png, frame3.png, …) in the project folder.
Run the script:
python create_gif.py

If the frames exist, a GIF named kickingrock.gif will be created in the same folder.

📂 Example
Input files:
frame1.png
frame2.png
frame3.png
frame4.png

Output:
✅ GIF successfully created in <your project path>

Result:
A looping GIF with 500ms per frame.