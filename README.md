# Smart Surveillance System

The Smart Surveillance System is a real-time object detection and tracking system built using Python and Flask. It utilizes computer vision techniques to detect and track objects in live video streams, with the ability to send alerts when specific events occur.

## Features

- Real-time object detection and tracking using the MobileNet SSD model
- Integration with Twilio for sending alerts via SMS
- User-friendly web interface for controlling the surveillance system
- Ability to start and stop the object detection process remotely

## Requirements

- Python 3.x
- Flask
- OpenCV
- dlib
- imutils
- Twilio

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/smart-surveillance-system.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the dashboard.

3. Use the provided interface to start and stop the object detection process.

## Configuration

- To configure Twilio integration, update the Twilio credentials in `main1.py`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the [MIT License](LICENSE).
