from pyrogram import Client, filters
from pyrogram.types import Message

# Your session string
SESSION ="BQFmONcASNSlWTTCENlUwDdYnMbA4Vplog6_plkvjhA2v6I1oN_Z2rJcbPMQtSYMR90BlvynlSa3SSQz_sCxPYkm39ffXdO_k-TKpx-KlHMKN-qhL1wV1NgPJaephiAl4kBB1S9JRZP8fSiC5OUdhnpCMVqmY-ma5XBaSsXRLR41RMKlmp2VK4aJvg2fXCUJ4FHph6b96eqPdcLtjc0KqqU1altrPgfwwDh-_hPkx1rudtTle4BEJbJAtdXTsY7HMNqPQI7vxF88bejzYs9F0XdU_bjDIVhaghnw8g_J1TVUmvzMAjvjBmIuzsrXv_rNCMoTNLVb-P080qbI36LzHjy6DQ4I-gAAAAFQUsvEAA"

APP_ID=23476439
API_HASH="1626e884119a29dbccbb78e39b48128f"

# Save the session string to a file
with open("session.txt", "w") as file:
    file.write(SESSION)

# Initialize Pyrogram client with the session file
app = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 


# Function to handle messages
@app.on_message(filters.me & filters.reply & filters.command("link", prefixes="."))
async def handle_link_command(client, message: Message):
    # Check if the replied message exists
    if message.reply_to_message:
        # Get the message ID of the replied message
        replied_msg_id = message.reply_to_message.message_id
        # Generate a link using the message ID
        link = f"https://t.me/{message.chat.username}/{replied_msg_id}"
        # Reply to the user with the link
        await message.reply_text(f"Here's the link to the message: {link}")
    else:
        # If there is no replied message, inform the user
        await message.reply_text("Please reply to a message to generate the link.")

# Run the userbot
app.run()
