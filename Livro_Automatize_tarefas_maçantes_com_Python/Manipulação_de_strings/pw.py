import sys, pyperclip

passwords = {
    "email": "carlosrjhoe@gmail.com",
    "blog": "carlosrjhoe@github.com.br",
    "luggage": "Python03",
}

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()
    
account = sys.argv[1]

if account == passwords:
    pyperclip.copy(passwords[account])
    print(f"Password for {account} copied to clipboard.")
else:
    print(f"there is no account named {account}")