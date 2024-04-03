# create by Mr. Pstar7
import re, requests, json, random, time, os, sys, string
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
Z = random.choice([P,M,H,K,B,U,O,N])

ses = requests.Session()
ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"


def login():
    print(f"{O} Masukkan cookie Instagram untuk melanjutkan!")
    coki = input(f"\n {H}? cookie : ") + ";"
    open(".cookie_ig.txt", "w").write(coki)
    try:
        hd = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3"
        }
        ck = {"cookie": coki}
        id = re.findall("ds_user_id=(\d+);", str(coki))[0]
        po = ses.get(
            f"https://i.instagram.com/api/v1/users/{id}/info/", headers=hd, cookies=ck
        )
        info = json.loads(po.text)
        if "full_name" in str(info):
            mulai()
        elif "challenge_required" in str(info):
            exit(f" {K}akun checkpoint")
        else:
            print(f"{M} cookie invalid atau perangkat spam")
            exit()
    except Exception as e:
        exit(f" {M}terjadi kesalahan")


def mulai():
    try:
        coki = open(".cookie_ig.txt", "r").read()
    except:
        login()
    try:
        hd = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3"
        }
        ck = {"cookie": coki}
        id = re.search("ds_user_id=(\d+)", str(coki)).group(1)
        po = ses.get(
            f"https://i.instagram.com/api/v1/users/{id}/info/", headers=hd, cookies=ck
        )
        info = json.loads(po.text)
        if "full_name" in str(info):
            try:
                nama = info["user"]["full_name"].split(" ")[0].lower()
            except:
                nama = info["user"]["full_name"].lower()
            uid = info["user"]["pk"]
        else:
            login()
    except Exception as e:
        login()
    os.system('clear' if 'Linux' in sys.platform.capitalize() else 'cls')
    print(
        f"""
                             {M}  @@@@@@@@@%%@@@@@@@@@
                           @@@#-:.              .:-#@@@
                       @@@*.                          .*@@@
                    @@@=.                                .=@@@
                  @@#.                                      .%@@
                @@*                                            *@@
               @#.                   ........                   .%@
             @@-     -%*.      .:-:--::::::::--:-:.      .*#-     -@@
            @@.  .-#@@:     .-:..::. ::.::.:: .::..:-.     :@@*-.  .@@
           @%. -@:%@%-   .::::..:.  .-. :: .-.  .-..::::.  .-%@%-@: .%@
          @%..-@#=%.%-  .:.   :::-:::...+*-..:::-::.   .:.  -%.%=#@-..%@
         @@.:=#@--@@- .:.    .:.   .-.+@=:@@.-.   .:.    .:. =@@--@#=: @@
        @@..@-##@@=  .-.    .-.    .:  .:=@* :.    .-     .-. .=@@##-@..@@
        @* *@+*@-=% .--:....:.     :.   :+   .:     .:....:--. %=-@*+@* *@
       @@. %@*-+@@. :.  ...:-:::...-    --    -...:::-:...  .:..@@=-#@# .@@
       @#.*-@*#@%. .:      ::     .-...:@@:...-.     :.      :. .%@#*@-+ #@
       @+.@.%#@=-..-.     .-.     .-    ::    :.     .:      .: :-=@#@ @.+@
       @-:@=:@-=@ .-.     .-.     .- -+@@@@+- :.      -.     .-. @=-@.=@:-@
       @-.@@--+@* .----------------#@* .%%. #@#----------------. *@+=-@@.-@
      {P} @- +@@:@@. .-.     .-.@@@@@@@@. :==: .@@@@@@@@.-.     .-. :@@:@@+ =@
       @+:.#@*@+--.-.      -%@@@@@@@@.  %%  .@@@@@@@@%:      .: ==+@*@#::+@
       @#.@.-@@.#% .:      :@@@@@@@@@- .@@. -@@@@@@@@@:     .:. %*:@@:.@.#@
       @@.*@*.%.@@  :.  ...=@@@@@@@@@@::@@.:@@@@@@@@@@=...  .:. @@.%.#@+.@@
        @*.+@@+:@@.+.--:.. -@@@@@@@@@@@=@@-@@@@@@@@@@@-...:--.*.@@:+@@+.*@
        @@. :@@##@:*%.-.   @@@@@@@@@@@@@@@@@@@@@@@@@@@%   .-.%*:@#%@@: .@@
         @@.#-:#@@*:@#.:. .@@@@@@@@@@@@@@@@@@@@@@@@@@@@. .:.#@:#@@#:-# @@
          @%.#@=.:%.@@=..::@@@@@@@@@@@@@@@@@@@@@@@@@@@@::..=@@.%:.=@#.@@
           @%.:@@@%=:@@:@=-@@@@@@@@@@@@@@@@@@@@@@@@@@@@-=%:@@:=%@@@:.%@
            @@. .#@@@%%%:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:%%%@@@#. .@@
             @@-.+=..-+*#-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-#*+-..=+ -@@
               @% .*@@@@@@@@#%@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@+..%@
                @@*. .:=+*+=:.:*@@@@@@@@@@@@@@@@@@*:.:=+*+=:. .*@@
                  @@#..+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+..%@@
                    @@@=. .:-:.-@@@@@@@@@@@@@@@@@@-.:-:. .=@@
                       @@@*.   =@@@@@@@@@@@@@@@@@@=   .*@@@
                           @@@##@@@@@@@@@@@@@@@@@@##@@@
                               @@@@@@@@@@@@@@@@@@@@
             {M} ___ _   __ ___ _____  _    ___  ____      _    __  __
             |_ _| \ | / ___|_   _|/ \  / ___|  _ \    / \  |  \/  |
              | ||  \| \___ \ | | / _ \| |  _| |_) |  / _ \ | |\/| |
              | || |\  |___) || |/ ___ \ |_| |  _ <  / ___ \| |  | |
             |___|_| \_|____/ |_/_/   \_\____|_| \_\/_/   \_\_|  |_|
 
                                                                                                                        {O}===[ {M}CODED BY {O}]===
                                 {M} ꧁{P}Mr. Pstar7{M}꧂
                     
                                 {B} version 0.09 {N}'''

	"""
    )
    print(f"\t {O}[ {U}HAI {H}{nama} {O}] ")
    print(
        f"""
{H}  1. unfollow yang tidak follow back
  2. unfollow masal
  3. Hubungi author 
  {M}4. LogOut
  """
    )

    apa = input(f"{N} input : ")
    if apa in ["1", "01"]:
        nofb(uid, coki)
    elif apa in ["2", "02"]:
        mass(uid, coki)
    elif apa in ["3", ",03"]:
       text = 'Assalamualaikum+warahmatullahi+wabarakatuh'
       os.system(f'xdg-open https://wa.me/+6285728337030?text={text}')
    else:
        os.remove(".cookie_ig.txt")


