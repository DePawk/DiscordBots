import discord
import responses


async def send_message(message, user_message,is_private):
    try:
        response = responses.handle_response(user_message)
        if response:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    token = "MTE0MzEwMjY3NzUzMDcyNjQwMA.G0h0Vj.IzeN_r5GyOlc5civCPvhwTqJbCjsXxAb09O8p0"
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        await message.channel.send('sup')



    client.run(token)
