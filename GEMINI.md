# Project Overview

This project, "Gemini Course," is a collection of Python-based educational and entertainment scripts. It includes two classic games implemented with the `turtle` module and a programmatic video generation script using `OpenCV`.

### Main Technologies
- **Python 3**: The core programming language.
- **Turtle Graphics**: Used for creating simple 2D games (`snake.py` and `defender.py`).
- **OpenCV (opencv-python)**: Used for generating video content (`generate_video.py`).
- **NumPy**: Used for frame manipulation in the video generation script.

### Architecture
The project follows a script-based architecture where each file is a standalone application:
- `snake.py`: A classic Snake game with high-score tracking.
- `defender.py`: A simple space shooting game ("Space Defender").
- `generate_video.py`: A utility to create a 5-second "Gemini Course" MP4 video with text animations.

---

# Building and Running

### Prerequisites
- Python 3.x installed.
- Install external dependencies:
  ```powershell
  pip install opencv-python numpy
  ```

### Running the Games
- **Snake Game**:
  ```powershell
  python snake.py
  ```
- **Space Defender**:
  ```powershell
  python defender.py
  ```

### Generating the Video
- Run the generation script:
  ```powershell
  python generate_video.py
  ```
- The output will be saved as `gemini_course.mp4`.

---

# Development Conventions

### Coding Style
- **Procedural Logic**: Most scripts use a standard procedural approach with global variables for state management (e.g., score, high score) and functional decomposition for game mechanics.
- **Event-Driven UI**: Uses `turtle.onkeypress` for handling user input in real-time.
- **Game Loops**: Implements manual `while True` loops with `screen.update()` and `time.sleep()` for frame rate control.

### Testing
- There are currently no automated tests. Manual verification by running the scripts is the primary method of testing.

### Contribution Guidelines
- Keep game logic simple and accessible for educational purposes.
- Use built-in libraries like `turtle` whenever possible to minimize setup overhead.
