import sys

from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL"""
    story = urlopen(url)

    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


# makes it more generic so can be used by other functions
def print_items(items):
    for item in items:
        print(item)



#print name of module
def main():
    words = fetch_words('http://sixty-north.com/c/t.txt')
    print_items(words)


if __name__ =='__main__':
    main()