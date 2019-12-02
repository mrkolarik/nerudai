from PIL import Image, ImageDraw, ImageFont
import sys
if sys.version_info[0] >= 3:
    unicode = str
try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3
import string
import textwrap
from importlib import reload

reload(sys)
from escpos.printer import Usb

with open('basen.txt', 'r') as myfile:
    veta = myfile.read()

veta_wrap = ""
s = StringIO(veta)
for line in s:
    if(len(line)>37):
        testline = textwrap.fill(line, width=37)
        veta_wrap+=testline + "\n"
    else:
        veta_wrap += line

img = Image.new('RGB', (1000, 30*veta_wrap.count("\n")), color=(255, 255, 255))
fnt = ImageFont.truetype('stroj.ttf', 25)
d = ImageDraw.Draw(img)
d.multiline_text((10, 10), veta_wrap,font=fnt, fill=(0, 0, 0))

img.save('pil_text.png')

# !!!!!!!! HERE ADD PRINTER USB ADDRESS !!!!!
p = Usb(0x04b8,0x0e15,0)
p.image("pil_text.png")
#p.image("logo.jpg")
p.cut()
