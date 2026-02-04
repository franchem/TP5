# TP5, par Mika Franche
# Janvier 2026
# Desolé pour les listes


import arcade as ac
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 1024
WINDOW_TITLE = "Da Game"

points = [
[[600.0, 600.0], [400.0, 600.0], [400.0, 400.0], [600.0, 400.0],
 [555.6, 555.6], [444.4, 555.6], [444.4, 444.4], [555.6, 444.4],
 [571.4, 571.4], [428.6, 571.4], [428.6, 428.6], [571.4, 428.6],
 [666.7, 666.7], [333.3, 666.7], [333.3, 333.3], [666.7, 333.3]],
[[561.0, 595.1], [364.3, 607.7], [364.3, 392.3], [561.0, 404.9],
 [534.7, 554.0], [427.1, 557.9], [427.1, 442.1], [534.7, 446.0],
 [585.6, 568.0], [452.4, 574.2], [452.4, 425.8], [585.6, 432.0],
 [687.6, 648.9], [382.8, 682.5], [382.8, 317.5], [687.6, 351.1]],
[[520.5, 592.6], [334.6, 618.4], [334.6, 381.6], [520.5, 407.4],
 [511.8, 553.2], [415.0, 560.8], [415.0, 439.2], [511.8, 446.8],
 [589.8, 564.3], [483.2, 575.7], [483.2, 424.3], [589.8, 435.7],
 [684.8, 632.3], [457.5, 692.1], [457.5, 307.9], [684.8, 367.7]],
[[479.5, 592.6], [315.2, 632.3], [315.2, 367.7], [479.5, 407.4],
 [488.2, 553.2], [410.2, 564.3], [410.2, 435.7], [488.2, 446.8],
 [585.0, 560.8], [516.8, 575.7], [516.8, 424.3], [585.0, 439.2],
 [665.4, 618.4], [542.5, 692.1], [542.5, 307.9], [665.4, 381.6]],
[[439.0, 595.1], [312.4, 648.9], [312.4, 351.1], [439.0, 404.9],
 [465.3, 554.0], [414.4, 568.0], [414.4, 432.0], [465.3, 446.0],
 [572.9, 557.9], [547.6, 574.2], [547.6, 425.8], [572.9, 442.1],
 [635.7, 607.7], [617.2, 682.5], [617.2, 317.5], [635.7, 392.3]]

]
lines = [[0, 1], [1, 2], [2, 3], [3, 0],  # top outer
         [4, 5], [5, 6], [6, 7], [7, 4],  # top inter
         [8, 9], [9, 10], [10, 11], [11, 8],  # bottom inter
         [12, 13], [13, 14], [14, 15], [15, 12],  # bottom outer
         [0, 12], [1, 13], [2, 14], [3, 15],  # side outer
         [4, 8], [5, 9], [6, 10], [7, 11],  # side inter
         [0, 4], [1, 5], [2, 6], [3, 7],  # top link
         [8, 12], [9, 13], [10, 14], [11, 15]  # bottom link
         ]
faces = [[0, 1, 2, 3], [13, 1, 2, 14], [12, 13, 14, 15], [15, 3, 0, 12]]


class GameView(ac.Window):
    """
    Main application class.
    """
    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.frame = 0
        self.second = 0
        self.rep = 0

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

        ac.draw.draw_polygon_filled(
            [points[self.frame][faces[self.rep][0]], points[self.frame][faces[self.rep][1]],
             points[self.frame][faces[self.rep][2]], points[self.frame][faces[self.rep][3]]],
            (100, 100, 100))

        for a in lines:
            ac.draw_line(points[self.frame][a[0]][0], points[self.frame][a[0]][1],
                         points[self.frame][a[1]][0], points[self.frame][a[1]][1], ac.color.WHITE)
        for a in points[self.frame]:
            ac.draw_point(a[0], a[1], ac.color.ATOMIC_TANGERINE, 5)

        ac.draw_text("Hypercube????", 360, 930, (255, 255, 255), 40)
        ac.draw_ellipse_outline(520, 950, (400), (72), (0, 255, 0), 7)


        ac.draw_rect_filled(ac.Rect(480, 490, 760, 790, 30, 70, 510, 860), ac.color.RED)
        ac.draw_triangle_filled(465, 825, 555, 825, 510, 780, ac.color.RED)

        ac.draw_arc_outline(700, 800, 300, 400, (255, 255, 255), 210, 360, 30, 280)
        ac.draw_triangle_filled(780, 620, 740, 640, 765, 680, ac.color.WHITE)

        ac.draw_circle_outline(500, 500, 250, (250, 0, 0), 10)



    def on_update(self, delta_time: float) -> bool | None:
        # print(self.frame, self.rep)
        self.second += delta_time
        if round(self.second, 1) == 0.1:
            self.frame += 1
            self.second = 0
            if self.frame == 5:
                self.frame = 0
                self.rep += 1
                if self.rep == 4:
                    self.rep = 0


def main():
    """Main function"""
    window = GameView()
    window.setup()
    ac.run()


if __name__ == "__main__":
    main()
