"""
Video Frame Extractor
====================

This script extracts the first frame from all video files in a specified directory
and saves them as PNG images.

Features:
- Automatic package installation if dependencies are missing
- Support for multiple video formats
- Error handling and logging
- Progress feedback
- Input validation

Dependencies:
- OpenCV (cv2)
- tqdm (for progress bars)

Usage:
    python frame_extractor.py <directory_path>
    
    If no directory path is provided, it will ask for one interactively.
"""

import cv2
import os
import sys
import subprocess
import logging
from typing import List, Optional

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_dependencies() -> None:
    """
    Check if required packages are installed and install them if necessary.
    """
    required_packages = ['opencv-python', 'tqdm']
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            logger.info(f"Installing required package: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def validate_directory(directory: str) -> bool:
    """
    Validate if the provided directory exists and is accessible.
    
    Args:
        directory (str): Path to the directory to validate
        
    Returns:
        bool: True if directory is valid, False otherwise
    """
    if not os.path.exists(directory):
        logger.error(f"Directory does not exist: {directory}")
        return False
    if not os.path.isdir(directory):
        logger.error(f"Path is not a directory: {directory}")
        return False
    if not os.access(directory, os.R_OK | os.W_OK):
        logger.error(f"Insufficient permissions for directory: {directory}")
        return False
    return True

def get_video_files(directory: str) -> List[str]:
    """
    Get a list of video files in the specified directory.
    
    Args:
        directory (str): Path to search for video files
        
    Returns:
        List[str]: List of video file paths
    """
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv')
    video_files = []
    
    for file in os.listdir(directory):
        if file.lower().endswith(video_extensions):
            video_files.append(os.path.join(directory, file))
    
    return video_files

def extract_first_frame(video_path: str) -> Optional[str]:
    """
    Extract the first frame from a video file and save it as PNG.
    
    Args:
        video_path (str): Path to the video file
        
    Returns:
        Optional[str]: Path to the saved frame image if successful, None otherwise
    """
    try:
        # Create video capture object
        video_capture = cv2.VideoCapture(video_path)
        
        if not video_capture.isOpened():
            logger.error(f"Could not open video file: {video_path}")
            return None
        
        # Read the first frame
        success, frame = video_capture.read()
        
        if not success:
            logger.error(f"Could not read frame from video: {video_path}")
            return None
        
        # Generate output filename
        base_name = os.path.splitext(video_path)[0]
        output_path = f"{base_name}_first_frame.png"
        
        # Save the frame
        cv2.imwrite(output_path, frame)
        
        return output_path
        
    except Exception as e:
        logger.error(f"Error processing {video_path}: {str(e)}")
        return None
        
    finally:
        video_capture.release()

def main():
    """
    Main function to run the frame extraction process.
    """
    # Check and install dependencies
    check_dependencies()
    
    # Now we can safely import tqdm
    from tqdm import tqdm
    
    # Get directory path
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("Please enter the directory path containing video files: ")
    
    # Validate directory
    if not validate_directory(directory):
        sys.exit(1)
    
    # Get video files
    video_files = get_video_files(directory)
    
    if not video_files:
        logger.warning(f"No video files found in {directory}")
        sys.exit(0)
    
    logger.info(f"Found {len(video_files)} video files")
    
    # Process videos with progress bar
    successful = 0
    failed = 0
    
    for video_file in tqdm(video_files, desc="Extracting frames"):
        if extract_first_frame(video_file):
            successful += 1
        else:
            failed += 1
    
    # Print summary
    logger.info(f"""
    Processing complete:
    - Total videos processed: {len(video_files)}
    - Successful extractions: {successful}
    - Failed extractions: {failed}
    """)

if __name__ == "__main__":
    main()
