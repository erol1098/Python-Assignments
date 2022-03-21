	
left_hand = {"q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b" }
right_hand = {"y", "u", "ı", "o", "p", "ğ", "ü", "h", "j", "k", "l", "ş", "i", "n", "m", "ö", "ç"}

word = set(input("Please enter a word to control:\n"))

left_true = bool(word & left_hand)

right_true = bool(word & right_hand)

print(left_true and right_true)
