# -*- coding: utf-8 -*-
# Assignment of Variables
v_Word = 'AB4DF8H2'
#v_Word = 'AB4DF8HZR5FJK26*MWQ9XR$3RTY7EGHJ'
v_Char = ''
v_Pos = 0
v_Num = 0

# print(len(vWord))
# begin selet each invidual alphanumeric and loop
# 
while v_Pos < len(v_Word):
    v_Char = v_Word[v_Pos:v_Pos+1]
    print(v_Char)

    if ord(v_Char) >= 48 and ord(v_Char) <= 57:
       
        v_Num = v_Num + int(v_Char)

    v_Pos = v_Pos +1
#    print(v_Pos)
#  reveal the summation of all numbers in string
print('The hidden code is ' + str(v_Num))
#   End of Program