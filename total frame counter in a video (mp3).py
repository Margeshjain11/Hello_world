from typing import Optional
import cv2
import numpy as np

def get_video_frame(video_path: str, frame_number: int = 0) -> Optional[np.ndarray]:
    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        print("Error: Could not open video.")
        return None

    frame_total = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_number = max(0, min(frame_total - 1, frame_number))
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    has_frame, frame = capture.read()
    capture.release()
    if has_frame:
        return frame
    else:
        print(f"Error: Could not retrieve frame {frame_number}.")
    return None

def get_video_frame_total(video_path: str) -> int:
    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        print("Error: Could not open video.")
        return 0

    video_frame_total = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    capture.release()
    return video_frame_total

# Example usage:
if __name__ == "__main__":
    video_path = "your video path"  # Replace with your actual video file path
    frame_number = ("no of frame")
    
    # Get the total number of frames in the video
    total_frames = get_video_frame_total(video_path)
    print(f"Total frames in the video: {total_frames}")

    # Get a specific frame from the video
    frame = get_video_frame(video_path, frame_number)

    if frame is not None:
        # Display the frame
        cv2.imshow(f"Frame {frame_number}", frame)

        # Wait for a key press and close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Optionally, save the frame to a file
        output_path = f"frame_{frame_number}.jpg"
        cv2.imwrite(output_path, frame)
        print(f"Frame {frame_number} saved to {output_path}")
