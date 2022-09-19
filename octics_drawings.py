import svgwrite
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

from octics_draw_utils import OcticSquares


# dwg = svgwrite.Drawing(filename = "l3_1.svg", size = ("400px", "200px"))
# octics_draw_utils.draw_square(dwg,(100,100),"asd")
# octics_draw_utils.line_mv(dwg,(100,100),"2")
image = OcticSquares("l3_1.svg",3)
image.add_lines("mv",["P2"],3)
image.save()

drawing = svg2rlg("l3_1.svg")
renderPDF.drawToFile(drawing, "file.pdf")


