from pyrogram import Client, filters

# Your session string

SESSION = "AQDJqkIAeRm_Rtdur4xDwf88Uroyo-SEr3xuRCd5PiOn71-p4kmVPPM4g9R1ck3U0Lfv6PzY0TQZQUWx1jh83dtI7aTe5aYRleqYmTIL4zcUbRHWF7VxpBfXC8qxVasScayBkc17311ODCJh6dNbqtvytK5zA3ypnWvuo5bLz-UOAIERm2HP2rjknu3k6-xzFAE3U4NvllO5Ke23C_MtgfXnohILOuwgMyq78jgaNMCvFeWyHEkNIYZ_I61zq9h5VioByuMa7_W4Jng20rqsoCD-fkgi5CngWOJmyodU3LB8srG7opdjqAljUA-khAA9rqgfeiex3HBH8L70qH0JonEpEgvm7QAAAAFSQG5zAA"
#SESSION = "BQGhN7YAuY8LdLZvtgjaYeexbBPa8GPZtY7KoXGV8_8alavr6t4TBdKdibhKQfDR2wrc3e6l-yKYYCm3_GZq-siCovX9d9hf85vnTYQh9oUinGLr745Li8Vu8mu3lxFFa1jA1W-8CN9-gEGHjvduNKoMlgoFRFBfOETWiJ3v5VjTEWITIFY6y26JTjCqVpdl8FhovZKfttGldms2bmt7hQmE49b6yIk4g0mNBCcBLYlJRjrhGT5Gjul7aiNagy0HJKm2epfJBKCTzmXcJor99cpsbAVt9xubLz-UOAIERm2HP2rjknu3k6-xzFAE3U4NvllO5"
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
    try:
        # Check if the replied message exists and is from a bot
        msg_id = message.reply_to_message.id
        chat_id = message.reply_to_message.from_user.username
        msg = await client.get_messages(chat_id, msg_id)
        msg = await message.reply_text("Genrating link")
        await msg.edit_text(f"https://t.me/b/{chat_id}/{msg_id}")
        await message.edit_text("hello")
    except Exception as e:
        print(f"An error occurred: {e}")


 

# Run the userbot
app.run()
