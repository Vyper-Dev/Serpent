# Block Encryption

A block encryption program that splits the given text or text file into three blocks and uses a different key for each block. Keys are generated on demand using a pre-made character list, giving roughly 72^72 possible combinations.

There are three versions:
1. Level 1(Encryption_Static)- Uses a static key on given text
2. Level 2(Encryption_Keys.py)- Uses private keys on given text
3. Level 3(Encryption_Keys_and_Files.py)- Uses private keys on text files or given text

NOTE: Other filetypes may be used in Level 3 but ensure the file type conversion will work (ex. .c to .txt) or risk losing all data in the given file