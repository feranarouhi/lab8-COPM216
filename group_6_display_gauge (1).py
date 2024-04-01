import tkinter as tk


class TemperatureDisplayGauge(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.temperature = tk.DoubleVar()
        self.init_ui()

    def init_ui(self):
        self.master.title("Temperature Display (Gauge)")
        self.pack(fill=tk.BOTH, expand=True)

        self.temperature.set(25.0)  # Initial temperature value

        tk.Label(self, text="Indoor Temperature").pack(pady=5)

        # Additional information
        tk.Label(self, text="Units: °C").pack()
        tk.Label(self, text="Low Value: 10°C").pack()
        tk.Label(self, text="Normal Range: 10°C - 30°C").pack()
        tk.Label(self, text="High Value: 30°C").pack()

        self.temperature_gauge = tk.Canvas(self, bg='white', width=200, height=200)
        self.temperature_gauge.pack(pady=10)
        self.update_temperature_gauge()

        tk.Label(self, text="Set Temperature:").pack(pady=5)
        self.temperature_entry = tk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.pack(pady=5)

        tk.Button(self, text="Update", command=self.update_temperature_gauge).pack()

    def update_temperature_gauge(self):
        self.temperature_gauge.delete("all")
        temperature_value = self.temperature.get()

        # Cap temperature value at maximum allowed value (30°C)
        temperature_value = min(temperature_value, 30)

        # Calculate angle for the temperature value
        angle = (temperature_value - 10) * 9  # Adjusting angle for better visualization

        # Draw gauge background
        self.temperature_gauge.create_arc(10, 10, 190, 190, start=0, extent=180, fill='lightblue', outline='black')

        # Draw temperature gauge arc
        self.temperature_gauge.create_arc(10, 10, 190, 190, start=0, extent=angle, fill='blue', outline='black')

        # Display temperature value
        self.temperature_gauge.create_text(100, 100, text=f"{temperature_value}°C", font=("Arial", 12, "bold"))


def main():
    root = tk.Tk()
    TemperatureDisplayGauge(root)
    root.mainloop()


if __name__ == "__main__":
    main()