def mass(uid, coki):
    csrf_token = "".join(random.choices(string.ascii_letters + string.digits, k=32))
    match = re.search(r"csrftoken=(\w+)", coki)
    csrftoken = match.group(1)
    head = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "dpr": "1.30208",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua": ua,
        "sec-ch-ua-full-version-list": ua,
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"15.0.0"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "viewport-width": "1475",
        "x-asbd-id": "129477",
        "x-csrftoken": csrftoken,
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": get_hmac(),
        "x-instagram-ajax": "1009977574",
        "x-requested-with": "XMLHttpRequest",
        "x-web-device-id": "25532C62-8BBC-4927-B6C5-02631D6E05BF",
        # "cookie": f"dpr=1.3020833730697632; csrftoken={csrf_token}",
        "Referer": "https://www.instagram.com/alifxynn",
        "Referrer-Policy": "strict-origin-when-cross-origin",
    }

    lo = requests.get(
        f"https://www.instagram.com/api/v1/friendships/{uid}/following/?count=100",
        headers=head,
        cookies={"cookie": coki},
    )
    for x in json.loads(lo.text)["users"]:
        print()
        print(" + ", x["username"])
        x = x["username"]
        akun = requests.get(
            f"https://i.instagram.com/api/v1/users/web_profile_info/?username={x}",
            headers=head,
            cookies={"cookie": coki},
        ).json()["data"]["user"]["id"]
        gas(akun, x, coki)
        time.sleep(10)
    exit(" * selesai\n  \__[ ©alifxynn/zhukov-z ] ")


