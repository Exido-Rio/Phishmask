import requests,re

#Devloped by Exido-Rio 
#just for educational purpose 
#you will be responsible for any misuse of this tool

regex = re.compile( # used by the django
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


print("""                   Welcome to

██████  ██   ██ ██ ███████ ██   ██ ███    ███  █████  ███████ ██   ██ 
██   ██ ██   ██ ██ ██      ██   ██ ████  ████ ██   ██ ██      ██  ██  
██████  ███████ ██ ███████ ███████ ██ ████ ██ ███████ ███████ █████   
██      ██   ██ ██      ██ ██   ██ ██  ██  ██ ██   ██      ██ ██  ██  
██      ██   ██ ██ ███████ ██   ██ ██      ██ ██   ██ ███████ ██   ██ 
""")

ur = "https://is.gd/create.php"

useable = lambda j:str(re.search('<div id="main"><p><b>Your shortened URL is:</b></p><input type="text" class="tb" id="short_url" value=[^>]+>', j.text).group(0)).partition('value="')[-1].split('"')[0].split("//")[-1]

assert bool(re.match(regex,main_url:=input("Enter the url to masked (ex:= your tunnel url of ngrok,localtunel etc) : ")) is not None)==True ,"Not a valid url"

assert bool(re.match(regex,mask_url:= input("Enter the legit url used as a cover : ")) is not None) ,"Not a valid url"

print("Processing ...............")


def call(link):
    short = requests.post(ur,data={'url':link})
    print('Successful') if (x:=short.status_code) == 200 else print(f"Error occourd :{x}")
    return short

decive_str = input("Enter the extra tag to be added (ex:=best vedio wow  etc):")

final=(zen:=lambda s : s.split("//")[0]+"//" + matches[0].split('/')[2]  if (matches:=re.findall(r'https?://[^\s/$.?#].[^\s]*', s)) else None)(zen(mask_url))+'-'+decive_str.replace(' ','-')+'@'+ useable(call(main_url))

print(f"Here is your url :{final} ")

print("Happy Hunting > ")

print("<3")
