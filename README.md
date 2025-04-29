# Automated File Organizer

A Python script that automatically organizes files into separate folders based on their file extensions. Ideal for organizing folders like **Downloads** by sorting images, documents, videos, music, programs, and more.

## Features

- **Organizes files** by extensions: 
  - Images → `.jpg`, `.jpeg`, `.png`, `.gif`
  - Documents → `.pdf`, `.docx`, `.txt`, `.xlsx`
  - Videos → `.mp4`, `.mkv`, `.mov`
  - Music → `.mp3`, `.wav`
  - Archives → `.zip`, `.rar`, `.tar`, `.gz`
  - Programs → `.exe`, `.msi`
  - Unknown files → moved to **Others** folder
- Creates folders automatically if they don't exist.

## How to Use

1. Clone the repository or download the Python script.
   
2. Change the `folder_path` variable to the folder you want to organize (e.g., your **Downloads** folder).

3. Run the script:
    ```bash
    python organizer.py
    ```

4. Enjoy an organized folder!

## Requirements

- Python 3.x
- No external libraries required (uses built-in `os` and `shutil` modules).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

