from pyrogram import Client, filters

# Your session string
SESSION = "BQGhN7YAuY8LdLZvtgjaYeexbBPa8GPZtY7KoXGV8_8alavr6t4TBdKdibhKQfDR2wrc3e6l-yKYYCm3_GZq-siCovX9d9hf85vnTYQh9oUinGLr745Li8Vu8mu3lxFFa1jA1W-8CN9-gEGHjvduNKoMlgoFRFBfOETWiJ3v5VjTEWITIFY6y26JTjCqVpdl8FhovZKfttGldms2bmt7hQmE49b6yIk4g0mNBCcBLYlJRjrhGT5Gjul7aiNagy0HJKm2epfJBKCTzmXcJor99cpsbAVt9xuQ6338yTC4yfSxzNyd_2z03jIg5gUkSY0HXLCEmM2nXYj1H2yoUDExqd0a0mlnAAAAAAFfdWJUAA"

APP_ID = 23476439
API_HASH = "1626e884119a29dbccbb78e39b48128f"

# Save the session string to a file
with open("session.txt", "w") as file:
    file.write(SESSION)

# Initialize Pyrogram client with the session file
app = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=APP_ID) 

# Function to handle messages
@app.on_message(filters.me & filters.reply & filters.command("link", prefixes="."))
async def handle_link_command(client, message):
    # Check if the replied message exists and is from a bot
    #id="error"
    id = message.reply_to_message.id
    #id = message.reply_to_message.message_id
    chat_id = message.reply_to_message.from_user.username
    await message.reply_text(f"https://t.me/b/{chat_id}/{id}")
    # Check if the replied message exists and is from a bot
    await client.edit_message_text(f"https://t.me/b/{chat_id}/{id}")
    print(id,chat_id)

 

# Run the userbot
app.run()
