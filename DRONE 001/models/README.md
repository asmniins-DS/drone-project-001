# Plantify AI

Plantify AI is an intelligent plant analysis system designed for phone-camera-based deployment. It uses a modular pipeline that can later be adapted to drone imagery without changing the core detection logic.

## Project Goals
- Capture live video from a mobile phone camera stream
- Detect and identify plant species
- Display botanical information such as common name, scientific name, confidence, description, and uses
- Keep the camera interface separate from the AI pipeline for future expansion

## Project Structure
- main.py: application entry point
- camera.py: mobile camera source abstraction
- detector.py: video frame processing and detection overlay
- classifier.py: plant classification logic
- plant_database.py: plant information database
- ui.py: live view and user interface

## Phone Camera Setup
1. Install an IP webcam or similar app on your Android phone.
2. Start the camera stream and note the phone’s local IP and port.
3. Update the camera source in camera.py if you want to use a specific stream URL.
4. Run the app and point the phone camera at a plant.

## Run the App
```bash
cd /workspaces/drone-project-001
/home/codespace/.python/current/bin/python main.py
```

## Verification
```bash
cd /workspaces/drone-project-001
/home/codespace/.python/current/bin/python -m unittest discover -s tests -v
```
