from pyrogram import Client, filters
import asyncio
# Your session string

SESSION="BQGhN7YAnGlp1AAP3BLUcjoBJuDj7qXl68lDf46nsVZFwcAVmCOMxfR9QiUC8J8bqbWIkiaFZS099KcMyH02C_RpmwjB6OX-feFK_a_lvywO9zI_H1ABdfhsh5atbvvJwm_e2fqaYjxStbwZyOKedr2x2dbe7KoG5_MIVz3sZRqQpwwRaFcxxLIRQO_WLAunBIYeYNnBqHwunfxJMgyiOqIE1boe0FmSEejT5uPqAmPpstNppsw7dvGygVDAGtFQgd2TgM0weIquF5_5ZhceUswrQi-Mvc_5MF56r92cCMPLZtkfiB6zvPyo5fUKNVi_6vx2KDMqABcEXpingXTDqxl4zn0eVgAAAAF-8UZkAA"
#SESSION = "AQDJqkIAeRm_Rtdur4xDwf88Uroyo-SEr3xuRCd5PiOn71-p4kmVPPM4g9R1ck3U0Lfv6PzY0TQZQUWx1jh83dtI7aTe5aYRleqYmTIL4zcUbRHWF7VxpBfXC8qxVasScayBkc17311ODCJh6dNbqtvytK5zA3ypnWvuo5bLz-UOAIERm2HP2rjknu3k6-xzFAE3U4NvllO5Ke23C_MtgfXnohILOuwgMyq78jgaNMCvFeWyHEkNIYZ_I61zq9h5VioByuMa7_W4Jng20rqsoCD-fkgi5CngWOJmyodU3LB8srG7opdjqAljUA-khAA9rqgfeiex3HBH8L70qH0JonBQGhN7YAxW8nU5629EFPT-6RrgRMybJxHTAZbWn-RVbTnYuBqRtK2EIVZkaUl30r5Tsju7vq8cCbv7q39V6b8k7wxMhxsi6qQYAi5x36VKdOcPUoCMt7XTShhSDhvYY2HIOifWr3Kwj0SQ0Ye0X2u4M2MTeIn9sOtNSXhdtYZ5OO7ox9AdeL53SsCPVLR_xtyAxzKwM8oYcqYHWrSOJP4VX91eSjuh4OOAiA0CsN2SmUiXIQP1EncilvdngUNlAhKIVDqyJKN7gNJJxylvNL5XE0DCshvsPV1J5TCjuoM2qLusN35q9t0GZ1ww9sYc-nsYEDB2rvx4-CEyl6HLYhdAk78wutWAAAAAF-8UZkAA"
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
        await message.edit_text("Generating link...")
        await asyncio.sleep(1.5)
        #await message.delete()
        await message.edit_text(f"https://t.me/b/{chat_id}/{msg_id}")
    except Exception as e:
        print(f"An error occurred: {e}")


 #await client.edit_message_text(
 #   chat_id=message.chat.id,
 #   message_id=message.id,
 #   text="hello"
#)

# Run the userbot
app.run()
