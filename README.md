# Text_Recognition
- In this project we can send an image using the android app (apk file already provided) consisting of text, and run a local server (flask). 
- When image is sent to server, the server does the processing and revert back the image with bounding box along with the recognized text.

#### Environment
- Make a separed environment to install dependencies and run flask server for backend
- USE: ```python3 -m venv my-venv``` for making environment named as "my-venv"
- To activate environment use  ```source ./my-venv/bin/activate```

#### Installation
- Install the packages and dependencies using ```pip install -r requirements.txt```    
- sudo apt-get install tesseract-ocr

- Download and install the .apk file in your android mobile.

#### Run
-  ```python api.py```
- Note the host Ipv4 Address given in the terminal 
- (example- http://192.169.30.52:8082/) Here  IP: 192.169.30.52, PORT:8082

#### Input
- Open the ```Text Recognition``` app installed using the given .apk
- Select any image from galary for applying text detection+recognition to it.
- Enter IPv4 address and PORT number noted in above step.
- Click 'CONNECT TO SERVER'

#### Output
- You will receive the file in the backend
- The detection and recognition process will take place
- You will get the output image in the app's image view and text as caption.


THANKS
