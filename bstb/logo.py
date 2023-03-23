import drawsvg as draw


def moluk():
    WIDTH = 100
    HEIGHT = 100
    STROKE = 8
    # COLOR = "#7db53d"
    COLOR = "black"

    d = draw.Drawing(WIDTH, HEIGHT)

    xc = int(WIDTH / 2)
    yc = int(HEIGHT / 2)
    r = int((WIDTH - STROKE) / 2)
    d.append(draw.Circle(xc, yc, r, stroke=COLOR, stroke_width=STROKE, fill="none"))

    # head
    x1 = int(WIDTH * 0.5)
    y1 = int(HEIGHT * 0.2)
    r = STROKE
    d.append(draw.Circle(x1, y1, r, fill=COLOR))

    # body
    x2 = x1
    y2 = y1
    x3 = int(WIDTH * 0.5)
    y3 = int(HEIGHT * 0.55)
    d.append(draw.Line(x2, y2, x3, y3, stroke=COLOR, stroke_width=STROKE, fill=COLOR, stroke_linecap="round"))

    # arms
    x4 = int(WIDTH * 0.25)
    y4 = int(HEIGHT * 0.30)
    x5 = int(WIDTH * 0.75)
    y5 = y4
    d.append(draw.Line(x4, y4, x5, y5, stroke=COLOR, stroke_width=STROKE, fill=COLOR, stroke_linecap="round"))

    # left leg
    x6 = x3
    y6 = y3
    x7 = int(WIDTH * 0.3)
    y7 = int(HEIGHT * 0.8)
    d.append(draw.Line(x6, y6, x7, y7, stroke=COLOR, stroke_width=STROKE, fill=COLOR, stroke_linecap="round"))

    # right leg
    x8 = x3
    y8 = y3
    x9 = int(WIDTH * 0.7)
    y9 = int(HEIGHT * 0.8)
    d.append(draw.Line(x8, y8, x9, y9, stroke=COLOR, stroke_width=STROKE, fill=COLOR, stroke_linecap="round"))

    d.save_svg("moluk.svg")


if __name__ == "__main__":
    moluk()
