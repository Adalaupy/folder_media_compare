import tkinter as tk
from process import *


class TextEditor:
    
    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Text Editor")
        self.window.geometry("1200x800")
        self.window.resizable(True, True)

        self.text_frame = tk.Frame(self.window)

        self.heading_label = tk.Label(self.text_frame, text="Photo Transfer from Phone to computer", font=("Helvetica", 18, "bold"))
        self.heading_label.pack(pady=10)

        self.heading_label2 = tk.Label(self.text_frame, text="You can input more than 1 directory by starting a new line", font=("Helvetica", 12))
        self.heading_label2.pack(pady=10)        

        self.text_widget1_frame = tk.Frame(self.text_frame)
        self.text_widget1_title = tk.Label(self.text_widget1_frame, text="Path of mobile phone", font=("Helvetica", 14, "bold"))
        self.text_widget1_title.pack(pady=5)
        self.text_widget1 = tk.Text(self.text_widget1_frame, font=("Helvetica", 12), height=10, width=50, wrap=tk.WORD)
        
        
        #        
        self.text_widget1.insert(1.0,r"""""".strip())
        
        
        self.text_widget1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.text_widget1_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.text_widget2_frame = tk.Frame(self.text_frame)
        self.text_widget2_title = tk.Label(self.text_widget2_frame, text="Path of local Computer", font=("Helvetica", 14, "bold"))
        self.text_widget2_title.pack(pady=5)
        self.text_widget2 = tk.Text(self.text_widget2_frame, font=("Helvetica", 12), height=10, width=50, wrap=tk.WORD)
        #
        self.text_widget2.insert(1.0,r"""""".strip())
        
        self.text_widget2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.text_widget2_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.text_frame.pack_propagate(False)

        self.button_frame = tk.Frame(self.window)
        self.close_button = tk.Button(self.button_frame, text="Submit", font=("Helvetica", 12, "bold"), command=self.close_window)
        self.close_button.pack(pady=10)

        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

    
    def show_text(self):

        self.window.mainloop()

    def close_window(self):    


        self.path_from = self.text_widget1.get("1.0", tk.END)
        self.path_to = self.text_widget2.get("1.0", tk.END)
        

        Process(self.path_from,self.path_to)
        
        
        self.window.destroy()

if __name__ == "__main__":
    
    editor = TextEditor()
    editor.show_text()
    
