import cv2
import numpy as np

# Video properties
width, height = 1280, 720
fps = 30
duration = 5  # seconds
num_frames = duration * fps

# Define codec and create VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_filename = 'gemini_course.mp4'
video = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

# Background and text settings
blue = (255, 120, 0)  # BGR
white = (255, 255, 255)
font = cv2.FONT_HERSHEY_DUPLEX

for i in range(num_frames):
    # Create black frame
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Simple animation: Text zooms in and fades
    scale = 1 + (i / num_frames) * 2  # Zoom from 1x to 3x
    alpha = min(1.0, (i / (num_frames // 4)))  # Fade in
    if i > num_frames * 0.75:
        alpha = max(0.0, 1.0 - ((i - num_frames * 0.75) / (num_frames // 4)))  # Fade out

    text = "GEMINI COURSE"
    text_size = cv2.getTextSize(text, font, scale, 5)[0]
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2
    
    # Overlay text with fade
    overlay = frame.copy()
    cv2.putText(overlay, text, (text_x, text_y), font, scale, blue, 5, cv2.LINE_AA)
    
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
    
    # Add a simple sub-heading
    if i > num_frames // 4:
        sub_text = "Master the CLI Agent"
        sub_scale = 1.0
        sub_size = cv2.getTextSize(sub_text, font, sub_scale, 2)[0]
        sub_x = (width - sub_size[0]) // 2
        sub_y = text_y + 100
        cv2.putText(frame, sub_text, (sub_x, sub_y), font, sub_scale, white, 2, cv2.LINE_AA)

    # Write frame to video
    video.write(frame)

video.release()
print(f"Video saved as {video_filename}")
