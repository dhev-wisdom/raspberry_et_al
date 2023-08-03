import cv2

# In other to acheive detecting faces from video/image using raspberry pi, you will need a Raspberry pi setup
# Get a Raspberry Pi board, power supply, and microSD card
# Download and install the raspberry pi operating system into the micro SD. You can download one from here:
# https://www.raspberrypi.org/software/
# Connect the Raspberry Pi to a display, keyboard, and mouse. Finish setup.
# Install the necessary libraries:
# On Ubuntu or Linux, run `sudo apt update`. Then `sudo apt-get install python3-opencv` to install OpenCV
# Below is the python script to detect face using OpenCV



def detect_face():
    """
    fucntion to detect face using OpenCV
    """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0) # Initialize the camera module

    while True:
        ret, frame = cap.read()  # Read a frame from the camera      
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert the frame to grayscale for face detection
        
        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('Face Detection', frame)
        
        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect_face()
