# ключи шифрования:
# K --> M
# O --> Q
# E --> G
# расшифровать:

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb." \
    " rfyrq ufyr amknsrcpq ypc dmp." \
    " bmgle gr gl zw fylb gq glcddgagclr " \
    "ylb rfyr'q ufw rfgq rcvr gq qm jmle." \
    " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb." \
    " lmu ynnjw ml rfc spj."
# print(ord(s[3]))
# print(chr(109))
z = ""
b = "z"
for i in s:  # для каждого элемента из последовотельностей эс
    if i == " " or i == "(" or i == "'" or i == '.' or i == ')' or i == "a" or i == "_" or i == "|" or i == "{" or i == "`" or i == "}" or i == "~" or i == "":
        z += i
    elif i == "y":
        z += "a"
    elif i == "z":
        z += "b"
    else:
        z += chr(ord(i) + 2)
print(z)

print(ord("`"))
print(chr(39))
print(chr(127))
#a b c'