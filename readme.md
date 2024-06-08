# Bitwarden to Chrome Password Converter

This Python script processes a CSV file exported from Bitwarden and converts it into a format suitable for import into Google Chrome.

## Features

- Validates the provided file path and extension.
- Ensures the existence of the specified file.
- Processes the CSV file to extract password information.
- Skips rows with insufficient columns and Android logins.
- Generates an output CSV file compatible with Google Chrome.
- Handles errors gracefully and provides user-friendly messages.

## Requirements

- Python 3.x
- Required libraries: `os`, `csv`, `datetime`

## Usage

1. Ensure you have Python 3 installed on your system.
2. Clone this repository or download the script.
3. Place the Bitwarden CSV export file in a known location.
4. Update the `file_path` variable in the script with the path to your Bitwarden CSV file.
5. Run the script using Python:

   ```
   python bitwarden_to_chrome.py
   ```

   ```

   ```

6. Follow the on-screen instructions. The script will process the CSV file and generate an output file in the same directory.

## Error Handling

- **Invalid File Extension** : The script checks if the provided file has a `.csv` extension. If not, it raises an error.
- **File Not Found** : If the specified file does not exist, the script raises a `FileNotFoundError` and prompts the user to try again.
- **Invalid Password File Format** : The script checks for the presence of required columns (`name`, `login_uri`, `login_username`, `login_password`). If any are missing, it raises an exception.
- **Permission Error** : If the script cannot write the output file (e.g., due to permission issues), it prompts the user to run the program as an administrator.

## Example

Here's an example of what a processed row might look like:

### Input (Bitwarden CSV):

```
name,login_uri,login_username,login_password
Example,https://example.com,user@example.com,securepassword123
```

### Output (Chrome CSV):

```
span
```

## Notes

- Android logins (rows containing `android://` in any cell) are skipped.
- The output CSV file is named with a timestamp to avoid overwriting existing files.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any issues or questions, please contact the developer.
