# 1. 문자를 입력받아 대소문자를 변경
# 대문자 -> 소문자, 소문자 -> 대문자

def convert_case(text):
    new_text = ""
    for t in text:
        if t.islower():
            new_text += t.upper()
        else:
            new_text += t.lower()
    return new_text

# def convert_case(text):
#     new_text = ""
#     i = 0

#     while i < len(text):
#         if text[i].islower():
#             new_text += text[i].upper()
#         else:
#             new_text += text[i].lower()
#         i += 1

#     return new_text
    
# print(convert_case('HellO'))
# print(convert_case('WelCOME'))
# print(convert_case('GoodBye'))
# print(convert_case('Good bye'))
# print(convert_case('This is long message, haha1234'))

def convert_case2(text):
    return ''.join([char.upper() if char.islower() else char.lower() for char in text])

print(convert_case2('HellO'))