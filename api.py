from flask import Flask, request, abort, jsonify, make_response
import cv2
import text_recognition as text_recognition
import text_detection as text_detection
import base64

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/home")
def home():
        if request.method == "POST":
            f = request.files['image']
            f_name = f.filename
            
            if f_name!='':
                f_path = './upload/image.jpg'
                f.save(f_path)
                print('File saved successfully')
                
                result_detection = text_detection.text_detection()
                result = text_recognition.text_recognition(result_detection)
                print('Recognized text: ',result)

                img = cv2.imread("./upload/detection.jpg")
                byte_im = cv2.imencode(".jpg", img)[1].tostring()

                byte_im_string=base64.encodebytes(byte_im).decode('ascii')
                response ={ "result":result, "byte":byte_im_string }
                res = make_response(jsonify(response))
                return res
            
            else:

                response ={"result":"Please upload any image file"}
                res = make_response(jsonify(response))
                return res

        return "Text Recognition API Working"

if __name__ == "__main__":
    # host-> Enter IPv4 address of wifi/hotspot your system is connected to
    # port-> Enter port number to open the end-point on
	app.run(host="192.168.29.51", port=8082, debug=True)