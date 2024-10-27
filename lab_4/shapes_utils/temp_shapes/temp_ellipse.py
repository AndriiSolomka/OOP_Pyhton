from lab_4.shapes_utils.shape.shape import Shape


class TempEllipse(Shape):

    def show(self):
        # print('IN TEMP ELLIPSE')
        return self.canvas.create_oval(
            self._x1,
            self._y1,
            self._x2,
            self._y2,
            outline="black",
            dash=(4, 2),
        )
