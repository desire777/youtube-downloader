
import os

def obter_pasta_downloads():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    downloads_path = os.path.join(script_dir, "downloads")
    
    if not os.path.exists(downloads_path):
        os.makedirs(downloads_path)
    
    return downloads_path


def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")