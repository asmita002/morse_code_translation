from MorseCode.Coder import Morse
import sys

plain_text=Morse.encode('This is my morse code generator')
print(plain_text)

#input_text = sys.argv[1]

#encoded_output = Morse.encode(input_text)
#Morse.print_and_play(encoded_output)