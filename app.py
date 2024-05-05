from flask import Flask, render_template, request
import subprocess
import signal  # Import signal module for process termination

app = Flask(__name__)


# Route for the homepage
@app.route("/")
def index():
    return render_template("index1.html")


# Variable to keep track of the detection process
detection_process = None


# Route for stopping object detection
@app.route("/stop_detection", methods=["POST"])
def stop_detection():
    global detection_process

    if detection_process:
        detection_process.terminate()  # Terminate the detection process if it's running
        detection_process = None
        return "Detection stopped successfully!"
    else:
        return "Detection is not running."


# Route for starting object detection
@app.route("/start_detection", methods=["POST"])
def start_detection():
    global detection_process

    if not detection_process:
        # Run the command to start object detection
        detection_process = subprocess.Popen(
            [
                "python",
                "main1.py",
                "--prototxt",
                "mobilenet_ssd/MobileNetSSD_deploy.prototxt",
                "--model",
                "mobilenet_ssd/MobileNetSSD_deploy.caffemodel",
            ]
        )
        return "Detection started successfully!"
    else:
        return "Detection is already running."


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)


# --------------------------------------------------------------------------------------------------------------------------------------------


# from flask import Flask, render_template, Response
# import cv2
# import subprocess

# app = Flask(__name__)


# def gen_frames():
#     for i in range(3):  # Try indices 0, 1, and 2
#         cap = cv2.VideoCapture(i)
#         if cap.isOpened():
#             break
#     else:
#         raise RuntimeError("Failed to open any camera")

#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode(".jpg", frame)
#             frame = buffer.tobytes()
#             yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

#     cap.release()


# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/start_detection", methods=["POST"])
# def start_detection():
#     # Run the command to start object detection
#     subprocess.Popen(
#         [
#             "python",
#             "main1.py",
#             "--prototxt",
#             "mobilenet_ssd/MobileNetSSD_deploy.prototxt",
#             "--model",
#             "mobilenet_ssd/MobileNetSSD_deploy.caffemodel",
#         ]
#     )
#     return "Detection started successfully!"


# @app.route("/video_feed")
# def video_feed():
#     return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


# if __name__ == "__main__":
#     app.run(debug=True)


# use this to get an idea how it works(does not include frontend video stream) runs without error
"""
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for starting object detection
@app.route('/start_detection', methods=['POST'])
def start_detection():
    # Run the command to start object detection
    subprocess.Popen(["python", "main1.py", "--prototxt", "mobilenet_ssd/MobileNetSSD_deploy.prototxt", "--model", "mobilenet_ssd/MobileNetSSD_deploy.caffemodel"])
    return 'Detection started successfully!'

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)

"""
