from string import ascii_lowercase, punctuation
def pangrams(s):
    # Write your code here
    s = s.lower()
    count_dict = {alpha: 0 for alpha in ascii_lowercase}
    for ch in s:
        if ch not in punctuation and ch != ' ':
            count_dict[ch] +=1
    count_alpha = list(count_dict.values())
    print(count_alpha)
    if count_alpha.count(0)>0:
        return "not pangram"
    else:
        return "pangram"