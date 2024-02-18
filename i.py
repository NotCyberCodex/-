import aminofixed

from os import _exit as finished_script
from threading import Thread
from colored import fore, style, attr
from pyfiglet import Figlet


client = aminofixed.Client()
ghost_post = "goiod241@proton.me"
ghost_offence = input("Password :  ")
client.login(email=ghost_post, password=ghost_offence)

print(f'''
[1].Mix Invite from ndc in cnd[mix][ndc]
[2].Mix Invit Inside from ndc in cnd[inside]
[3].Ultime Invite from ndc in publy cnd[pb]

utiles for :  [{client.profile.nickname}]
''')
utiles_master = int(input("Function :  "))

def fast_invite():
		while True:
			set_users = sub_client.get_online_users(start=0, size=showed_users).profile.userId
			sets_members = sub_client.get_all_users(type="recent", start=0, size=showed_users).profile.userId
			sets_membs = [*set_users, *sets_members]
			for total_set in sets_membs:
				try:
					sub_client.invite_to_chat(userId=[sub_client.profile.userId, total_set], chatId=chat_id)
					members_info = sub_client.get_user_info(userId=total_set).json
					name_user = members_info["nickname"]
					exp_user = members_info["reputation"]
					print(f'''
Invited :  {name_user}
user info :  {exp_user}
''')
				except Exception as NotUsersInvited:
					print(NotUsersInvited)
					continue
				
def inside_invite():
		while True:
			internal_users = sub_client.get_online_users(start=0, size=displayed_users).profile
			for inside_name, exp_user, user_Id in zip(internal_users.nickname, internal_users.reputation, internal_users.userId):
				try:
					client.invite_to_chat(userId=[client.profile.userId,user_Id], chatId=chat_Id)
					print(f'''
invited :  {inside_name}
info user :  {exp_user}
main info :  {user_Id}
''')
				except Exception as InviteRequestDisabled:
					print(InviteRequestDisabled)
					continue
					
def ultimate_Invite():
				while True:
					ultimes_users = sub_client.get_online_users(start=0, size=ultime_nums).profile
					for ultime_name, expl_info, ultim_id in zip(ultimes_users.nickname, ultimes_users.reputation, ultimes_users.userId):
						try:
							sub_client.invite_to_chat(userId=[sub_client.profile.userId, ultim_id], chatId=chat_ld)
							
						except Exception as RequestInvDisabled:
							print(RequestInvDisabled)
							continue							

if utiles_master == 1:
				try:	
					ndc_list = client.sub_clients(start=0, size=100)
					for nums, name in enumerate(ndc_list.name, 1):
						print(f"Ndc :  {nums} - [{name}]")
					ndc_id = ndc_list.comId[int(input("Ndc number :  ")) -1]
					sub_client = aminofixed.SubClient(comId=ndc_id, profile=client.profile)
					cnd_list = sub_client.get_chat_threads(start=0, size=100)
					for numsy, title in enumerate(cnd_list.title, 1):
						print(f"Chat :  {numsy} - [{title}]")
					chat_id = cnd_list.chatId[int(input("Chat number :  ")) -1]
					
					showed_users = int(input("How many invire users :  "))
		
					for _ in range(int(input("Thread numb[1-slow[infinity] 2- fast [replie] :  "))):
						Thread(target=fast_invite).start()
				except Exception as InvalidOperation:
						print(InvalidOperation)
						finished_script(1)
						
elif utiles_master == 2:
				try:
					ndc_sorts = client.sub_clients(start=0, size=100)
					for number, name in enumerate(ndc_sorts.name, 1):
						print(f"Community :  {number} - [{name}]")
					ndc_Id = ndc_sorts.comId[int(input("Ndc number :  ")) -1]
					sub_client = aminofixed.SubClient(comId=ndc_Id, profile=client.profile)
					
					inside_list = client.get_chat_threads(start=0, size=50)
					for numery, title in enumerate(inside_list.title, 1):
						print(f"Rooms :  {numery} - [{title}]")
					chat_Id = inside_list.chatId[int(input("Room number :  ")) -1]
					
					displayed_users = int(input("How many invite people :  "))
					
					for _ in range(int(input("Thread :  [1 - slow[2 - fast[replie] :  "))):
						Thread(target=inside_invite).start()
				
				except Exception as OperationError:
					print(OperationError)
					finished_script(2)

elif utiles_master == 3:
					try:
						sets_ndc = client.sub_clients(start=0, size=100)
						for num_bility, name in enumerate(sets_ndc.name, 1):
							print(f"Community :  {num_bility} - [{name}]")
						ndc_ld = sets_ndc.comId[int(input("Community number :  ")) -1]
						sub_client = aminofixed.SubClient(comId=ndc_ld, profile=client.profile)
						
						chat_sets = sub_client.get_public_chat_threads(type="recommended", start=0, size=50)
						for num_obility, title in enumerate(chat_sets.title, 1):
							print(f"Public chat :  {num_obility} - [{title}]")
						chat_ld = chat_sets.chatId[int(input("Enter chat :  ")) -1]
						sub_client.join_chat(chatId=chat_ld)
						print(f"Join to :  [{chat_ld}]")
						
						ultime_nums = int(input("How many invite online users :  "))
						
						for _ in range(int(input("Thread :  [1-slow[normaly] [2-fast _ replie] :  "))):
							Thread(target=ultimate_Invite).start()
						
					except Exception as InvalidateOperation:
							print(InvalidateOperation)
							finished_script(3)
					
else:
		print(f"Function : [{utiles_master}] not finded! Please enter 1 or 2 or 3 in next launch script!")
		finished_script(4)
		
					
		
