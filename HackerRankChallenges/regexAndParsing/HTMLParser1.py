__author__ = "Manoj Kumar Arram"

from html.parser import HTMLParser

if __name__ == "__main__":
    # create a subclass and override the handler methods
    class MyHTMLParser(HTMLParser):
        def error(self, message):
            print("Error Occurred : ", message)

        def handle_starttag(self, tag, attrs):
            print("Start :", tag)
            for attr in attrs:
                print("->", attr[0], ">", attr[1])

        def handle_startendtag(self, tag, attrs):
            print("Empty :", tag)
            for attr in attrs:
                print('->', attr[0], '>', attr[1])

        def handle_endtag(self, tag):
            print("End   :", tag)

        # def handle_data(self, data):
        #     print(
        #         "Some data : ", data)


    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    # htmlCode = None
    # for _ in range(int(input())):
    #     htmlCode += input()
    # parser.feed(htmlCode)
    parser.feed('<html><head><title>Test</title></head>'
                '<body><h1>Parse me!</h1><br /></body></html>')
