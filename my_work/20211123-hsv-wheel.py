#
import taichi as ti

ti.init(arch=ti.gpu)

radius = 480
canvas_w = 2*radius
canvas_h = 2*radius
pi = 3.1416
pixels = ti.Vector.field(3, dtype=ti.f32, shape=(canvas_w, canvas_h))

@ti.func
def hsv2rgb(hue_deg, saturation, value) -> ti.Vector:
# taken from https://rosettacode.org/wiki/Color_wheel#C.2B.2B
    hp = hue_deg / 60.0
    chroma = value * saturation

    c = chroma
    #                         ( hp%2 if % were float mod ) 
    x = chroma * (1 - ti.abs( (hp - 2 * ti.floor(hp / 2.)) - 1))
    m = value - chroma

    r = 0.
    g = 0.
    b = 0.

    if hp <= 1:
        r = c
        g = x
    elif hp <= 2:
        r = x
        g = c
    elif hp <= 3:
        g = c
        b = x
    elif hp <= 4:
        g = x
        b = c
    elif hp <= 5:
        r = x
        b = c
    else:
        r = c
        b = x

    r += m
    g += m
    b += m

    return ti.Vector([r, g, b])


@ti.kernel
def draw_frame(buffer: ti.template(), frame_no: ti.i32):
    for x, y in buffer:
        ox = x * 1. - radius
        oy = y * 1. - radius
        r = ti.sqrt(ox*ox + oy*oy)
        if r < radius:
            hue = ti.atan2(oy, ox)  # range [-pi, pi]
            saturation = r / radius
            value = 1.
            hue_deg = (1 + hue / pi) * 180
            buffer[x, y] = hsv2rgb(hue_deg, saturation, value)


gui = ti.GUI("HSV Wheel", res=(canvas_w, canvas_h))
for frame_no in range(0, 1000000000):
    draw_frame(pixels, frame_no)
    gui.set_image(pixels)
    if gui.running:
        gui.show()
    else:
        print("finished at frame #%d" % (frame_no))
        exit(0)
