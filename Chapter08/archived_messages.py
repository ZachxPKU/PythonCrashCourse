def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


messages = ['Hello, Zach!', '你好，志强！']
sent_messages = []
send_messages(messages[:], sent_messages)

print(messages)

print(sent_messages)