import cv2
import pytesseract
from pytesseract import Output
#pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\deskop_\\tesseract.exe'

def text_recognition(res):
    boxes = res[0]

    if len(boxes)==0:
        result = "There is NO text"
        
    else:
        rW = res[1]
        rH = res[2]
        orig = cv2.imread('./upload/image.jpg')
        print(len(boxes),"word found")

        # loop over the bounding boxes
        result= ""
        for idx,(startX, startY, endX, endY) in enumerate(boxes):
        	# scale the bounding box coordinates based on the respective ratios
            startX = int(startX * rW)
            startY = int(startY * rH)
            endX = int(endX * rW)
            endY = int(endY * rH)
            try:
                cropped= orig[startY:startY+(endY-startY),startX:startX+(endX-startX)]
                e = pytesseract.image_to_string(cropped, lang = 'eng')
                result+=" "+e
            except:
                pass
                        
    return result

if __name__ == "__main__":
    print(text_recognition([[],1,2]))