"""
Engagify: Twitter Bot
author: samuel
type: bot
description: Automatically extracts and engages with Twitter links from text messages
2024


TEXT CAN TAKE ANY FORMAT
All twitter links are automatically extracted and reply is sent to them individually

Example usage: 
Text copied directly from Whatsapp:
tweet_urls = '''
[4/18, 10:54 AM] +234 706 066 7130: https://twitter.com/lovelytee110/status/1780888092104171726?t=B7yTn82gFCSVkA0BLRvkxg&s=19

Royal @lovelytee110
[4/18, 10:59 AM] +234 708 721 9781: https://twitter.com/SaikiFaith/status/1780898844168933770?t=lq2kKGn5-NGNFvEh8_YWKQ&s=19


Banzthehustla @saikifaith
[4/18, 10:59 AM] +234 903 192 5524: https://twitter.com/Jefferyidi/status/1780861746871218371?t=XbiX15awV7mFNS9u5ppKLg&s=19

@Jefferyidi
[4/18, 10:59 AM] +234 803 240 2584: https://x.com/OUhunmwang8433/status/1780854006685880572
OUhunmwang8433
[4/18, 11:00 AM] +234 905 531 2220: https://x.com/lil_petite3/status/1780892079243055350?s=46

Lil_petite3
[4/18, 11:00 AM] +234 703 684 2131: https://twitter.com/elzipoking/status/1780885921966997713?t=G_GuCvTwLO_cakuKzi-Vmw&s=19
 
Elzipoking
[4/18, 11:00 AM] +234 901 645 9708: https://x.com/Tomtom_dark/status/1780895090816188663

@Tomtom_dark
[4/18, 11:00 AM] +234 817 389 8301: https://twitter.com/Benjidex01/status/1780896065987674218?t=_5G8ncC2lT07fhRbF7tI1w&s=19

Benjamin@ Benjidex01
[4/18, 11:01 AM] +234 818 344 6169: https://x.com/youngnewton07/status/1780628205612711960.    @youngnewton07
[4/18, 11:01 AM] +234 706 425 0557: https://x.com/Tsojon1234/status/1780862426939855359
@tsojon1234
[4/18, 11:01 AM] +234 806 870 5374: https://twitter.com/asst_comrade/status/1780899487419920842?t=26iCHi3i58gRE7MG_HXiNw&s=19
[4/18, 11:01 AM] +234 901 349 3058: https://x.com/kingtrillz321/status/1780895980302303341?s=46

@kingtrillz321
[4/18, 11:03 AM] +234 906 658 0672: https://x.com/kruujack/status/1780899771797962885?s=46

@kruujack
[4/18, 11:03 AM] +234 904 667 6319: https://twitter.com/JoSeehua/status/1780883101838614957?t=fjL_oFbRE7bqp1o2kcK_IQ&s=19

@JoSeehua 
[4/18, 11:05 AM] +234 902 887 5832: https://x.com/_eudera/status/1780900107371577741?s=46

Pls do well to leave only this ticket *@senderLabs*  in the comments section I’d appreciate that 

Eudera @_eudera
[4/18, 11:06 AM] +234 701 131 4503: https://x.com/esosa_idemudia/status/1780857688240296411?s=46

@esosa_idemudia
[4/18, 11:08 AM] +234 903 411 6803: https://twitter.com/SylvaChurchill/status/1780895866686939190?t=3FOaHICqcdlYrtVG54dfcw&s=19
@sylvachurchill
[4/18, 11:09 AM] +234 813 068 3474: https://twitter.com/Jamesis72478271/status/1780901015107072417?t=2bbwQ5ekFsoGBgrlZwOYHQ&s=19


Jamesis @Jamesis72478271
'''

auto_reply(links, reply)
"""

from app.bot import auto_reply

if __name__ == "__main__":
    print("---------------------------------")
    print("Welcome To Engagify")
    links = input("Paste text containing the Twitter post links here")
    reply = input("What reply would you like to send? ")

    auto_reply(links, reply)