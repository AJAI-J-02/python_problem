from PIL import Image

img=Image.open("loco.jpeg")

bw=img.convert("L")

bw.save("op.jpeg")
bw.show()