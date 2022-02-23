import base64


def encode():
    message=input("Enter Characters:")
    message_bytes=message.encode("ascii")
    base64_bytes=base64.b64encode(message_bytes)
    base64_message=base64_bytes.decode("ascii")
    print(base64_message)


def decode():
    base64_message=input("Enter Characters:")
    base64_bytes=base64_message.encode("ascii")
    message_bytes=base64.b64decode(base64_bytes)
    message=message_bytes.decode("ascii")
    print(message)


while True:
    user_input=int(input("[1]Encode/[2]Decode/[3]Exit:"))
    if user_input==1:
        encode()
    elif user_input==2:
        decode()
    elif user_input==3:
        print("Quit")
        exit()
    else:
        print("Quit")
        exit()