from shapes_utils.shape.shape import Shape


class EllipseShape(Shape):
    def show(self):
        self.canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2, outline="black", fill="lightgreen"
        )
