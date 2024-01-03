import tkinter as tk
from tkinter import messagebox, StringVar

class KursApp:
    def __init__(self, Apk):
        self.Apk = Apk
        self.Apk.title("Konversi Kurs")
        self.Apk.geometry("380x380")
        self.Apk.config(bg="orange")

        # Definisi nilai tukar mata uang
        self.nilaiTukar = {
            'USD': {'EUR': 0.85, 'JPY': 110.25, 'GBP': 0.75, 'IDR': 14000.0},
            'EUR': {'USD': 1.18, 'JPY': 129.71, 'GBP': 0.88, 'IDR': 16920.0},
            'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0068, 'IDR': 164.0},
            'GBP': {'USD': 1.34, 'EUR': 1.13, 'JPY': 147.67, 'IDR': 18998.0},
            'IDR': {'USD': 0.000069, 'EUR': 0.000059, 'JPY': 0.0061, 'GBP': 0.000053}
        }

        self.jumlah_label = tk.Label(Apk, text="Jumlah:", font=("Arial",14), fg="white", bg="orange")
        self.jumlah_entry = tk.Entry(Apk, font=("Arial",14))
        
        self.from_currency_label = tk.Label(Apk, text="Dari Mata Uang", font=("Arial",14), fg="white", bg="orange")
        self.from_currency_var = StringVar()
        self.from_currency_var.set("-")
        self.from_currency_menu = tk.OptionMenu(Apk, self.from_currency_var, *self.nilaiTukar.keys())
        
        self.to_currency_label = tk.Label(Apk, text="Ke", font=("Arial",14), fg="white", bg="orange")
        self.to_currency_var = StringVar()
        self.to_currency_var.set("-")
        self.to_currency_menu = tk.OptionMenu(Apk, self.to_currency_var, *self.nilaiTukar.keys())
        
        self.result_label = tk.Label(Apk, text="Hasil:", font=("Arial",14), fg="white", bg="orange")
        self.result_display = tk.Label(Apk, text="", font=("Helvetica", 16, "bold"), fg="white", bg="orange")
        
        self.convert_button = tk.Button(Apk, text="Konversikan", command=self.konversikanKurs, font=("Arial",14))

        self.jumlah_label.pack(pady=5)
        self.jumlah_entry.pack(pady=5)
        
        self.from_currency_label.pack(pady=5)
        self.from_currency_menu.pack(pady=5)
        
        self.to_currency_label.pack(pady=5)
        self.to_currency_menu.pack(pady=5)
        
        self.result_label.pack()
        self.result_display.pack()
        self.convert_button.pack()

    def konversikanKurs(self):
        try:
            jumlah = float(self.jumlah_entry.get())
            from_currency = self.from_currency_var.get().upper()
            to_currency = self.to_currency_var.get().upper()

            if from_currency == to_currency:
                result = jumlah  # Jika mata uang sumber dan tujuan sama, hasil sama dengan jumlah input
            else:
                exchange_rate = self.nilaiTukar.get(from_currency, {}).get(to_currency)
                if exchange_rate is not None:
                    result = jumlah * exchange_rate
                else:
                    raise ValueError("Belum dipilih")

            self.result_display.config(text=f"{result:.2f} {to_currency}")
        except ValueError as e:
            messagebox.showerror("Kocag lu belum isi semua", str("Jumlah masih kosong atau mata uang masih '' - ''"))

if __name__ == "__main__":
    root = tk.Tk()
    app = KursApp(root)
    root.mainloop()