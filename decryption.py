import sys

d = {'А': 'Ⱥ', 'Б': 'Ȼ', 'В': 'ȼ', 'Г': 'Ƚ', 'Д': 'Ⱦ', 'Е': 'ȿ', 'Ж': 'ɀ', 'З': 'Ɂ', 'И': 'ɂ', 'Й': 'Ƀ', 'К': 'Ʉ',
     'Л': 'Ʌ', 'М': 'Ɇ', 'Н': 'ɇ', 'О': 'Ɉ', 'П': 'ɉ', 'Р': 'Ɋ', 'С': 'ɋ', 'Т': 'Ɍ', 'У': 'ɍ', 'Ф': 'Ɏ', 'Х': 'ɏ',
     'Ц': 'ɐ', 'Ч': 'ɑ', 'Ш': 'ɒ', 'Щ': 'ɓ', 'Ъ': 'ɔ', 'Ы': 'ɕ', 'Ь': 'ɖ', 'Э': 'ɗ', 'Ю': 'ɘ', 'Я': 'ə', 'а': 'ɚ',
     'б': 'ɛ', 'в': 'ɜ', 'г': 'ɝ', 'д': 'ɞ', 'е': 'ɟ', 'ж': 'ɠ', 'з': 'ɡ', 'и': 'ɢ', 'й': 'ɣ', 'к': 'ɤ', 'л': 'ɥ',
     'м': 'ɦ', 'н': 'ɧ', 'о': 'ɨ', 'п': 'ɩ', 'р': 'ɪ', 'с': 'ɫ', 'т': 'ɬ', 'у': 'ɭ', 'ф': 'ɮ', 'х': 'ɯ', 'ц': 'ɰ',
     'ч': 'ɱ', 'ш': 'ɲ', 'щ': 'ɳ', 'ъ': 'ɴ', 'ы': 'ɵ', 'ь': 'ɶ', 'э': 'ɷ', 'ю': 'ɸ', 'я': 'ɹ'}

rev_d = {v: k for k, v in d.items()}

print('Введите текст: ')
string = sys.stdin.readlines()

for j in string:
    for i in j:
        if i in rev_d:
            print(rev_d[i], end='')
        else:
            print(i, end='')