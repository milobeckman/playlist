

NO_NEXT = "<!-- NO NEXT -->"
TEMPLATE = "template.txt"
LIST = "list.txt"
INDEX = "index.txt"



def main():
    playlist_id = ask_for("playlist ID")
    html_name = ask_for("html name")
    header = ask_for("header")
    
    html_list = open(LIST, "r").readlines()
    
    if len(html_list) >= 1:
        prev = html_list[-1].strip()
    else:
        prev = ""
    
    create_new_file(playlist_id, html_name, header, prev, "")
    if prev != "":
        update_file(prev, html_name)
    update_index(html_name)


def ask_for(name):
    return raw_input("Enter " + name + ": ")


def create_new_file(playlist_id, html_name, header, prev_html, next_html):
    text = open(TEMPLATE, "r").read()
    text = text.replace("[[PLAYLIST_ID]]", playlist_id)
    text = text.replace("[[HEADER]]", header)
    
    if prev_html == "":
        text = text.replace("<a href=\"[[PREV_HTML]].html\">&laquo;</a>", "")
    else:
        text = text.replace("[[PREV_HTML]]", prev_html)
    
    if next_html == "":
        text = text.replace("<a href=\"[[NEXT_HTML]].html\">&raquo;</a>", NO_NEXT)
    else:
        text = text.replace("[[NEXT_HTML]]", next_html)
    
    new_file = open(html_name + ".html", "w")
    new_file.write(text)
    
    open(LIST, "a").write(html_name + "\n")


def update_file(html_name, next_html):
    text = open(html_name + ".html", "r").read()
    text = text.replace(NO_NEXT, "<a href=\"[[NEXT_HTML]].html\">&raquo;</a>")
    text = text.replace("[[NEXT_HTML]]", next_html)
    open(html_name + ".html", "w").write(text)

def update_index(html_name):
    text = open(INDEX, "r").read()
    text = text.replace("[[HTML_NAME]]", html_name)
    open("index.html", "w").write(text)





if __name__ == '__main__':
    main()