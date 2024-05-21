def get_mime_type(filename):
    # Dictionary mapping file extensions to their MIME types
    known_mime_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    # Normalize the filename to handle case insensitivity
    filename = filename.strip().lower()

    # Find the last dot in the filename to get the extension
    dot_index = filename.rfind('.')

    # If there's no dot or the dot is the last character, there is no valid extension
    if dot_index == -1 or dot_index == len(filename) - 1:
        return 'application/octet-stream'

    # Get the extension from the filename
    file_extension = filename[dot_index:]

    # Return the corresponding MIME type or the default if not recognized
    return known_mime_types.get(file_extension, 'application/octet-stream')

def main():
    # Prompt the user for the name of the file
    filename = input("File name: ")

    # Get the MIME type of the file
    mime_type = get_mime_type(filename)

    # Output the MIME type
    print(mime_type)

if __name__ == "__main__":
    main()