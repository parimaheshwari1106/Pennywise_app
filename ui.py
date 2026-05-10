# ui.py
import tkinter as tk
from tkinter import messagebox
from expense_manager import ExpenseManager
from trip_planner import TripPlanner

# ---------- MAIN UI ----------
class PennyWiseUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("PennyWise Budget Assistant")
        self.win.geometry("500x650")
        self.win.configure(bg="#f0e6ff")

        self.expense_manager = ExpenseManager()
        self.trip_planner = TripPlanner()

        title = tk.Label(self.win, text="PennyWise", font=("Arial", 28, "bold"),
                         fg="#b30000", bg="#f0e6ff")
        title.pack()

        self.draw_clown()

        btn1 = tk.Button(self.win, text="Expense Tracker",
                         command=self.open_expense_tracker,
                         width=20, height=2, bg="#ffcccc", fg="black")
        btn1.pack(pady=20)

        btn2 = tk.Button(self.win, text="Trip Cost Estimator",
                         command=self.open_trip_planner,
                         width=20, height=2, bg="#ccffcc", fg="black")
        btn2.pack()

        self.win.mainloop()

    # ---------- CLOWN FACE (simple + legal) ----------
    def draw_clown(self):
        canvas = tk.Canvas(self.win, width=300, height=300, bg="#f0e6ff", highlightthickness=0)
        canvas.pack()

        # Face
        canvas.create_oval(50, 40, 250, 240, fill="white", outline="black", width=2)

        # Eyes
        canvas.create_oval(100, 90, 130, 120, fill="black")
        canvas.create_oval(170, 90, 200, 120, fill="black")

        # Nose (red)
        canvas.create_oval(135, 130, 165, 160, fill="red", outline="darkred")

        # Smile
        canvas.create_arc(90, 130, 210, 220, start=0, extent=-180,
                          style=tk.CHORD, outline="red", width=3)

        # Hair (orange)
        canvas.create_oval(20, 40, 90, 160, fill="#ff6600", outline="")
        canvas.create_oval(210, 40, 280, 160, fill="#ff6600", outline="")

    # ---------- EXPENSE TRACKER ----------
    def open_expense_tracker(self):
        win = tk.Toplevel(self.win)
        win.title("Expense Tracker")
        win.geometry("400x450")
        win.configure(bg="#ffe6e6")

        tk.Label(win, text="Add Expense", font=("Arial", 20, "bold"), bg="#ffe6e6").pack()

        tk.Label(win, text="Name:", bg="#ffe6e6").pack()
        name_entry = tk.Entry(win)
        name_entry.pack()

        tk.Label(win, text="Amount:", bg="#ffe6e6").pack()
        amount_entry = tk.Entry(win)
        amount_entry.pack()

        def add():
            n = name_entry.get()
            a = amount_entry.get()

            if n == "" or a == "":
                messagebox.showerror("Error", "Please enter all fields.")
                return

            # convert amount safely
            num = 0
            for ch in a:
                if ch.isdigit():
                    num = num * 10 + int(ch)
                else:
                    messagebox.showerror("Error", "Numbers only.")
                    return

            self.expense_manager.add_expense(n, num)
            messagebox.showinfo("Added", "Expense added successfully.")

        tk.Button(win, text="Add Expense", command=add,
                  bg="#ff9999").pack(pady=10)

        def show_all():
            data = self.expense_manager.get_all_expenses()
            text = ""
            for item in data:
                text = text + item[0] + ": " + str(item[1]) + "\n"
            messagebox.showinfo("Expenses", text)

        tk.Button(win, text="Show All Expenses", command=show_all,
                  bg="#ffcccc").pack(pady=10)

        def show_total():
            total = self.expense_manager.get_total()
            messagebox.showinfo("Total", "Total Expense = " + str(total))

        tk.Button(win, text="Show Total", command=show_total,
                  bg="#ffdddd").pack(pady=10)

    # ---------- TRIP PLANNER ----------
    def open_trip_planner(self):
        win = tk.Toplevel(self.win)
        win.title("Trip Planner")
        win.geometry("400x450")
        win.configure(bg="#e6ffe6")

        tk.Label(win, text="Trip Cost Estimator", font=("Arial", 20, "bold"),
                 bg="#e6ffe6").pack()

        entries = {}

        categories = ["Transport", "Food", "Hotel", "Misc"]

        for c in categories:
            tk.Label(win, text=c + " Cost:", bg="#e6ffe6").pack()
            e = tk.Entry(win)
            e.pack()
            entries[c] = e

        def calculate():
            for c in entries:
                val = entries[c].get()

                if val == "":
                    messagebox.showerror("Error", "Enter all fields.")
                    return

                num = 0
                for ch in val:
                    if ch.isdigit():
                        num = num * 10 + int(ch)
                    else:
                        messagebox.showerror("Error", "Numbers only allowed.")
                        return

                self.trip_planner.set_cost(c, num)

            total = self.trip_planner.calculate_total()
            messagebox.showinfo("Total Trip Cost", str(total))

        tk.Button(win, text="Calculate Total", command=calculate,
                  bg="#ccffcc").pack(pady=20)
