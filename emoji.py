import emoji
def emoji_func(text):
    return emoji.emojize(text)

user_input=input('Enter text to generate emoji: ')
gen_emoji=emoji_func(user_input)
print('final results: ',gen_emoji)