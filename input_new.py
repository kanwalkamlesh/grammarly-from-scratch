def launch_text_input_gui():
    def on_submit():
        user_text = text_box.get("1.0", tk.END).strip()
        print("User entered:\n", user_text)
        root.destroy()

    root = tk.Tk()
    root.title("AI Writing Assistant")

    text_box = tk.Text(root, height=10, width=60)
    text_box.pack(padx=10, pady=10)

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=5)

    root.mainloop()