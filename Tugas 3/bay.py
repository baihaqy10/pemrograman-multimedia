from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import PIL
#1 buka file gambar
img = Image.open("phoenix.jpg")

#1 menampilkan
img.show()

#1 simpan sebagai file baru format bmp
img.save('phoenix.BMP', format='BMP')

#2 7 atribut
print(img.filename)
print(img.format)
print(img.mode)
print(img.size)
print(img.width)
print(img.height)
print(img.info)

#3 resize gambar
resized_img = img.resize((300, 300), resample=Image.BICUBIC)
resized_img.save('resized.BMP')

#4 thumbnail
img.thumbnail((720, 720))
img.save('thumb.gif')

#5 crop
crop_img = img.crop((0, 0, 500, 360))
crop_img.save('cropped.jpg')

#6 border
border_im = PIL.Image.new('RGB', (img.width+20, img.height+20), 'red')
border_im.paste(img, (10, 10))
border_im.save('phoenix-border.jpg')

#7 rotate
rotated = img.transpose(Image.ROTATE_90)
# rotated.show()
rotated.save('rotate90.jpg')

#8 Flip kiri-kanan (axis vertikal)
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)

flipped.show()

flipped.save('flipped.jpg')

#9 brightness contrast sharpness
# buat instansi enhancer untuk brightness
enhancer = ImageEnhance.Brightness(img)

factor = 1
# panggil metode enhance untuk memanipulasi
im_output = enhancer.enhance(factor)
#im_output.save('original-image.png')

factor = 0.5 # darkens
im_output = enhancer.enhance(factor)
im_output.save('darkened.png')

factor = 1.5 # brightens
im_output = enhancer.enhance(factor)
im_output.save('brightened.png')

# contrast
enhancer = ImageEnhance.Contrast(img)

factor = 1
im_output = enhancer.enhance(factor)
#im_output.save('original-image.png')

factor = 0.5 # kurangi kontras
im_output = enhancer.enhance(factor)
im_output.save('less-contrast.png')

factor = 1.5 # tambah kontras
im_output = enhancer.enhance(factor)
im_output.save('more-contrast.png')

#sharpen

enhancer = ImageEnhance.Sharpness(img)

factor = 1
im_s_1 = enhancer.enhance(factor)
#im_s_1.save('original-image.png')

factor = 0.05
im_s_1 = enhancer.enhance(factor)
im_s_1.save('blurred.png')

factor = 2
im_s_1 = enhancer.enhance(factor)
im_s_1.save('sharpened.png')

#10 watermark
# Buka gambar sumber
img = Image.open('phoenix.jpg')
width, height = img.size  # lebar dan tinggi untuk kalkulasi koordinat teks

# menambahkan elemen 2d ke gambar yang sudah ada
draw = ImageDraw.Draw(img)

text = '56417904' # ganti dengan npm mu...

# mendefinisikan font baru, lengkap dengan ukurannya
font = ImageFont.truetype('arial.ttf', 18)
# hitung lebar dan tinggi font relatif terhadap gambar utama
textwidth, textheight = draw.textsize(text, font)

# hitung koordinat x, y teks
margin = 15
x = width - textwidth - margin
y = height - textheight - margin

# terapkan watermark
draw.text((x, y), text, font=font)
img.show()

# Simpan gambar
img.save('watermark.jpg')