def nofb(uid, coki):
    csrf_token = "".join(random.choices(string.ascii_letters + string.digits, k=32))
    match = re.search(r"csrftoken=(\w+)", coki)
    csrftoken = match.group(1)
    head = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "dpr": "1.30208",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua": ua,
        "sec-ch-ua-full-version-list": ua,
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"15.0.0"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "viewport-width": "1475",
        "x-asbd-id": "129477",
        "x-csrftoken": csrftoken,
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": get_hmac(),
        "x-instagram-ajax": "1009977574",
        "x-requested-with": "XMLHttpRequest",
        "x-web-device-id": "25532C62-8BBC-4927-B6C5-02631D6E05BF",
        # "cookie": f"dpr=1.3020833730697632; csrftoken={csrf_token}",
        "Referer": "https://www.instagram.com/alifxynn",
        "Referrer-Policy": "strict-origin-when-cross-origin",
    }

    lo = requests.get(
        f"https://www.instagram.com/api/v1/friendships/{uid}/following/?count=100",
        headers=head,
        cookies={"cookie": coki},
    )  # followers
    for x in json.loads(lo.text)["users"]:
        print()
        print(" + ", x["username"])
        x = x["username"]
        lok = requests.get(
            f"https://www.instagram.com/api/v1/friendships/{uid}/followers/?count=100",
            headers=head,
            cookies={"cookie": coki},
        )
        if x in lok.text:
            print(f"  {M}+ {x} sudah follow back")
            pass
        else:
            akun = requests.get(
                f"https://i.instagram.com/api/v1/users/web_profile_info/?username={x}",
                headers=head,
                cookies={"cookie": coki},
            ).json()["data"]["user"]["id"]
            gas(akun, x, coki)
        time.sleep(10)
    exit(" * selesai\n  {H}\__[ ©alifxynn/zhukov-z ] ")


def get_hmac():
    rc = random.choices
    A = "".join(
        rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=17)
    )
    B = "".join(
        rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=10)
    )
    C = "".join(
        rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=10)
    )
    D = "".join(
        rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=7)
    )
    return f"hmac.{A}-{B}-{C}-{D}-"


def gas(user, x, coki):
    csrf_token = "".join(random.choices(string.ascii_letters + string.digits, k=32))
    match = re.search(r"csrftoken=(\w+)", coki)
    csrftoken = match.group(1)
    body_json = {
        "container_module": "profile",
        "nav_chain": f"PolarisProfileRoot:profilePage:1:via_cold_start",
        "user_id": user,
    }
    head = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "dpr": "1.30208",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua": ua,
        "sec-ch-ua-full-version-list": ua,
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"15.0.0"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "viewport-width": "1475",
        "x-asbd-id": "129477",
        "x-csrftoken": csrftoken,
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": get_hmac(),
        "x-instagram-ajax": "1009977574",
        "x-requested-with": "XMLHttpRequest",
        "x-web-device-id": "25532C62-8BBC-4927-B6C5-02631D6E05BF",
        # "cookie": f"dpr=1.3020833730697632; csrftoken={csrf_token}",
        "Referer": "https://www.instagram.com/alifxynn",
        "Referrer-Policy": "strict-origin-when-cross-origin",
    }

    http_response = ses.post(
        f"https://www.instagram.com/api/v1/friendships/destroy/{user}/",
        headers=head,
        data=body_json,
        cookies={"cookie": coki},
    )
    following_status = http_response.json()["friendship_status"]["following"]
    if isinstance(following_status, bool):
        if following_status:
            print(f"  {M}\__[ gagal unfol {x} ]")
        else:
            print(f"  {H}\__[ done unfol {x} ]")


os.system("clear")
mulai()
