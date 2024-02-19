The Atbash cipher is a cipher that will encrypt a plaintext by reversing the alphabet and replacing each letter with the corresponding letter

For example

ABCDEFGHIJKLMNOPQRSTUVWXYZ

ZYXWVUTSRQPONMLKJIHGFEDCBA

HELLO WORLD = SVOOL DLIOOW

This script performs this by converting the letters to their ASCII representations.
It then subtracts the index of each letter from 25 (the index of the letter Z).
The letter will then be converted back from ASCII using the chr() function

