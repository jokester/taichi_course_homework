# a main program with empty canvas
import taichi as ti

ti.init(arch=ti.gpu)

canvas_w = 960
canvas_h = 540

@ti.kernel
def draw_frame(buffer: ti.template(), frame_no: ti.i32):
    for x, y in buffer:
        buffer[x, y] = ti.Vector([1.0 * x / canvas_w, 1.0 * y / canvas_h, 0.0])

pixels = ti.Vector.field(3, dtype=ti.f32, shape=(canvas_w, canvas_h))
gui = ti.GUI("Empty Canvas", res=(canvas_w, canvas_h))

for frame_no in range(0, 1000000000):
    draw_frame(pixels, frame_no)
    gui.set_image(pixels)
    if gui.running:
        gui.show()
    else:
        print("finished at frame #%d" % (frame_no) )
        exit(0)
