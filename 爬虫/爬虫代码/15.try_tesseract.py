#coding=utf-8

from PIL import Image
import pytesseract


class PytesseractTest():
    def __init__(self):
        self.path = "D:\documents\image\eng_bw.png"

    def ShiBie(self):
        img = Image.open(self.path)
        return pytesseract.image_to_string(img)

if __name__ == '__main__':
    pyt = PytesseractTest()
    text = pyt.ShiBie()
    print(text)