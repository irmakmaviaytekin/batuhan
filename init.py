import cv2
import pytesseract

# Initialize the camera
cap = cv2.VideoCapture(0)

# Function to process each frame from the camera
def capture_and_ocr(frame):
    # Convert the frame to grayscale (optional, helps with OCR accuracy)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply OCR to the grayscale image
    text = pytesseract.image_to_string(gray_frame)

    # Return the recognized text
    return text

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Show the frame in a window
    cv2.imshow('Camera', frame)

    # Perform OCR on the current frame
    text = capture_and_ocr(frame)
    print(f"Recognized Text: {text}")

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()

# biseyler yaptik