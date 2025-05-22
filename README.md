# GitHub Raw Link Generator and personal VSCode Background

A simple Python script that automatically generates GitHub raw links for image files in the current directory, making it easy to batch-generate links before uploading files to your repository.


## Overview

This tool scans your local directory for image files and generates the corresponding GitHub raw links based on a predefined repository pattern. This is particularly useful when you want to prepare links for images before actually uploading them to GitHub, streamlining your workflow for managing image repositories.

## Features

- **Automatic Image Detection**: Scans current directory for common image formats
- **Batch Link Generation**: Creates raw GitHub links for all detected images
- **Multiple Format Support**: Supports JPG, JPEG, PNG, GIF, BMP, TIFF, and WebP formats
- **Simple Output**: Generates a clean text file with one link per line
- **Zero Dependencies**: Uses only Python standard library

## Installation

1. Clone this repository or download the script
2. Ensure you have Python 3.x installed
3. No additional dependencies required

## Usage

1. Place the `Generate_Link_List.py` script in the directory containing your image files
2. Open `Generate_Link_List.py`, change the `base_url` to your own git hub repository URL.
  E.g:
  ```python
  base_url = "https://raw.githubusercontent.com/Sheart-out/Selfuse_VSC_Background/refs/heads/main/"
  ```
  URL Pattern:
  'https://raw.githubusercontent.com/[Your github username]/[Your repository name]/.......'
4. Run the script:
   ```bash
   python Generate_Law_list.py
   ```
5. The script will create a `raw_links.txt` file with all the generated links

### Example Output

```
https://raw.githubusercontent.com/Sheart-out/Selfuse_VSC_Background/refs/heads/main/wallpaper1.jpg
https://raw.githubusercontent.com/Sheart-out/Selfuse_VSC_Background/refs/heads/main/background.png
https://raw.githubusercontent.com/Sheart-out/Selfuse_VSC_Background/refs/heads/main/99428027_p0.jpg
```

## Configuration

To use this script with your own repository, modify the `base_url` variable in the script:

```python
base_url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/refs/heads/main/"
```

## Supported Image Formats

- JPG/JPEG
- PNG
- GIF
- BMP
- TIFF
- WebP

## Workflow

1. **Prepare Images**: Place all your image files in a directory
2. **Generate Links**: Run the script to create `raw_links.txt`
3. **Upload Images**: Upload the actual image files to your GitHub repository
4. **Use Links**: The pre-generated links in `raw_links.txt` will now be accessible

## Use Cases

- **Wallpaper Collections**: Perfect for managing personal wallpaper repositories
- **Image CDN**: Using GitHub as a simple image hosting solution
- **Documentation**: Preparing image links for README files or documentation
- **Web Development**: Batch-generating image URLs for web projects

## File Structure

```
your-directory/
├── generate_raw_links.py
├── image1.jpg
├── image2.png
├── ...
└── raw_links.txt (generated)
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements:

- Some other beautiful Background
- Support for additional image formats
- Custom output file naming
- Subdirectory scanning
- Different link formats

## License

This project is open source and available under the [MIT License](LICENSE).

## Notes

- The script only processes files in the current directory (not subdirectories)
- Generated links will be valid once the corresponding files are uploaded to GitHub
- Make sure your repository is public if you want the raw links to be accessible without authentication
