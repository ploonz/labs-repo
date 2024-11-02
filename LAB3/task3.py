# TODO  Напишите функцию count_letters
def count_letters(text):
    slv=text.lower()
    letters=[]
    for i in range(len(slv)):
        if slv[i].isalpha():
            letters.append(slv[i])
    return letters
# TODO Напишите функцию calculate_frequency
def calculate_frequency(text):
 all_letters=count_letters(text)
 usedlet=[]
 for i in range(len(all_letters)):
     if all_letters[i] not in usedlet:
      usedlet+=all_letters[i]
 freq={}
 for index, letter in enumerate(usedlet):
     currentfreq="%.2f"%(all_letters.count(letter)/len(all_letters))
     freq[letter]=currentfreq
 return freq
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
freq=calculate_frequency(main_str)
for key,value in freq.items():
    print(f"{key}:",value)