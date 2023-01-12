# Аве, Цезарь 🌶️
#
# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.
#
# Формат входных данных
# На вход программе подается строка текста на английском языке.
#
# Формат выходных данных
# Программа должна вывести зашифрованный текст в соответствии с условием задачи.
#
# Примечание. Символы, не являющиеся английскими буквами, не изменяются.

# put your python code here
en = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input()
st = []
tmp = ""
for c in s :
    if c in en : tmp = tmp + c
    elif tmp == "" : st.append(c)
    else :
        st.append(tmp)
        st.append(c)
        tmp = ""
if tmp != "" : st.append(tmp)
tmp = ""
for i in range(len(st)) :
    if st[i].isalpha() :
        count = len(st[i])
        for c in st[i] :
            n = ord(c.lower()) + count
            if n > 122 : n = n - 26
            if c.isupper() : tmp = tmp + chr(n).upper()
            else : tmp = tmp + chr(n)
        st[i] = tmp
        tmp = ""
print(*st, sep = '')