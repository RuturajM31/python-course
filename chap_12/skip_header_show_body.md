import socket

# ------------------------------------------------------------
# 1. FETCH WEBPAGE BODY USING SOCKET
# ------------------------------------------------------------
def fetch_body(host, path):
    """
    Connects to a web server and extracts ONLY the body
    (removes HTTP headers manually)
    """

    # Step 1: Create a TCP socket (internet connection tool)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 2: Connect to server on port 80 (HTTP)
    mysock.connect((host, 80))

    # Step 3: Build HTTP request manually
    # \r\n = line break required by HTTP protocol
    request = f"GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n"

    # Step 4: Send request to server
    mysock.send(request.encode())

    # Step 5: Collect full response here (headers + body)
    data = b""  # empty bytes container

    # Step 6: Receive data in chunks (512 bytes at a time)
    while True:
        chunk = mysock.recv(512)

        # If no more data → stop loop
        if not chunk:
            break

        # Add chunk to full response
        data += chunk

    # Step 7: Close connection (good practice)
    mysock.close()

    # Step 8: Convert bytes → readable text
    text = data.decode(errors="ignore")

    # ------------------------------------------------------------
    # 2. SEPARATE HEADERS FROM BODY
    # ------------------------------------------------------------

    # HTTP separates headers and body using blank line (\r\n\r\n)
    pos = text.find("\r\n\r\n")

    # If separator found → extract body
    if pos != -1:
        body = text[pos + 4:]   # skip header section
        print("\n===== WEBPAGE BODY =====\n")
        print(body)
    else:
        print("No body found")


# ------------------------------------------------------------
# 3. MAIN PROGRAM (CONTROLLER)
# ------------------------------------------------------------
def main():
    """
    Takes user input and starts the process
    """

    # Step 1: Get URL from user
    url = input("Enter URL: ")

    try:
        # Step 2: Remove http:// if present
        if url.startswith("http://"):
            url = url[7:]

        # Step 3: Split into host and path
        # Example: example.com/page1
        parts = url.split("/", 1)

        host = parts[0]  # domain name

        # If no path given → default "/"
        path = "/" + parts[1] if len(parts) > 1 else "/"

        # Step 4: Call function to fetch webpage
        fetch_body(host, path)

    except Exception as e:
        print("Error:", e)


# ------------------------------------------------------------
# 4. ENTRY POINT
# ------------------------------------------------------------
if __name__ == "__main__":
    main()