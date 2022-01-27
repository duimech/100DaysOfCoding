from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        start_position = [(0,0), (-20,0), (-40,0)]

        for position in start_position:
            self.add_segment(position)

    def move_snake(self):
        # Move the last segment to the segment before the last
        for seg_num in range(len(self.segment_list) -1, 0, -1):
            new_x = self.segment_list[seg_num -1].xcor()
            new_y = self.segment_list[seg_num -1].ycor()
            self.segment_list[seg_num].setpos(new_x, new_y)
        
        # Move the head and the body will follow
        self.segment_list[0].forward(20)

    def extend_snake(self):
        self.add_segment(self.segment_list[-1].position())


    def reset(self):
        # Move the snake off the screen before resetting it
        for segment in self.segment_list:
            segment.setposition(900,0)

        self.segment_list.clear()
        self.create_snake()
        self.head = self.segment_list[0]

    
    def add_segment(self, position):
        # The snake is just a list of segments
        new_segment = Turtle()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.setpos(position)
        self.segment_list.append(new_segment)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)