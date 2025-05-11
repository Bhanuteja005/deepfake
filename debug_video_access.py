import os
import glob

def list_video_files():
    """List all video files in the static/videos directory."""
    video_dir = os.path.join('static', 'videos')
    
    if not os.path.exists(video_dir):
        print(f"Error: Directory '{video_dir}' does not exist.")
        return
    
    video_files = glob.glob(os.path.join(video_dir, '*.mp4'))
    
    if not video_files:
        print(f"No video files found in {video_dir}")
        return
    
    print(f"Found {len(video_files)} video files in {video_dir}:")
    
    for i, file_path in enumerate(video_files, 1):
        file_size = os.path.getsize(file_path) / (1024)  # Size in KB
        file_name = os.path.basename(file_path)
        url_path = f"/static/videos/{file_name}"
        
        print(f"{i}. {file_name} ({file_size:.2f} KB)")
        print(f"   URL: {url_path}")
        print(f"   Full path: {os.path.abspath(file_path)}")
        print()

if __name__ == "__main__":
    list_video_files()
    print("\nTo debug video access:")
    print("1. Run your Flask app")
    print("2. Try accessing one of the URLs directly in your browser")
    print("3. Check your browser's developer tools (F12) for network errors")
