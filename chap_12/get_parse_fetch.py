import socket


def parse_url(url):
    """Extract host and path from URL"""
    ## http://data.pr4e.org/romeo.txt

    # remove http://
    if url.startswith("http://"):
        url = url[7:]

    parts = url.split("/", 1)

    host = parts[0]
    path = "/" + parts[1] if len(parts) > 1 else "/"

    return host, path


def fetch_data(host, path):
    """Fetch webpage using socket"""

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    # send HTTP request
    request = f"GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n"
    mysock.send(request.encode())

    total_count = 0
    shown_count = 0

    while True:
        data = mysock.recv(512)

        if not data:
            break

        text = data.decode(errors="ignore")

        total_count += len(text)

        # print only first 3000 characters
        if shown_count < 3000:
            remaining = 3000 - shown_count
            print(text[:remaining], end="")
            shown_count += len(text[:remaining])

    mysock.close()

    print("\n\nTotal characters:", total_count)


def main():
    url = input("Enter URL: ")

    try:
        host, path = parse_url(url)
        fetch_data(host, path)
    except:
        print("Invalid URL or error")


if __name__ == "__main__":
    main()