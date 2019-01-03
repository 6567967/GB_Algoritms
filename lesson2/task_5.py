# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа
# под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
# https://drive.google.com/file/d/1dRO7fXCLV1LLGWruoj_rnoHU5a8pRIjH/view?usp=sharing

for i in range(32, 128):
    print(f"{i:3}-{chr(i)} ", end='')
    if (i-32+1) % 10 == 0:
        print("")
