import tkinter as tk

class CistercianApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Explorador Cisterciano - Desktop Version")
        self.root.resizable(False, False)
        
        # Criação do Canvas onde os gráficos serão desenhados
        self.canvas = tk.Canvas(root, width=700, height=700, bg="#dcdcdc")
        self.canvas.pack()
        
        # Associa o movimento do mouse na tela a uma função
        self.canvas.bind('<Motion>', self.on_mouse_move)
        
        # Desenha inicialmente com valor 0
        self.draw(0)
        
    def on_mouse_move(self, event):
        x = max(0, min(event.x, 700))
        y = max(0, min(event.y, 699))
        
        # Mapeamento do mouse para o número de 0 a 9999
        row = y // 7
        number = int((x / 700.0) * 100) + row * 100
        number = max(0, min(number, 9999))
        
        # Atualiza a tela com o novo número
        self.draw(number)
        
    def draw_digit(self, digit, start_x, start_y, x_dir, y_dir):
        w, h = 150, 150
        ex = start_x + w * x_dir
        ey = start_y + h * y_dir
        
        lines = []
        if digit == 1: lines = [(start_x, start_y, ex, start_y)]
        elif digit == 2: lines = [(start_x, ey, ex, ey)]
        elif digit == 3: lines = [(start_x, start_y, ex, ey)]
        elif digit == 4: lines = [(ex, start_y, start_x, ey)]
        elif digit == 5: lines = [(start_x, start_y, ex, start_y), (ex, start_y, start_x, ey)]
        elif digit == 6: lines = [(ex, start_y, ex, ey)]
        elif digit == 7: lines = [(start_x, start_y, ex, start_y), (ex, start_y, ex, ey)]
        elif digit == 8: lines = [(ex, start_y, ex, ey), (start_x, ey, ex, ey)]
        elif digit == 9: lines = [(start_x, start_y, ex, start_y), (ex, start_y, ex, ey), (start_x, ey, ex, ey)]
            
        # Desenha cada linha calculada
        for lx1, ly1, lx2, ly2 in lines:
            self.canvas.create_line(lx1, ly1, lx2, ly2, width=12, fill="black", capstyle=tk.PROJECTING)
            
    def draw(self, number):
        self.canvas.delete("all") # Limpa a tela
        
        # Conversão Binária (Inverte a string para pegar da direita pra esquerda)
        bin_str = format(number, '016b')[::-1]
        for i in range(16):
            # Calcula a posição y com saltos de 10px a cada 4 bits
            y_pos = 260 + i * 10 + (i // 4) * 10
            self.canvas.create_text(30, y_pos, text=bin_str[i], font=("Consolas", 12), fill="black", anchor="nw")
            
        # Texto Decimal
        self.canvas.create_text(350, 680, text=str(number), font=("Arial", 24, "bold"), fill="black", anchor="center")
        
        # Haste central
        x1, y1 = 350, 125
        x2, y2 = 350, 575
        self.canvas.create_line(x1, y1, x2, y2, width=12, fill="black", capstyle=tk.PROJECTING)
        
        # Calcula os dígitos
        ones = number % 10
        tens = (number % 100) // 10
        hundreds = (number % 1000) // 100
        thousands = number // 1000
        
        # Desenha os quatro cantos
        self.draw_digit(ones, x1, y1, 1, 1)
        self.draw_digit(tens, x1, y1, -1, 1)
        self.draw_digit(hundreds, x2, y2, 1, -1)
        self.draw_digit(thousands, x2, y2, -1, -1)

if __name__ == "__main__":
    root = tk.Tk()
    app = CistercianApp(root)
    root.mainloop()
