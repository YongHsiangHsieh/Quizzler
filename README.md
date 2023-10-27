# Computer Science Quizzer

## Description
This is a simple quiz application designed to test your knowledge of Computer Science. The application is built using Python and uses Tkinter for the user interface.

## Installation

1. Clone the repository to your local machine.
2. Install the required packages using pip:
    ```
    pip install -r requirements.txt
    ```

## How to Run

1. Navigate to the project directory.
2. Run the `main.py` file:
    ```
    python main.py
    ```

## Code Structure

- `data.py`: Fetches quiz questions from an external API. Uses the `requests` library.
- `main.py`: The entry point for the application. Initializes objects and kicks off the quiz.
- `question_model.py`: Defines the `Question` class, used for creating question objects.
- `quiz_brain.py`: Contains the `QuizBrain` class that handles the core quiz logic, including keeping score.
- `ui.py`: Handles the GUI using Tkinter. Interacts with the `QuizBrain` for quiz functionality.

## Future Improvements

1. Add more categories for the quiz.
2. Implement a leaderboard system.
3. Enhance the UI for better user experience.

## License
MIT

---

Enjoy quizzing!
