import urllib.request
from bs4 import BeautifulSoup


def count_paragraphs(url):
    """Count number of <p> tags"""

    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, "html.parser")

    paragraphs = soup.find_all("p")

    return len(paragraphs)


def main():
    url = input("Enter URL: ")

    try:
        count = count_paragraphs(url)
        print("Number of <p> tags:", count)
    except:
        print("Error processing URL")


if __name__ == "__main__":
    main()