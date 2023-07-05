
# Morse Code Translator

This program provides functionality for encoding and decoding Morse code messages. It includes audio playback capabilities to represent Morse code as sound.

## Program Structure

The program is organized into multiple files:

- `main.py`: Contains the main entry point of the program.
- `utils.py`: Provides utility functions used by the program.
- `Coder.py`: Defines the `Morse` class responsible for encoding, decoding, and audio playback.

## Morse Code Encoding and Decoding

The `Morse` class in `Coder.py` offers methods for encoding plain text into Morse code and decoding Morse code back to plain text. Here's an example of how to use these methods:

```python
from MorseCode.Coder import Morse

plain_text = "HELLO"
morse_code = Morse.encode(plain_text)
decoded_text = Morse.decode(morse_code)

print("Morse Code:", morse_code)
print("Decoded Text:", decoded_text)
 ```

The encode method takes plain text as input and returns the corresponding Morse code. The decode method does the reverse by taking Morse code as input and returning the decoded plain text.

## Audio Playback
The Morse class also provides a print_and_play method that converts Morse code into audio representation. It utilizes threading and sound files to create the audio playback. Here's an example of how to use it:

```
morse_code = ".... . .-.. .-.. ---"
Morse.print_and_play(morse_code)
```
The print_and_play method plays the Morse code audio and simultaneously prints the corresponding characters on the console.

## Instructions on usage
To use this program, follow these steps:

Install the required dependencies, such as pygame, by running pip install pygame in your Python environment.

Import the Morse class from MorseCode.Coder in your Python script.

Utilize the encode and decode methods to convert between plain text and Morse code.

Use the print_and_play method to play Morse code audio and visualize the characters.

## Resources
The program uses the following resources:

Sound Files: The audio files dot.ogg and dash.ogg are used to represent the Morse code symbols '.' and '-' respectively. These files are located in the resources directory.

Morse Code Mapping: The file morse.json in the resources directory contains the mapping between characters and their Morse code representations.

