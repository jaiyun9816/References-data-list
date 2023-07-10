from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
import os
import openai

first_q = "1. 논문의 제목 \n-English : \n-Korean : \n\n\
    2.저자명 \n-English : \n-Korean : "

def convert_pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)

def convert_image_to_text(file):
    text = image_to_string(file, lang='eng+kor')
    return text

def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    for pg, img in enumerate(images):
        final_text += convert_image_to_text(img)

    return final_text

path_to_pdf = './PDF/img_sample2.pdf'
print(get_text_from_any_pdf(path_to_pdf)) # text 추출


