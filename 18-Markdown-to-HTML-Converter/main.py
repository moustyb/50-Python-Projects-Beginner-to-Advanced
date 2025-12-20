# main.py
import re

def convert_line(line):
    line = line.rstrip("\n")

    # Headings
    if line.startswith("### "):
        return f"<h3>{line[4:]}</h3>"
    elif line.startswith("## "):
        return f"<h2>{line[3:]}</h2>"
    elif line.startswith("# "):
        return f"<h1>{line[2:]}</h1>"

    # Bold: **text**
    line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)

    # Italic: *text*
    line = re.sub(r"\*(.*?)\*", r"<i>\1</i>", line)

    # Paragraph
    if line.strip():
        return f"<p>{line}</p>"
    return ""

def convert_markdown(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as md:
            lines = md.readlines()

        html_lines = [convert_line(line) for line in lines]

        with open(output_file, "w", encoding="utf-8") as html:
            html.write("<html><body>\n")
            html.write("\n".join(html_lines))
            html.write("\n</body></html>")

        print(f"✅ Converted to {output_file}")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("Error:", e)

def main():
    print("🗂️ Markdown to HTML Converter")
    input_file = input("Enter input .md file path: ").strip()
    output_file = input("Enter output .html file path: ").strip()
    convert_markdown(input_file, output_file)

if __name__ == "__main__":
    main()
