import cv2,os,urllib.request
import numpy as np
from django.conf import settings




#the idea behind this class is to open user's camera and scan the QR code.
#The __init__ functions access the user's camera at port 0 
# The __del__ function is to release the user's camera
# The get_frame function uses the camera and then extract the data from the QR code and send it
# to funtion from where it is called. If no data found in QR then it convert the RAW image of
# opencv to jpeg and stream it to user's interface
# That's all about below codes 



class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
		try:
			detector = cv2.QRCodeDetector() #making our detector ready for detection of QR code
			data, bbox, _ = detector.detectAndDecode(image) #passing image to detectore
			if bbox is not None:
				if data: #if found any data in QR
					#print("[+] QR Code detected, data:",data)
					return data
			frame_flip = cv2.flip(image,1)
			ret, jpeg = cv2.imencode('.jpg', frame_flip)
			return jpeg.tobytes()
		except Exception:
			pass


