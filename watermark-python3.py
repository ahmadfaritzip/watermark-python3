from PIL import Image, ImageDraw, ImageFont
import glob

def watermark_text_1(input_image_path, output_image_path, font_file, text, position):
    im = Image.open(input_image_path)
    width, height = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_file, int((width + height) / 30))
    textwidth, textheight = draw.textsize(text, font)

    verticalY, horizontalX = position
    # pos = (width/2) - (textwidth/2), (height/2) - (textheight/2)
    pos = (width) - (textwidth), ((height) - (textheight)) / 2
    # print(width, height)
    # print(pos)
    # print()
    draw.text(pos, text, font=font, fill=(252, 94, 3))
    # im.show()
    im.save(output_image_path)

def watermark_text_2(input_image_path, output_image_path, font_file, text):
    photo = Image.open(input_image_path)
    w, h = photo.size
    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype(font_file, int((w + h) / 30))
    text ="   " + text + "   "
    text_w, text_h = drawing.textsize(text, font)
    
    pos = w - text_w, (h - text_h) - 50
    
    c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
    drawing = ImageDraw.Draw(c_text)
    
    drawing.text((0,0), text, fill="#ffffff", font=font)
    c_text.putalpha(100)
   
    photo.paste(c_text, pos, c_text)
    # photo.show()
    photo.save(output_image_path)

def watermark_photo(input_image_path, output_image_path, watermark_image_path, position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    # add watermark to your image
    base_image.paste(watermark, position)
    base_image.show()
    base_image.save(output_image_path)


def watermark_with_transparency(input_image_path, output_image_path, watermark_image_path, position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path).convert("RGBA")
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)

def main():
    pathFile = 'images/img' + '/'
    pathFileOutput = 'images/watermark' + '/'
    listImg = glob.glob(pathFile + '*')
    watermarkImg = 'fonts/Autumninnovember-rRX8.png'
    text = 'simple Ampas'
    position = (600,600)
    font = 'fonts/Autumninnovember-yPR3.ttf'

    # img = 'images/1.jpg'
    # imgOut = 'images/test_out.jpg'
    # watermark_text_1(img, imgOut, font, text, position)
    for img in listImg:
        imgOut = f'{pathFileOutput}watermark_{img.replace(pathFile, "")}'
        watermark_text_1(img, imgOut, font, text, position)
        # watermark_text_2(img, imgOut, font, text)
    #     watermark_photo(img, imgOut, watermarkImg, position)
    #     watermark_with_transparency(img, imgOut, watermarkImg, position)
    

if __name__ == "__main__":
    main()