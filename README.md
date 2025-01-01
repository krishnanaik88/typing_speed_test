# Typing Speed Test Application

## Description

This project is a terminal-based Typing Speed Test application that allows users to:

- Sign up or log in using their name.
- Take typing speed tests at different difficulty levels.
- View their test history including accuracy and speed.
- Log out and switch between users.

The project uses **MySQL** to store user information and test history, ensuring data persistence. It also features an easy-to-use menu-driven interface.

## Team Members
1. Krishna Rajesh Naik
2. Anurag Adinath Wakchaure
3. Bushra Bilal Shaikh

## Features

1. **User Management**:
   - Sign up for new users.
   - Log in for existing users.
2. **Typing Test**:
   - Difficulty levels: Easy, Medium, and Hard.
   - Calculates accuracy and words-per-minute (WPM).
3. **History Management**:
   - Automatically stores test results in the database.
   - Allows logged-in users to view their test history.
4. **Logout Functionality**:
   - Users can log out and switch accounts without restarting the application.

## Technologies Used

- **Python**: Core programming language.
- **MySQL**: Database management.
- **MySQL Connector**: For connecting Python with MySQL.

## Prerequisites

- Python 3.x installed.
- MySQL installed and running.
- Python package `mysql-connector-python` installed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/krishnanaik88/typing_speed_test.git
   cd typing_speed_test
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the MySQL database:
   - Create a database named `typing_test_db`.
   - Update the database connection settings in the code if needed.

## Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Follow the prompts to log in or sign up.
3. Use the menu to:
   - Take a typing test.
   - View your typing history.
   - Log out or exit the application.

## Database Structure

### Tables

1. **Users Table**:
   - `id`: Primary key.
   - `name`: User's name (unique).
2. **Test History Table**:
   - `id`: Primary key.
   - `user_id`: Foreign key referencing `Users` table.
   - `accuracy`: Typing accuracy.
   - `speed`: Typing speed (WPM).
   - `test_date`: Timestamp of the test.

## Example Output

```
Welcome to the Typing Speed Test!
Enter your username: JohnDoe
Welcome, JohnDoe!

Typing Speed Test Menu:
1. Start Typing Test
2. View Test History
3. Log Out
4. Exit
Enter your choice (1/2/3/4):
```

## Future Scope
1. **Enhanced User Profiles**:
   - Add features like profile pictures and detailed statistics.
2. **Leaderboard System**:
   - Display top users based on their typing speed and accuracy.
3. **Multiplayer Mode**:
   - Allow users to compete in real-time typing tests.
4. **Mobile Application**:
   - Develop a mobile version of the application for Android and iOS.
5. **Custom Text Input**:
   - Allow users to provide their own text for practice.
6. **Gamification**:
   - Introduce badges, rewards, and levels to make the typing test more engaging.








