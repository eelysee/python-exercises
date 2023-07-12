

def is_two(l):
    two = 'two'
    if l.lower().strip() == two or l == 2 or l == '2':
        return True
    else:
        return False

def is_vowel(a):
    v = ['a', 'e', 'i' , 'o' , 'u']
    if a in v:
        return True
    else:
        return False
    
def is_consonant(b):
    v = ['a', 'e', 'i' , 'o' , 'u']
    if b not in v:
        return True
    else:
        return False
    
def proper_c(w):
    v = ['a', 'e', 'i' , 'o' , 'u']
    if w[0] not in v:
        return w.capitalize()
    else:
        return w
    
def calculate_tip(tip, bill):
   return tip * bill

def apply_discount(original_price, discount):
   return original_price - (original_price * discount)

def handle_commas(big_num):
    return big_num.replace(',', '')

def get_letter_grade(n):
    if n >= 88:
        return('You got an: A')
    elif n >= 80:
        return('You got a: B')
    elif n >= 67:
        return('You got a: C')
    elif n >= 60:
        return('You got a: D')
    else:
        return('You got a: F')
    
def remove_vowels(s):
    vs = ['a', 'e', 'i' , 'o' , 'u']
    ss = s.strip().lower()

    for v in vs:
      ss = ss.replace(v, '')
    
    return ss