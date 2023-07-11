from tika import parser
pdf_path = "/PDF/img_sample1.pdf"
parsed = parser.from_file(pdf_path)
print(parsed['content'])
# txt = open('output.txt', 'w', encoding = 'utf-8')
# print(parsed['content'], file = txt)
# txt.close()