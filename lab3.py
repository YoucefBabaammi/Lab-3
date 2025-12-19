import tkinter as tk
import string
import random
from PIL import Image, ImageTk
    
def set_background(root , image_path):
    
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((700, 400))
    root.bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=root.bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)


def setup_weights(root):
    """Setup character weights: A=1 to Z=26, 0=27 to 9=36"""
    root.weights = {}
    
    # Letters A-Z = 1-26
    for i, char in enumerate(string.ascii_uppercase):
        root.weights[char] = i + 1
    
    # Digits 0-9 = 27-36
    for i, char in enumerate(string.digits):
        root.weights[char] = 27 + i
    
    root.all_chars = string.ascii_uppercase + string.digits

def create_widgets(root):
    
    """Create simple UI elements"""
    title = tk.Label(
        root,
        text="KEY GENERATOR",
        font=("Arial", 20, "bold"),
        bg='white',
        fg='blue'
    )
    title.pack(pady=20)
    
    tk.Label(
        root,
        text="Generated Key:",
        font=("Arial", 12),
        bg='white'
    ).pack()
    
    root.key_var = tk.StringVar()
    root.key_var.set("XXXX-XXXX-XXXX")
    
    key_display = tk.Entry(
        root,
        textvariable=root.key_var,
        font=("Courier", 14),
        width=20,
        justify='center',
        state='readonly',
        readonlybackground='white'
    )
    key_display.pack(pady=10)
    
    generate_btn = tk.Button(
        root,
        text="Generate Key",
        command=lambda:generate_key(root),
        font=("Arial", 12),
        bg='green',
        fg='white',
        width=15
    )
    generate_btn.pack(pady=20)
    
    info = tk.Label(
        root,
        text="Format: XXXX-XXXX-XXXX\nEach block sum: 30-35",
        font=("Arial", 10),
        bg='white'
    )
    info.pack()

def generate_block(root):
    """Generate one 4-character block with sum 30-35"""
    while True:
        block = ""
        total = 0
        
        for _ in range(4):
            char = random.choice(root.all_chars)
            block += char
            total += root.weights[char]
        
        if 30 <= total <= 35:
            return block, total

def generate_key(root):
    """Generate the full key"""
    blocks = []
    for _ in range(3):
        block, _ = generate_block(root)
        blocks.append(block)
    
    key = "-".join(blocks)
    root.key_var.set(key)
    print(f"Generated: {key}")

# Run the program

def init_gui():
    root = tk.Tk()
    root.title("Simple Key Generator")
    root.geometry("500x400")

    set_background(root, "D:/Python/windows.png")

    setup_weights(root)

    create_widgets(root)

    root.mainloop()


if __name__ == "__main__":
   init_gui()
