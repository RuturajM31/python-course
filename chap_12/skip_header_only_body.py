import socket


def fetch_body(host, path):
    """
    Connect to a web server, fetch response,
    and print ONLY the body (no headers)
    """

    # 1. Create TCP socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    # 2. Send HTTP request
    request = f"GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n"
    mysock.send(request.encode())

    # 3. Receive full response
    data = b""

    while True:
        chunk = mysock.recv(512)
        if not chunk:
            break
        data += chunk

    mysock.close()

    # 4. Convert bytes → string
    text = data.decode(errors="ignore")

    # 5. Separate headers from body
    pos = text.find("\r\n\r\n")

    if pos == -1:
        print("No body found")
        return

    body = text[pos + 4:]

    # 6. Output result
    print(body)


def main():
    """
    Entry point of the program
    """

    url = input("Enter URL (http:// only): ")

    try:
        # Remove http:// if present
        if url.startswith("http://"):
            url = url[7:]

        # Split host and path
        parts = url.split("/", 1)

        host = parts[0]
        path = "/" + parts[1] if len(parts) > 1 else "/"

        # Fetch webpage body
        fetch_body(host, path)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()