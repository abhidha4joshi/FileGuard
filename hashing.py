import hashlib


def calculate_hash(file_path):
    """
    Calculate the SHA-256 hash of a file.
    """

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as error:
        print(f"Error: {error}")
        return None