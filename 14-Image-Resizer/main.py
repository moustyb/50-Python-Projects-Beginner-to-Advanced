# main.py
from PIL import Image

def resize_image(input_path, output_path, width, height):
    try:
        img = Image.open(input_path)
        resized = img.resize((width, height))
        resized.save(output_path)
        print(f"Image saved to {output_path}")
    except Exception as e:
        print("Error:", e)

def main():
    print("🖼️ Image Resizer")
    input_path = input("Enter path to image: ").strip()
    output_path = input("Enter output path (e.g., resized.jpg): ").strip()
    try:
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))
        resize_image(input_path, output_path, width, height)
    except ValueError:
        print("Width and height must be integers.")

if __name__ == "__main__":
    main()
