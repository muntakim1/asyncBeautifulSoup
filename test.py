from AsyncBeautifulSoup import get_content


if __name__ == "__main__":
    if get_content("https://realpython.com/python-testing/"):
        print("Test:01- passed") 
    else:
        print("Failed")   