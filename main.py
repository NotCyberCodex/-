import aminofix
from time import sleep

client = aminofix.Client()
client.parse_headers = lambda data=None, type=None: {**aminofix.headers.ApisHeaders(deviceId=aminofix.helpers.gen_deviceId() if client.autoDevice else client.device_id, data=data, type=type).headers, 'Host': 'service.aminoapps.com'}
email = input("𝗘𝗺𝗮𝗶𝗹 ➪ ")
password = input("𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 ➪ ")
client.login(email=email, password=password),

def invite_ndcs():
    myself_ndcs = client.sub_clients(size=100)
    for ndc_name, people_total, ndc_id in zip(myself_ndcs.name, myself_ndcs.usersCount, myself_ndcs.comId):
        sub_client = aminofix.SubClient(comId=ndc_id, profile=client.profile)
        
        only_online = sub_client.get_online_users(size=users_maximal)
        for users_name, users_id in zip(only_online.profile.nickname, only_online.profile.userId):
            try:
                sleep(frize_time)
                client.invite_to_chat(chatId=inside_id, userId=users_id)
                print(f"\nname users :  [{users_name}] \ninfo id :  [{users_id}] \ninvited with :  [{ndc_name}] \ninfo ndc :  [{ndc_id}] \nmembers :  [{people_total}]")
            except Exception as NotUserInvited:
                    print(NotUserInvited)
                    pass


def invite_npbl():
    others_ndcs = client.sub_clients(size=100)
    for name_ndc, memb_total, ndc_ld in zip(others_ndcs.name, others_ndcs.usersCount, others_ndcs.comId):
        ndc_client = aminofix.SubClient(comId=ndc_ld, profile=client.profile)
        
        share_threads = ndc_client.get_public_chat_threads(type="recommended", size=100).chatId
        acces_threads = ndc_client.get_public_chat_threads(type="latest", size=100).chatId
        store_threads = ndc_client.get_public_chat_threads(type="popular", size=100).chatId
        
        official_chats = [*share_threads, *acces_threads, *store_threads]
        
        for chat_ld in official_chats:
            chats_infos = ndc_client.get_chat_thread(chatId=chat_ld).json
            chat_name = chats_infos["title"]
            chat_membs = chats_infos["membersCount"]
            
            only_chats = ndc_client.get_chat_users(chatId=chat_ld, size=resize_users)
            for user_name, people_id in zip(only_chats.nickname, only_chats.userId):
                try:
                    sleep(pause_time)
                    client.invite_to_chat(chatId=ethernal_id, userId=people_id)
                    print(f"\nname_user :  [{user_name}] \ninfo id :  [{people_id}] \ninvited with : [{name_ndc}] \ninfo ndc : [{ndc_ld}] \nmembers ndc :  [{memb_total}] \ninvite with :  [{chat_name}] \ninfo chat :  [{chat_membs}] - members in chat")
                except Exception as NotInvPubl:
                      print(NotInvPubl)
                      pass


advanced_invite = int(input('''
1.Inside Invite [Global][With all ndc]
2.Eternal invite [Global[all ndc][pblc th]

choose function :  '''))

if advanced_invite == 1:
    inside_threads = client.get_chat_threads(size=100)
    for inside_num, title in enumerate(inside_threads.title, 1):
        print(f"[{inside_num}].[{title}]")
    inside_id = inside_threads.chatId[int(input("Choose my chat :  ")) -1]
    client.edit_chat(chatId=inside_id, viewOnly=True)
    
    users_maximal = int(input("How many invited users, only one ndc :  "))
    frize_time = int(input("Time for freeze script :  "))
    invite_ndcs()
    
elif advanced_invite == 2:
    ethernal_threads = client.get_chat_threads(size=100)
    for ethernal_num, title in enumerate(ethernal_threads.title, 1):
        print(f"[{ethernal_num}].[{title}]")
    ethernal_id = ethernal_threads.chatId[int(input("Choose my thread :  ")) -1]
     
    client.edit_chat(chatId=ethernal_id, viewOnly=True)
    resize_users = int(input("How many invited users, only one ndc and one pbl thread :  "))
    pause_time = int(input("How many time waitings :  "))
    invite_npbl()

else:
    checker_ndc = int(input("How in ndc checked :  "))
    teg_all_ndc = client.sub_clients(size=checker_ndc)
    for cn_name, cn_id in zip(teg_all_ndc.name, teg_all_ndc.comId):
        check_client = aminofix.SubClient(comId=cn_id, profile=client.profile)
        try:
            check_client.check_in(tz=100)
            print(f"\nmarked in :  [{cn_name}] \info cn :  [{cn_id}]")
        except Exception as CheckError:
            print(CheckError)
            pass
            
