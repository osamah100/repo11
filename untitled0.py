from PIL import Image as im,ImageFont as imf,ImageDraw as imd
import numpy as np
img=im.open("a.jpg")

imageArrye=np.array(img)


print(img.size,img.mode,img.format,img.height,img.width)
c=(0,24,1000,240)
img_crop=img.crop(c)
#img_crop.show()
img.save('ooss.jpg')

img1=im.open('oo.jpg')
wm=im.new("RGBA", img.size)
draw=imd.Draw(wm)
text="osamah"
im1=im.open('oo.jpg')
im1.thumbnail((50,50))
x=(img1.height-im1.height-10)
font=imf.truetype("arial.ttf",size=100)
im_heitht,im_width=draw.textsize(text,font)
text_loc=(img1.width/2-im_heitht/2,im_width)
draw.text(text_loc, text, font=font, fill=(200,200,200,200))
img1.paste(wm,wm)
img1.paste(im1,(10,x))
#img1.show()

r=img.rotate(0.10)
m=img.transpose(im.ROTATE_90)

co=img.convert('CMYK')
print(img.mode,img.format)
print(co.mode,img.format)

from playsound import playsound
playsound("ii.WAV")

import wave
import matplotlib.pyplot as plt
wav=wave.open("ii.WAV")
raw=wav.readframes(-1)
r=np.frombuffer(raw,"int16")
plt.title("os")
plt.ylabel("o")
plt.xlabel("oa")
plt.plot(raw, color='green')

from gtts import GTTS
tr="im osamah"
t=GTTS(tr)





























