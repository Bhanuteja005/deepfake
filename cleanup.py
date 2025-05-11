import os
import shutil
import tempfile
import glob
import time

def cleanup_temp_files():
    """
    Clean up temporary files that are older than 1 hour
    """
    # Get all temporary directories created by the application
    temp_dir = tempfile.gettempdir()
    temp_pattern = os.path.join(temp_dir, 'tmp*')
    
    current_time = time.time()
    one_hour = 3600  # seconds
    
    temp_dirs = glob.glob(temp_pattern)
    
    for directory in temp_dirs:
        try:
            # Check if directory is older than 1 hour
            if os.path.isdir(directory):
                created_time = os.path.getctime(directory)
                if current_time - created_time > one_hour:
                    shutil.rmtree(directory)
                    print(f"Removed old temp directory: {directory}")
        except Exception as e:
            print(f"Error cleaning up {directory}: {str(e)}")

if __name__ == "__main__":
    cleanup_temp_files()
