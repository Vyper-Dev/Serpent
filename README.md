# Block Encryption

A block encryption program. This version splits the text into three blocks and uses a different key for each block. This method is more secure due to the blocks being asymmetrical and finding one key/pattern will not decrypt the rest.

There are three versions:
1. Encryption_Static- Least Complex, uses a static key and splits the string into blocks
2. Encryption_Keys.py- Medium Complexity, uses private keys placed into text files
3. Encryption_Keys_and_Files.py- Most Complex, uses private keys as well as encrypts/decrypts text files
