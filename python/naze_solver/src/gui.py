from enum import Enum, auto
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

from maze_solver import MazeSolver


class MazeSolverGUI:
    class MazeSolverState(Enum):
        LOADING_IMAGE = auto()
        SELECTING_POINTS = auto()
        ANALYZING = auto()
        PATH_FOUND = auto()
        ERROR = auto()

    def __init__(self, root):

        self.root = root
        self.state = MazeSolverGUI.MazeSolverState.SELECTING_POINTS
        self.current_width = self.root.winfo_screenwidth()
        self.current_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.current_width}x{self.current_height}")
        self.root.title("MAZE SOLVER")

        # Data for engine
        self.image = None
        self.points = []

        # Load and display the image
        self.load_image_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_image_button.pack(pady=(30, 10))

        self.size_image = self.get_canvas_image_size()
        self.canvas = tk.Canvas(self.root, width=self.size_image, height=self.size_image, bg="white")
        self.canvas.pack()

        self.label = tk.Label(root, text="Please select a picture of a maze", font=("Arial", 16))
        self.label.pack(pady=10)

        self.run_button = tk.Button(root, text="run", command=self.run)
        self.run_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Refresh", command=self.refresh)
        self.exit_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

        # Bind mouse click event
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.root.bind("<Configure>", self.resize)

    def update_state(self, new_state):
        self.state = new_state
        if self.state == MazeSolverGUI.MazeSolverState.LOADING_IMAGE:
            self.label.config(text="Loading image...")
        elif self.state == MazeSolverGUI.MazeSolverState.SELECTING_POINTS:
            self.label.config(text="Please select a start point and an end point (click on the image)")
        elif self.state == MazeSolverGUI.MazeSolverState.ANALYZING:
            self.label.config(text="Analyzing... Please wait")
        elif self.state == MazeSolverGUI.MazeSolverState.PATH_FOUND:
            self.label.config(text="Path found and displayed!")
        elif self.state == MazeSolverGUI.MazeSolverState.ERROR:
            self.label.config(text="An error occurred")

    def get_canvas_image_size(self):
        if self.current_width > self.current_height:
            w_h = self.current_height * (3 / 4)
        else:
            w_h = self.current_width * (3 / 4)
        return int(w_h)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.update_state(MazeSolverGUI.MazeSolverState.LOADING_IMAGE)
            self.root.update_idletasks()

            self.image = cv2.imread(file_path)
            self.image = cv2.resize(self.image, (self.size_image, self.size_image))
            self.tk_image = ImageTk.PhotoImage(image=Image.fromarray(self.image))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

            self.update_state(MazeSolverGUI.MazeSolverState.SELECTING_POINTS)

    def on_canvas_click(self, event):
        if self.image is not None and (self.state == MazeSolverGUI.MazeSolverState.SELECTING_POINTS or self.state == MazeSolverGUI.MazeSolverState.SELECTING_POINTS):
            x, y = event.x, event.y
            point_id = self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, outline="red", fill="red")
            self.points.append(((y, x), point_id))

            if len(self.points) > 2:
                old_point = self.points.pop(0)
                if old_point[1]:
                    self.canvas.delete(old_point[1])

            if len(self.points) == 2:
                self.update_state(MazeSolverGUI.MazeSolverState.SELECTING_POINTS)

    def resize(self, event):
        if event.widget != self.root:
            return

        self.current_width = event.width
        self.current_height = event.height

        self.size_image = self.get_canvas_image_size()
        self.canvas.config(width=self.size_image, height=self.size_image)

        if self.image is not None:
            self.image = cv2.resize(self.image, (self.size_image, self.size_image))
            self.tk_image = ImageTk.PhotoImage(image=Image.fromarray(self.image))
            self.canvas.delete("image")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image, tags="image")

    def draw_path(self, path):
        x0, y0 = path[0]
        for vertex in path[1:]:
            x1, y1 = vertex
            self.canvas.create_line(y0, x0, y1, x1, fill="red", width=2, tags="path")
            x0, y0 = vertex

    def refresh(self):
        if self.state == MazeSolverGUI.MazeSolverState.PATH_FOUND:
            self.update_state(MazeSolverGUI.MazeSolverState.SELECTING_POINTS)
            self.canvas.delete("path")

    def run(self):
        if len(self.points) < 2 or self.image is None and self.state == MazeSolverGUI.MazeSolverState.SELECTING_POINTS:
            self.update_state(MazeSolverGUI.MazeSolverState.ERROR)
            return

        self.update_state(MazeSolverGUI.MazeSolverState.ANALYZING)
        self.root.update_idletasks()

        path = MazeSolver.solv(self.image, self.points[0][0], self.points[1][0])
        if path:
            self.draw_path(path)
            self.update_state(MazeSolverGUI.MazeSolverState.PATH_FOUND)
        else:
            self.update_state(MazeSolverGUI.MazeSolverState.ERROR)
