import tkinter as tk

def determine_recyclability(textiles):
    recyclable_textiles = ["cotton", "linen", "silk", "wool"]
    non_recyclable_textiles = ["polyester", "nylon", "acrylic", "polypropylene", "elastane", "aramid fibers"]

    result = ""
    for textile, percentage in textiles.items():
        if textile.lower() in recyclable_textiles and percentage >= 50:
            result += f"{textile}: Recyclable\n"
        elif textile.lower() in non_recyclable_textiles and percentage >= 50:
            result += f"{textile}: Not recyclable\n"
        else:
            result += f"{textile}: Not determined\n"

    return result

def process_textiles():
    input_text = text_entry.get("1.0", tk.END)
    input_lines = input_text.strip().split("\n")
    textiles = {}

    for line in input_lines:
        textile, percentage = line.split(":")
        textiles[textile.strip()] = int(percentage.strip())

    result = determine_recyclability(textiles)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


# Create GUI window
window = tk.Tk()
window.title("Cloth Recyclability")
window.geometry("400x300")

# Create input label and text entry
input_label = tk.Label(window, text="Enter textiles and percentages (one per line):")
input_label.pack()
text_entry = tk.Text(window, height=10, width=40)
text_entry.pack()

# Create process button
process_button = tk.Button(window, text="Process", command=process_textiles)
process_button.pack()

# Create output label and text box
output_label = tk.Label(window, text="Recyclability Results:")
output_label.pack()
output_text = tk.Text(window, height=10, width=40)
output_text.pack()

# Start the GUI event loop
window.mainloop()
