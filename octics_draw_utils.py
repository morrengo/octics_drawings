import svgwrite

FONT_STYLE    = "font-size:10px; font-family:Arial"
LEFT_OFFSET   = 5
TOP_OFFSET    = 5
IMG_SIZE      = (600,100)

SQUARE_SIZE   = (80,80)
SQUARE_STROKE = 2
SQ_TEXT_OFFSET= 10
SQUARE_OFFSET = 20

LINE_STROKE   = 1

def draw_square(dwg,pos,txt):
    dwg.add(dwg.rect(
        insert=pos,
        size=SQUARE_SIZE,
        stroke="black",
        stroke_width=SQUARE_STROKE,
        fill="white"))
    dwg.add(dwg.text(
        txt,
        insert=(
            pos[0]+SQUARE_SIZE[0]/2-5,
            pos[1]+SQUARE_SIZE[1]+SQ_TEXT_OFFSET),
        style = "font-size:10px; font-family:Arial"))

def add_line_mv(dwg,pos,txt):
    dwg.add(dwg.line(
        start=(pos[0]+SQUARE_SIZE[0]/2,pos[1]),
        end=(pos[0]+SQUARE_SIZE[0]/2,pos[1]+SQUARE_SIZE[1]),
        stroke_width=1,
        stroke="black")
        )
    dwg.add(dwg.text(
        txt,
        insert=(
            pos[0]+SQUARE_SIZE[0]/2+3,
            pos[1]+10),
        style = "font-size:10px; font-family:Arial"))

class OcticSquares:
    def __init__(self,filename,num_of_squares):
        self.num_of_squares = num_of_squares
        self.dwg = svgwrite.Drawing(filename = filename, size = IMG_SIZE)

        self.squares = {}
        curr_pos = (LEFT_OFFSET,TOP_OFFSET)
        for i in range(1,num_of_squares+1):
            sq_id="P"+str(i)
            draw_square(self.dwg,curr_pos,sq_id)
            self.squares[sq_id]=curr_pos
            curr_pos = (curr_pos[0] + SQUARE_SIZE[0] + SQUARE_OFFSET,curr_pos[1])

    def add_lines(self,type,squares,label):
        for square in squares:
            add_line_mv(self.dwg,self.squares[square],label)

    def save(self):
        self.dwg.save()

    