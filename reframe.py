import cv2
import os

# Function to separate each frame in a video into individual PNG image files
def separate_frames(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all AVI files in the input folder
    avi_files = [f for f in os.listdir(input_folder) if f.endswith('.avi')]

    for avi_file in avi_files:
        input_path = os.path.join(input_folder, avi_file)

        # Open the video file
        cap = cv2.VideoCapture(input_path)
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Save each frame as a PNG image file
            frame_filename = f"{os.path.splitext(avi_file)[0]}_{frame_count:04d}.png"
            frame_path = os.path.join(output_folder, frame_filename)
            cv2.imwrite(frame_path, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])

            frame_count += 1

        # Release video object
        cap.release()

# Example usage

input_folder = '.'
output_folder = 'output_frames'

separate_frames(input_folder, output_folder)
