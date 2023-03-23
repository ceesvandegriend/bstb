import drawsvg as draw


def moluk():
    COLOR = "black"
    d = draw.Drawing(174, 174)
    d.append(draw.Circle(87, 87, 80, stroke=COLOR, stroke_width=14, fill="none"))

    # head
    d.append(draw.Circle(85, 50, 14, fill=COLOR))
    # body
    d.append(draw.Line(85, 50, 85, 100, stroke=COLOR, stroke_width=14, fill="none", stroke_linecap="round"))
    # arms
    d.append(draw.Line(40, 72, 132, 72, stroke=COLOR, stroke_width=14, fill="none", stroke_linecap="round"))
    # left leg
    d.append(draw.Line(85, 100, 52, 127, stroke=COLOR, stroke_width=14, fill="none", stroke_linecap="round"))
    # right leg
    d.append(draw.Line(85, 100, 119, 127, stroke=COLOR, stroke_width=14, fill="none", stroke_linecap="round"))

    d.set_render_size(150, 150)
    d.save_svg("moluk.svg")


if __name__ == "__main__":
    moluk()
