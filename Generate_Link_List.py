import os

def generate_raw_links():
    # GitHub raw link base URL
    base_url = "https://raw.githubusercontent.com/Sheart-out/Selfuse_VSC_Background/refs/heads/main/"
    
    # Common image file extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    
    # Get all files in the current directory
    files = os.listdir(".")
    
    # Filter for image files
    image_files = []
    for file in files:
        if os.path.isfile(file):
            _, extension = os.path.splitext(file)
            if extension.lower() in image_extensions:
                image_files.append(file)
    
    # Generate raw links
    raw_links = []
    for image_file in image_files:
        raw_link = '"' + base_url + image_file + '"'
        raw_links.append(raw_link)
    
    # Write links to a text file
    with open("raw_links.txt", "w") as f:
        for link in raw_links:
            f.write(f"{link}\n")
    
    print(f"Generated {len(raw_links)} raw links and saved them to raw_links.txt")

if __name__ == "__main__":
    generate_raw_links()