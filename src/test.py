from jobs import load_accounts, authenticate_user

# Load accounts
accounts = load_accounts()
print(f"✅ Loaded {len(accounts)} accounts\n")

# List all usernames
print("All usernames in system:")
for username in accounts.keys():
    print(f"  - {username}")

print("\n" + "="*50)
print("Testing Stuart's login...")
print("="*50)

# Check if Stuart exists
if "stuartbovesbanana" in accounts:
    stuart = accounts["stuartbovesbanana"]
    print(f"\n✅ Stuart found!")
    print(f"Stored username: '{stuart.username}'")
    print(f"Stored password: '{stuart.password}'")
    print(f"Name: {stuart.name}")
    print(f"Account: {stuart.account}")
    print(f"Balance: ${stuart.balance}")
else:
    print("\n❌ Stuart NOT found in accounts!")

print("\n" + "="*50)
print("Testing authentication...")
print("="*50)

# Test authentication
test_username = "stuartbovesbanana"
test_password = "99Banana!"

print(f"\nTrying to login with:")
print(f"  Username: '{test_username}'")
print(f"  Password: '{test_password}'")

result = authenticate_user(test_username, test_password, accounts)

if result:
    print(f"\n✅ LOGIN SUCCESS!")
    print(f"Welcome {result.name}!")
else:
    print(f"\n❌ LOGIN FAILED!")
    
    # Debug why it failed
    if test_username in accounts:
        stuart = accounts[test_username]
        print(f"\nDEBUG INFO:")
        print(f"Username exists: YES")
        print(f"Stored password: '{stuart.password}'")
        print(f"Typed password:  '{test_password}'")
        print(f"Passwords match: {stuart.password == test_password}")
        
        # Check character by character
        if stuart.password != test_password:
            print(f"\nPassword length - Stored: {len(stuart.password)}, Typed: {len(test_password)}")
            for i, (c1, c2) in enumerate(zip(stuart.password, test_password)):
                if c1 != c2:
                    print(f"  Position {i}: stored='{c1}' typed='{c2}' ❌")
    else:
        print(f"\nDEBUG INFO:")
        print(f"Username '{test_username}' does NOT exist in accounts")