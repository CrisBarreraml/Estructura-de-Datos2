import tkinter as tk
from tkinter import messagebox

class PilaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Pila (Stack)")
        self.root.geometry("400x500")
        self.root.configure(bg="#F5F5F5")

        self.pila = []  
        self.max_altura = 10  

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        frame_botones = tk.Frame(root, bg="#F5F5F5")
        frame_botones.pack(pady=5)

        self.btn_push = tk.Button(frame_botones, text="Push", command=self.push, width=10, bg="#4CAF50", fg="white")
        self.btn_push.grid(row=0, column=0, padx=5)

        self.btn_pop = tk.Button(frame_botones, text="Pop", command=self.pop, width=10, bg="#F44336", fg="white")
        self.btn_pop.grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root, width=200, height=350, bg="white")
        self.canvas.pack(pady=20)

        self.dibujar_pila()

    def push(self):
        valor = self.entry.get()
        if valor == "":
            messagebox.showwarning("Atención", "Ingrese un valor para apilar")
            return
        if len(self.pila) >= self.max_altura:
            messagebox.showerror("Error", "La pila está llena")
            return
        self.pila.append(valor)
        self.entry.delete(0, tk.END)
        self.dibujar_pila()

    def pop(self):
        if not self.pila:
            messagebox.showerror("Error", "La pila está vacía")
            return
        self.pila.pop()
        self.dibujar_pila()

    def dibujar_pila(self):
        self.canvas.delete("all")
        ancho = 150
        alto = 30
        x1 = 25
        x2 = x1 + ancho
        y2 = 330

        for valor in reversed(self.pila):  
            y1 = y2 - alto
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="#2196F3")
            self.canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text=valor, fill="white", font=("Arial", 12, "bold"))
            y2 = y1 - 5

        self.canvas.create_rectangle(x1, 20, x2, 330, outline="black", width=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = PilaGUI(root)
    root.mainloop()
