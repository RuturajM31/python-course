# 🌐 Python Functions + Web Programming (Socket & URL Handling)

---

# 📌 1. Introduction

This document explains Python functions using a real-world web programming example.

We build a program that:
- Takes a URL from the user
- Parses it into host + path
- Connects to a web server using sockets
- Fetches and displays data
- Counts characters

---

# 🧠 2. What is a Function?

A function is a reusable block of code that performs a specific task.

```python
def greet():
    print("Hello World")

greet()

| Concept | Meaning              |
| ------- | -------------------- |
| def     | defines a function   |
| call    | runs the function    |
| reuse   | avoid repeating code |

🌐 5. Program Overview

We build a web program using functions:

Steps:

Input URL
Parse URL
Fetch data using socket
Display output

User Input URL
      ↓
    main()
      ↓
 parse_url()
      ↓
 fetch_data()
      ↓
   Output


   🧩 7. parse_url()

   def parse_url(url):
    if url.startswith("http://"):
        url = url[7:]

    parts = url.split("/", 1)

    host = parts[0]
    path = "/" + parts[1] if len(parts) > 1 else "/"

    return host, path

    🧠 What it does:
Removes http://
Splits URL into host + path

🌍 8. fetch_data()

import socket

def fetch_data(host, path):
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

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

        if shown_count < 3000:
            remaining = 3000 - shown_count
            print(text[:remaining], end="")
            shown_count += len(text[:remaining])

    mysock.close()

    print("\n\nTotal characters:", total_count)

    🎮 9. main()

    def main():
    url = input("Enter URL: ")

    try:
        host, path = parse_url(url)
        fetch_data(host, path)
    except:
        print("Invalid URL or error")