from openpyxl import load_workbook

wb = load_workbook("rasp.xlsx")
week = "нечет"
clas = "10"
letter = "С"
letter = letter.upper()
args = {"week": week, "class": clas, "letter": letter}
rasp = wb[f'{args["class"]}-е кл {args["week"]}']
bigletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
column = ''
columnn = 0
for i in range(1000):
    if rasp[f"{bigletters[i]}9"].value == f"{clas}{letter}":
        column = bigletters[i]
        columnn = i
        break
raspisanie = '''
день                        |время| пара, кабинет, учитель
----------------------
'''
days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']


def para(value):
    global firstpara, secondpara, thirdpara, fourthpara
    if firstpara == '':
        firstpara = value
    elif secondpara == '':
        secondpara = value
    elif thirdpara == '':
        thirdpara = value
    elif fourthpara == '':
        fourthpara = value


count = 0
for j in range(6):
    firstpara = ''
    secondpara = ''
    thirdpara = ''
    fourthpara = ''
    paru = [11, 13, 16, 18, 21, 23, 26, 28, 31, 33, 36, 38, 42, 44, 47, 49, 52, 54, 57, 59, 62, 64, 67]
    for i in range(4):
        number = paru[count]
        if rasp[f'{column}{number}'].value == "нет":
            para(' ')
        elif rasp[f'{column}{number}'].value == None:
            if letter != "С":
                if rasp[f'{bigletters[columnn - 1]}{number}'].value == None:
                    para(' ')
                else:
                    para(f"{rasp[f'{bigletters[columnn - 1]}{number}'].value} {rasp[f'{bigletters[columnn - 1]}{number + 1}'].value}")
            else:
                para(' ')
        else:
            para(f"{rasp[f'{column}{number}'].value} {rasp[f'{column}{number + 1}'].value}")
        count += 1
        if count > 22:
            break
    if j == 5:
        raspisanie += f'''                            |08:45| {firstpara}
                            |10:45| {secondpara}          
{days[j]}               
                            |13:05| {thirdpara}
----------------------
'''
    else:
        raspisanie += f'''                            |08:45| {firstpara}
                            |10:45| {secondpara}          
{days[j]}               
                            |13:05| {thirdpara}
                            |14:55| {fourthpara}
----------------------
'''
print(raspisanie)
