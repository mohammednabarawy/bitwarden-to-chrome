import os
import csv
import datetime


def main():
    while True:
        try:
            file_path = r"C:\Users\moham\Desktop\bitwarden to chrome\bitwarden_export_20240608143645.csv"

            # Check if the provided file path ends with .csv
            if not file_path.lower().endswith(".csv"):
                raise Exception("ERROR: Invalid file extension. Must be .csv")

            # Ensure the file exists
            if not os.path.isfile(file_path):
                raise FileNotFoundError(
                    f"ERROR: File not found at {file_path}")

            file_location_dir = os.path.dirname(file_path)
            file_name_with_extension = os.path.basename(file_path)
            file_name, file_extension = os.path.splitext(
                file_name_with_extension)

            print("Processing passwords...")

            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                output_csv = [["name", "url", "username", "password"]]

                headers = next(reader)
                if "name" not in headers or "login_uri" not in headers or "login_username" not in headers or "login_password" not in headers:
                    raise Exception(
                        "Invalid password file format. Please contact the developer!")

                index_of_name = headers.index("name")
                index_of_url = headers.index("login_uri")
                index_of_username = headers.index("login_username")
                index_of_password = headers.index("login_password")

                # Start from 2 to account for header row
                for row_num, row in enumerate(reader, start=2):
                    # Skip android logins
                    if any("android://" in cell for cell in row):
                        continue

                    if len(row) <= max(index_of_name, index_of_url, index_of_username, index_of_password):
                        print(
                            f"Skipping row {row_num}: {row} (Not enough columns)")
                        continue

                    name = row[index_of_name]
                    uri = row[index_of_url]
                    username = row[index_of_username]
                    password = row[index_of_password]

                    chrome_csv_line = [name, uri, username, password]
                    output_csv.append(chrome_csv_line)
                    print(name)

            print("Processing finished!")
            print("")

            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            output_file_name = f"BitwardenToChromePasswords_{timestamp}.csv"
            output_file_path = os.path.join(
                file_location_dir, output_file_name)

            with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(output_csv)

            print("\033[42m\033[30mOperation successful!\033[0m")
            print(f"Output file: {output_file_name}")
            print(f"Output location: {output_file_path}")
            print("Press Enter to quit")
            input()
            return
        except PermissionError:
            print(
                "ERROR: Cannot write output file. Please run the program as an administrator!")
            print("Press any key to exit!")
            input()
            return
        except FileNotFoundError as fnfe:
            print(fnfe)
            print("Press any key to try again!")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            print(f"ERROR: {e}")
            print("Press any key to try again!")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
