# a main program with empty canvas

import taichi as ti

ti.init(arch=ti.gpu)

canvas_w = 512
canvas_h = 512

pixels = ti.field(dtype=float, shape=(canvas_w, canvas_h))

gui = ti.GUI("Julia Set", res=(canvas_w, canvas_h))
gui.set_image(pixels)
gui.show()

@ti.kernel
def draw_frame(frame_no: ti.i32):
    for x, y in pixels:
        pass


for frame_no in range(0, 1000000000):
    draw_frame(frame_no)
    if frame_no % 1000 == 0:
        print("drawing frame #%i" % (frame_no))
    if not gui.running:
        exit(0)
