from flask import Flask, request, abort, jsonify, make_response
import flask
import cv2
import werkzeug
import numpy as np
import text_recog_v2 as text
import base64

app = Flask(__name__)

app.config["detection"] = "C:\\Users\\Himanshu Khairajani\\Desktop\\Himanshu 17100017_updated"

@app.route("/", methods=['GET', 'POST'])
@app.route("/home")
def home():
        if request.method=='POST':

            imagefile = flask.request.files['image']
            filename = werkzeug.utils.secure_filename(imagefile.filename)
            print("\nReceived image File name : " + imagefile.filename)
            imagefile.save(filename)

            result = text.himanshu()
            print(result)

            img = cv2.imread("C:\\Users\\Himanshu Khairajani\\Desktop\\Himanshu 17100017_updated\\detection.jpg")
            byte_im = cv2.imencode(".jpg", img)[1].tostring()

            byte_im_string=base64.encodebytes(byte_im).decode('ascii')
            response ={ "result":result, "byte":byte_im_string }
            res = make_response(jsonify(response))
            return res


        return "Working"
if __name__ == "__main__":
	app.run(host="192.168.29.51", port=8081, debug=True)