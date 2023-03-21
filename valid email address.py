# To check valid email address

def check(mail):
    if '@' in mail and 'com' in mail:
        return True
    else:
        return False

def switch(result):
    switch = {
        True: "valid",
        False: "invalid"
    }
    return switch.get(result, "please confirm proper input")

# Test cases
print(switch(check("abc@gmail.com")))
print(switch(check("abc@.com")))
