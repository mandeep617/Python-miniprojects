# pip install python_barcode
import barcode
from barcode.writer import ImageWriter
text = "Generating barcode using Python"
text_ = str(text)
code = barcode.get_barcode_class("code128")
image = code(text, writer=ImageWriter())
savedimage = image.save("final barcode")