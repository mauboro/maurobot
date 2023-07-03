import random

def handle_questions(username, message, channel):
    if username == "ak4za":
        return f"well well well, if it isn't the worst league of legends player that I have ever seen!"
    if username == "PedroGTR":
        return f"it's been a long time since we played together man, let's gooo"
    if username == "Kolis":
        return f"hey bro, long time no see!"
    if message == "hello":
        return f"hello {username}"
    elif message == "roll":
        return random.randint(1, 10)
    elif message == "!help":
        return "`my manual will soon be here, it depends on my owner's will, so I don't think it will be THAT soon.`"
    else:
        return f"{message}"

def handle_commands(username, message, channel):
    if message == "flip coin":
        coins = ["heads", "tails"]
        return f"I've flipped {random.choice(coins)}, {username}."
    if message.split()[0] == "maketeam":
        if message.split()[1] == "2":
            players = message.split()[2:]
            random.shuffle(players)
            team_1 = [p for i, p in enumerate(players) if i % 2]
            team_2 = [p for i, p in enumerate(players) if i % 2 == 0]
            return f"TEAM 1: {', '.join(team_1)}\nTEAM 2: {', '.join(team_2)}"
    else:
        return f"{message}"
            

def handle_response(message):

    username = str(message.author).split("#")[0]
    u_message = str(message.content).lower()
    channel = message.channel
    print(u_message.split())

    if len((u_message).split()) == 1:
        return handle_questions(username, u_message, channel)
    elif len(u_message.split()) >= 2:
        return handle_commands(username, u_message, channel)
