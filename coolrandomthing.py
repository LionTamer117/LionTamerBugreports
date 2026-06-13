NPC_name = "[Carl]"
var1 = input(NPC_name,"hello whats ur name?")
print(NPC_name,"Oh",var1,"That sounds like a intresting name!")
while True:
    user_input = input("\n[System] Type in a command: ").strip()
    if user_input == "/help":
        print("\n--- Available Commands ---")
        print("- /npc name <string>  (Changes the NPC's name)")
        print("- /npc say <string>   (Makes the NPC talk)")
        print("- /exit               (Quits the program)")
        continue
    if user_input == "/exit":
        print("[System] Goodbye!")
        break
    if user_input.startswith("/npc name "):
       NPC_name = user_input[10:].strip()
        print(f"[System] NPC name changed to: {npc_name}")
        
    elif user_input.startswith("/npc say "):
        dialogue = user_input[9:].strip()
        print(f"[{NPC_name}]: \"{dialogue}\"")
    else:
        print("[System] Unknown command. Type /help for a list of commands.")
