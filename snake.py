import tkinter as tk
import random

# Game settings
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
        self.canvas.pack()
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.running = True
        self.root.bind("<KeyPress>", self.change_direction)
        self.update()

    def create_food(self):
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        return x, y

    def change_direction(self, event):
        new_direction = event.keysym
        opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction in opposite_directions and new_direction != opposite_directions[self.direction]:
            self.direction = new_direction

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= CELL_SIZE
        elif self.direction == "Down":
            head_y += CELL_SIZE
        elif self.direction == "Left":
            head_x -= CELL_SIZE
        elif self.direction == "Right":
            head_x += CELL_SIZE
        
        new_head = (head_x, head_y)
        
        # Check for collisions
        if (new_head in self.snake or head_x < 0 or head_y < 0 or head_x >= WIDTH or head_y >= HEIGHT):
            self.running = False
            return
        
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.food = self.create_food()
        else:
            self.snake.pop()

    def draw_elements(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=SNAKE_COLOR)
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx + CELL_SIZE, fy + CELL_SIZE, fill=FOOD_COLOR)

    def update(self):
        if self.running:
            self.move_snake()
            self.draw_elements()
            self.root.after(100, self.update)
        else:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
