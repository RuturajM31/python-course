import socket
import ssl


def fetch_body(host, path, use_https=True):
    """
    Fetch webpage body using socket
    Supports HTTPS + required User-Agent (for sites like Wikipedia)
    """

    # 1. Create socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Handle HTTP vs HTTPS
    if use_https:
        context = ssl.create_default_context()
        mysock = context.wrap_socket(mysock, server_hostname=host)
        port = 443
    else:
        port = 80

    # 3. Connect to server
    mysock.connect((host, port))

    # 4. HTTP request with proper headers
    request = (
        f"GET {path} HTTP/1.0\r\n"
        f"Host: {host}\r\n"
        f"User-Agent: Mozilla/5.0\r\n"
        f"Accept: text/html\r\n"
        f"\r\n"
    )

    mysock.send(request.encode())

    # 5. Receive response
    data = b""

    while True:
        chunk = mysock.recv(512)
        if not chunk:
            break
        data += chunk

    mysock.close()

    # 6. Decode response
    text = data.decode(errors="ignore")

    # 7. Remove HTTP headers
    pos = text.find("\r\n\r\n")

    if pos == -1:
        print("No body found")
        return

    body = text[pos + 4:]

    # 8. Output body
    print(body)


def main():
    """
    Main program controller
    """

    url = input("Enter URL (http or https): ")

    use_https = False

    # detect protocol
    if url.startswith("https://"):
        use_https = True
        url = url[8:]

    elif url.startswith("http://"):
        url = url[7:]

    # split host and path
    parts = url.split("/", 1)

    host = parts[0]
    path = "/" + parts[1] if len(parts) > 1 else "/"

    fetch_body(host, path, use_https)


if __name__ == "__main__":
    main()