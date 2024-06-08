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

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>نسخ الكود</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python bitwarden_to_chrome.py
</code></div></div></pre>

6. Follow the on-screen instructions. The script will process the CSV file and generate an output file in the same directory.

## Error Handling

- **Invalid File Extension** : The script checks if the provided file has a `.csv` extension. If not, it raises an error.
- **File Not Found** : If the specified file does not exist, the script raises a `FileNotFoundError` and prompts the user to try again.
- **Invalid Password File Format** : The script checks for the presence of required columns (`name`, `login_uri`, `login_username`, `login_password`). If any are missing, it raises an exception.
- **Permission Error** : If the script cannot write the output file (e.g., due to permission issues), it prompts the user to run the program as an administrator.

## Example

Here's an example of what a processed row might look like:

### Input (Bitwarden CSV):

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>perl</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>نسخ الكود</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-perl">name,login_uri,login_username,login_password
Example,https://example.com,user@example.com,securepassword123
</code></div></div></pre>

### Output (Chrome CSV):

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>perl</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>نسخ الكود</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-perl">name,url,username,password
Example,https://example.com,user@example.com,securepassword123
</code></div></div></pre>

## Notes

- Android logins (rows containing `android://` in any cell) are skipped.
- The output CSV file is named with a timestamp to avoid overwriting existing files.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any issues or questions, please contact the developer.
