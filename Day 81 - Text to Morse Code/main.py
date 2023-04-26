MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
              'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..',
              'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',

              '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', ' ': '   '
              }

print("Welcome to Morse Code Convertor!!")

is_continue = True

while is_continue:
    text = input("Enter the text you want to convert to morse: \n").upper()
    try:
        coded_msg = [MORSE_CODE[char] for char in text]
    except KeyError:
        print("Only use numbers and alphabets. No symbols.")
    else:
        print(coded_msg)

    continue_morse = input("Do you want to continue? Type Y/N: ").upper()
    if continue_morse == 'N':
        print("Thank You!!!")
        is_continue = False
