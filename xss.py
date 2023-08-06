import tkinter as tk

def on_button_click():
    url = entry.get()
    if url.strip():
        if "xss" in url.lower():
            result_label.config(text="Enjoy")
        else:
            result_label.config(text="No XSS detected.")
    else:
        result_label.config(text="Please enter a valid URL.")

# Create the main application window
root = tk.Tk()
root.title("XSS Scanner")
root.geometry("400x150")

# Create and configure the UI elements
button = tk.Button(root, text="Scan", bg="yellow", command=on_button_click)
button.pack(pady=20)

entry = tk.Entry(root, width=40)
entry.pack()

result_label = tk.Label(root, text="Enter URL for scanning XSS", font=("Arial", 12))
result_label.pack(pady=20)

# Start the application
root.mainloop()
