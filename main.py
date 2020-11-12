import socket
import re
import shelve
from tkinter import *

server = "irc.chat.twitch.tv"
port = 6667
nickname = "Fenastus"
token = "oauth:usqo247rahf8jdncinmwk7me8boe3s"
channel = "#sodapoppin"




def main():
    window = Tk()
    window.geometry("300x200")

    start_scrape = Button(window, text="Run Scraper", command=scrape_data)
    stop_scrape = Button(window, text="Stop Scraper", command="break")
    start_scrape.grid(row=0, column=0, padx=5, pady=5)
    stop_scrape.grid(row=1, column=0, padx=5, pady=5)
    #
    window.mainloop()


# def start():
#     global running
#     running = True
#
#
# def stop():
#     global running
#     running = False


def scrape_data():
    sock = socket.socket()
    sock.connect((server, port))

    sock.send(f"PASS {token}\n".encode("utf-8"))
    sock.send(f"NICK {nickname}\n".encode("utf-8"))
    sock.send(f"JOIN {channel}\n".encode("utf-8"))

    with shelve.open("word_count_data") as word_count_shelf:
        while True:
            response = sock.recv(2048).decode("utf-8")
            response = str(response.strip())

            # print(response)

            try:
                user_search = re.search(":(.*)!", response)
                username = user_search.group(1)
            except AttributeError:
                pass

            channel_format = channel + " :"

            try:
                message = (response.split(channel_format, 1)[1]).lower()
                split_message = message.split(" ")
                for item in split_message:
                    if "tmi.twitch.tv" in item or item.startswith("@"):
                        pass
                    else:
                        if item not in word_count_shelf.keys():
                            word_count_shelf[item] = 1
                            # print(item + "\n" + word_count_dict.get(item))
                            print("not found")
                        else:
                            word_count_shelf[item] = word_count_shelf.get(item) + 1
                            print("found", word_count_shelf.get(item))
            except:
                pass


if __name__ == "__main__":
    main()