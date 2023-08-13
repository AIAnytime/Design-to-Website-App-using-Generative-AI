import easyocr

class OCRProcessor:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def extract_layout(self, img):
        result = self.reader.readtext(img)

        output_list = []

        for original_list, key, _ in result:
            values = [coord for sublist in original_list for coord in sublist]
            formatted_dict = {key: values}
            output_list.append(formatted_dict)

        return output_list

