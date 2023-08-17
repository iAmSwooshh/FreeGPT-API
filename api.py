#___________________________________________           #_____________________________    _____ __________.___ 
#\_   _____/\______   \_   _____/\_   _____/          /  _____/\______   \__  #  ___/   /  _  \\______   \   |
 #|    __)   |       _/|    __)_  |    __)_   ______ /   \  ___ |     ___/ |    |     /  /_\  \|     ___/   |
 #|     \    |    |   \|        \ |        \ /_____/ \    \_\  \|    |     |    |    /    |    \    |   |   |
 #\___  /    |____|_  /_______  //_______  /          \______  /|____|     #|____|    \____|__  /____|   |___|
     #\/            \/        \/         \/                  \/                              \/              

# YOU ARE ALLOWED TO USE THIS CODE ANYWHERE PASTERS


import requests

url = "https://chatgpt.ai/wp-admin/admin-ajax.php"

headers = {
    "Content-Type": "multipart/form-data; boundary=---------------------------16082485041676678739315451361"
}

payload_template = '''-----------------------------16082485041676678739315451361
Content-Disposition: form-data; name="_wpnonce"

894f198f58
-----------------------------16082485041676678739315451361
Content-Disposition: form-data; name="post_id"

1048
-----------------------------16082485041676678739315451361
Content-Disposition: form-data; name="url"

https://chatgpt.ai
-----------------------------16082485041676678739315451361
Content-Disposition: form-data; name="action"

wpaicg_chat_shortcode_message
-----------------------------16082485041676678739315451361
Content-Disposition: form-data; name="message"

{user_input}
-----------------------------16082485041676678739315451361
Content-Disposition: form-data; name="bot_id"

14562
-----------------------------16082485041676678739315451361--
'''

# comment the input and use a string variable if you want to do it using strings/definite data  
user_input = input("Enter your message: ") 
payload = payload_template.format(user_input=user_input)

response = requests.post(url, headers=headers, data=payload)
data = response.json()["data"]

print(f"Reply: {data}")
