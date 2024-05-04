import cv2

# Define image paths and frame timings
image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]
frame_timings = [1, 2, 3]  # Seconds for each frame

# Initialize video writer
video_writer = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'XVID'), 0.5, (640, 480))

# Read and display frames
for image_path, frame_timing in zip(image_paths, frame_timings):
    image = cv2.imread(image_path)
    cv2.imshow('Frame', image)

    # Write frame to video with specified timing
    video_writer.write(image)
    cv2.waitKey(frame_timing * 1000)  # Wait for specified time in milliseconds

# Release resources
video_writer.release()
cv2.destroyAllWindows()
