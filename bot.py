import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(message)
        if response[:3] == "!!!":
            for i in range(5):
                await message.channel.send(response[3:])

        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_bot():
    token = "DISCORD_TOKEN_HERE"
    intents = discord.Intents.default()
    intents.message_content = True
    print(f"intents.messages_content is set to {intents.message_content}")
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running.")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: {user_message} on the channel: {channel}.")

        if not user_message:
            print("still not working")
        else:
            if user_message[0] == "?":
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True)
            else:
                await send_message(message, user_message, is_private=False)

    @client.event
    async def on_guild_channel_create(channel):
        await channel.send(f"you've created the channel {channel}.")

    @client.event
    async def on_guild_channel_delete(channel):
        await channel.send(f"you've deleted the channel {channel}.")

    client.run(token)



