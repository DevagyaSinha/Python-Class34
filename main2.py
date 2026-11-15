keys={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

def count_combo(digits):
    if len(digits)==0:
        return 1
    return len(keys[digits[0]])*count_combo(digits[1:])

input("count_combo multiplies letter/choices ")
print("count_combo(2)=",count_combo('2'))
print("count_combo(23)=",count_combo('23'))



