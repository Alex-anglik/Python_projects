import cairo
from PIL import Image
import numpy

from IPython.display import display, Image as DImage
from io import BytesIO
from math import pi

filename= input("what is the path to the file?")

def disp(draw_func, alpha=1.0, fmt=cairo.FORMAT_ARGB32):
    img = Image.open(filename)
    if 'A' not in img.getbands():
        img.putalpha(int(alpha * 256.))
    arr = bytearray(img.tobytes('raw', 'BGRa'))
    surface = cairo.ImageSurface.create_for_data(arr, fmt, img.width, img.height)
    ctx = cairo.Context(surface)
    draw_func(ctx, img.width, img.height)
    with BytesIO() as fileobj:
        surface.write_to_png(fileobj)
        display(DImage(fileobj.getvalue(), width=img.width))



def text_on_image(cr, width, height):
    TEXT = input("what do you want to write?")
    opacity= int(input('how opaque do you want the text?(from one to ten(ten being the most opaque))'))
    font_size = 0.08
    line_width = 0.04
    cr.scale(width, height)
    cr.set_line_width(line_width)
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(font_size)
    cr.move_to(0.1, 0.1)
    cr.set_source_rgba(0.9, 0.9, 0.9, 0.1*opacity)
    glyphs = []
    x = 0.02
    y = 0.14
    for letter in TEXT:
        glyphs.append(cairo.Glyph(char2glyph(letter), x, y))
        x += letter_width(letter) 
        if x > 0.95:
            y += font_size + line_width
            x = 0.02
            if glyphs[-1].index == char2glyph(' '):
                continue
            else:
                index = glyphs[-1].index
                del glyphs[-1]
                glyphs.append(cairo.Glyph(index, x, y))
                x += letter_width(letter)
    cr.show_glyphs(glyphs)
    cr.stroke()
    
def char2glyph(c):
    return ord(c) - 29
def letter_width(letter):
    if letter.lower() in ['m', 'w', "#", '%', '@', '&' ]:
        return 0.08
    elif letter.lower() in ['i', 'l', 'j', "'", '"', ',', '!', '.', 't', ' ', 'f', '(', ')', '^','*']:
        return 0.03
    elif letter.lower() in ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'k', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'x', 'y', 'z']:
        return 0.05
    else: 
        return 0.05

disp(text_on_image)