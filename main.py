import socket
import re
import shelve

server = "irc.chat.twitch.tv"
port = 6667
nickname = ""
token = ""
channel = "#sodapoppin"

sock = socket.socket()
sock.connect((server, port))

sock.send(f"PASS {token}\n".encode("utf-8"))
sock.send(f"NICK {nickname}\n".encode("utf-8"))
sock.send(f"JOIN {channel}\n".encode("utf-8"))

# word_count_shelf = shelve.open("word_count_data")
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

