import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("1200x700")  # Set window size to 8" by 8" (600x600 pixels)

        # Create a custom style for buttons with a black background and white text
        self.style = ttk.Style()
        self.style.configure("Custom.TButton", background="black", foreground="white")
        self.style.configure("Flashcard.TLabel", background="yellow", foreground="black", font=("Arial", 24))

        self.flashcards = []
        self.current_card = 0
        self.correct_answers = 0
        self.wrong_answers = 0

        # Create GUI elements
        self.card_frame = ttk.Frame(root)
        self.card_frame.grid(row=0, padx=20, pady=20, sticky="nsew")
        self.card_frame.grid_rowconfigure(0, weight=1)
        self.card_frame.grid_columnconfigure(0, weight=1)

        self.front_label = ttk.Label(
            self.card_frame, text="", font=("Arial", 24), style="Flashcard.TLabel"
        )
        self.front_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.back_label = ttk.Label(
            self.card_frame, text="", font=("Arial", 24), style="Flashcard.TLabel"
        )
        self.back_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.back_label.grid_remove()

        self.show_back_button = ttk.Button(
            root, text="Show Back", command=self.show_back, style="Custom.TButton"
        )
        self.correct_button = ttk.Button(
            root, text="Correct", command=self.mark_correct, style="Custom.TButton"
        )
        self.wrong_button = ttk.Button(
            root, text="Wrong", command=self.mark_wrong, style="Custom.TButton"
        )
        self.skip_button = ttk.Button(
            root, text="Skip", command=self.next_card, style="Custom.TButton"
        )

        self.show_back_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.correct_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.wrong_button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.skip_button.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

        # Load flashcards from a file
        self.load_flashcards("flashcards.txt")

        # Initialize the first flashcard
        self.show_front()

    def load_flashcards(self, file_name):
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(" - ")
                    if len(parts) == 2:
                        self.flashcards.append((parts[0], parts[1]))
        except FileNotFoundError:
            print("File not found")

    def show_front(self):
        if self.current_card < len(self.flashcards):
            self.back_label.grid_remove()
            self.front_label.grid()
            self.front_label.config(text=self.flashcards[self.current_card][0])
        else:
            self.show_result()

    def show_back(self):
        if self.current_card < len(self.flashcards):
            self.front_label.grid_remove()
            self.back_label.grid()
            self.back_label.config(text=self.flashcards[self.current_card][1])
        else:
            self.show_result()

    def mark_correct(self):
        if self.current_card < len(self.flashcards):
            self.correct_answers += 1
            self.next_card()

    def mark_wrong(self):
        if self.current_card < len(self.flashcards):
            self.wrong_answers += 1
            self.next_card()

    def next_card(self):
        if self.current_card < len(self.flashcards):
            self.current_card += 1
            self.show_front()
        else:
            self.show_result()

    def show_result(self):
        self.front_label.grid_remove()
        self.back_label.grid_remove()

        result_message = f"Correct: {self.correct_answers}, Wrong: {self.wrong_answers}"
        messagebox.showinfo("Result", result_message)

def main():
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
