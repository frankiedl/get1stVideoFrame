# get1stVideoFrame

A Python utility that automatically extracts the first frame from video files in a specified directory. This tool is useful for creating thumbnails or previews from a collection of videos.

## Features

- 🎥 Supports multiple video formats (MP4, AVI, MOV, MKV, WMV, FLV)
- 📦 Automatic dependency installation
- 🚀 Progress bar visualization
- 📝 Comprehensive logging
- ⚡ Batch processing capabilities
- 🔒 Input validation and error handling
- 📊 Processing summary statistics

## Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

The script will automatically install the required dependencies if they're not present:
- OpenCV (cv2)
- tqdm (for progress bars)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/get1stVideoFrame.git
cd get1stVideoFrame
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line

Run the script by providing the directory path as an argument:
```bash
python get1stVideoFrame.py /path/to/video/directory
```

### Interactive Mode

Run the script without arguments to enter interactive mode:
```bash
python get1stVideoFrame.py
```
You'll be prompted to enter the directory path.

### Output

The script will:
1. Scan the specified directory for video files
2. Extract the first frame from each video
3. Save frames as PNG files with "_first_frame" suffix
4. Display progress and provide a summary of the operation

Example output structure:
```
video_directory/
├── video1.mp4
├── video1_first_frame.png
├── video2.avi
├── video2_first_frame.png
└── ...
```

## Error Handling

The script includes comprehensive error handling for common issues:
- Invalid directory paths
- Inaccessible directories
- Corrupted video files
- Missing dependencies
- Insufficient permissions

All errors are logged with appropriate messages to help troubleshoot issues.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

If you encounter any issues or have questions, please:
1. Check the existing issues in the GitHub repository
2. Create a new issue with a detailed description of your problem
3. Include any relevant error messages and your environment details

## Project Status

This project is actively maintained. Feel free to create issues for bugs or feature requests.

## Requirements.txt

Create a `requirements.txt` file in your project directory with the following content:
```
opencv-python>=4.5.0
tqdm>=4.65.0
```

## Changelog

### [1.0.0] - 2024-02-17
- Initial release
- Basic frame extraction functionality
- Automatic dependency installation
- Progress bar implementation
- Error handling and logging
