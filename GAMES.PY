import random
import time

def start_game():
  
    player_credits = 0
    decryption_software = 1
    stealth_software = 1
    
  
    alert_level = 0
    database_breached = False
    #learning git with vscode.
    print("=" * 50)
    print(" SYSTEM INITIALIZED: WELCOME BACK, NETRUNNER. ")
    print("=" * 50)
    print("Your objective: Breach the secure database before Alert hits 100%.")
    time.sleep(1)

    while alert_level < 100 and not database_breached:
        print(f"\n--- [ STATUS: Alert Level: {alert_level}% | Credits: ${player_credits} ] ---")
        print("Choose your action:")
        print("1. [Scan Network] - Find weak nodes and harvest minor data (Low Risk)")
        print("2. [Crack Firewall] - Attacking core database (High Risk / High Reward)")
        print("3. [Clear Logs] - Spend credits to lower the system alert level")
        print("4. [Black Market] - Upgrade your hacking software tools")
        print("5. [Disconnect] - Abort mission and flee")

        choice = input("\nSelect action (1-5): ")

       
        if choice == "1":
            credits_earned = random.randint(10, 30) * decryption_software
            added_alert = max(5, random.randint(5, 15) - stealth_software)
            
            player_credits += credits_earned
            alert_level += added_alert
            
            print(f"\n[SUCCESS] Node bypassed! Siphoned ${credits_earned} from data packets.")
            print(f"[WARNING] Traces left. Alert increased by +{added_alert}%.")

       
        elif choice == "2":
            print("\n[ALERT] Bypassing security matrix... Enter the override code!")
           
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            correct_answer = num1 * num2
            
            start_time = time.time()
            user_answer = input(f"CRITICAL LOCK: What is {num1} x {num2}? ")
            end_time = time.time()
            
          
            if user_answer.isdigit() and int(user_answer) == correct_answer and (end_time - start_time) < 6:
                success_chance = random.randint(1, 100)
              
                if success_chance + (decryption_software * 10) >= 75:
                    database_breached = True
                else:
                    alert_level += 25
                    print(f"\n[PARTIAL SUCCESS] Firewall damaged, but core still locked. Alert jumped +25%.")
            else:
                alert_level += 40
                print(f"\n[BREACH FAILED] Security protocol triggered! Heavy tracing. Alert jumped +40%.")

    
        elif choice == "3":
            if player_credits >= 50:
                player_credits -= 50
                reduction = random.randint(15, 30)
                alert_level = max(0, alert_level - reduction)
                print(f"\n[CLEARED] Proxies rerouted. Reduced alert by -{reduction}%. Cost: $50.")
            else:
                print("\n[ERROR] Insufficient funds! You need at least $50 to scrub logs.")

        
        elif choice == "4":
            print(f"\n--- BLACK MARKET SHOP (Current Credits: ${player_credits}) ---")
            print(f"1. Decryption Rig (Current: Lvl {decryption_software}) -> Cost: $100")
            print(f"2. Stealth Cloak  (Current: Lvl {stealth_software}) -> Cost: $100")
            print("3. Exit Shop")
            
            shop_choice = input("Select upgrade (1-3): ")
            if shop_choice == "1" and player_credits >= 100:
                player_credits -= 100
                decryption_software += 1
                print(f"[UPGRADED] Decryption Rig is now Level {decryption_software}!")
            elif shop_choice == "2" and player_credits >= 100:
                player_credits -= 100
                stealth_software += 1
                print(f"[UPGRADED] Stealth Cloak is now Level {stealth_software}!")
            else:
                print("\n[EXIT] Leaving black market.")

     
        elif choice == "5":
            print("\n[LOGOUT] Jacking out safely. Mission aborted.")
            break

        else:
            print("\n[INVALID INPUT] Command not recognized.")
            
        time.sleep(1.5)

 
    if database_breached:
        print("\n" + "=" * 50)
        print(" ACCESS GRANTED: DATABASE SECURED! ")
        print("=" * 50)
        print(f"Excellent work, Netrunner. You escaped with ${player_credits} in clean currency.")
    elif alert_level >= 100:
        print("\n" + "=" * 50)
        print(" SYSTEM LOCKDOWN: YOU WERE TRACED! ")
        print("=" * 50)
        print("The corporation traced your IP. Tactical teams are en route. GAME OVER.")


start_game()
