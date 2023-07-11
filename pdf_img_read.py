import pytesseract
from PIL import Image
from pdf2image import convert_from_path

# PDF를 이미지로 변환
def pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    return images

# 이미지에서 텍스트 추출
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

# 이미지로 구성된 PDF에서 텍스트 추출
def extract_text_from_pdf(pdf_path):
    images = pdf_to_images(pdf_path)
    extracted_text = ''
    for image in images:
        text = extract_text_from_image(image)
        extracted_text += text
    return extracted_text

# 이미지로 구성된 PDF 경로
pdf_path = '경로/이미지로_구성된_파일.pdf'

# 텍스트 추출 실행
extracted_text = extract_text_from_pdf(pdf_path)

# 추출된 텍스트 출력
print(extracted_text)
