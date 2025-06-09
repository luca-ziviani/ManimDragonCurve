from manim import *

class DragonCurve(Scene):
    def construct(self):
        n = 10                         # Iteration counter
        string = 'F'                   # Initial string
        step = 8. * 2**(-n/2)          # Length of one step
        point = np.array([0,0,0])      # Starting point 

        # Initial orientation
        direction = np.array([-np.cos(np.pi*n/4), np.sin(np.pi*n/4),0])

        # Rotation matrices (90°)
        turn_left = np.array([[0.,-1.,0.],[1.,0.,0.],[0.,0.,0.]])
        turn_right = np.array([[0.,1.,0.],[-1.,0.,0.],[0.,0.,0.]])

        # Initialization
        path = VMobject()
        points = [point]
        
        # Replace F by F+G , replace G by F-G
        replacements = str.maketrans({"F": "F+G", "G": "F-G"})
        for i in range(0, n):
            string = string.translate(replacements)

        # Follow the string instructions
        for c in string:
            if c=="F" or c == "G":
                # Move forward
                point = point + step * direction
                points.append(point)

            elif c == "+":
                # Turn Left
                direction = turn_left.dot(direction)

            elif c == "-":
                # Turn Right
                direction = turn_right.dot(direction)

        # Define path
        path.set_points_as_corners(points)
        path.center()

        # Play: Title
        text = Text("Dragon Curve", color=RED, font_size = 60)
        self.play(FadeIn(text), run_time=1)
        self.wait(1)
        self.play(FadeOut(text),run_time=1)

        # Play: Curve
        self.play(Create(path), run_time=2**(n/2), rate_function=linear)
        self.wait(2)
