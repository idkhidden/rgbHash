from PIL import ImageGrab
import random

def rgbtobinary(rgbtuple):
    return ''.join(format(x, '08b') for x in rgbtuple)

def hashingkey(total):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-="
    hashedkey = ''.join(random.choice(characters) for char in str(total) if char.isdigit())
    return hashedkey

def hashingtext(text, hashedkey):
    combined = list(hashedkey)
    text = list(text)
    for char in text:
        position = random.randint(0, len(combined))
        combined.insert(position, char)
    return ''.join(combined)

while True:
    input("Press Enter to take a screenshot!")  
    print("Taking a screenshot!")

    screenshot = ImageGrab.grab()
    width, height = screenshot.size

    total = 0

    for y in range(height):
        for x in range(width):
            rgb = screenshot.getpixel((x, y))
            binarycolor = rgbtobinary(rgb)
            binaryvalue = int(binarycolor, 36)  
            total  += binaryvalue

    print("Key -> ", total)
    
    hashedkey = hashingkey(total)
    print("Hashed Key -> ", hashedkey)
    
    text = input("Enter your text to be hashed -> ")
    finalhash = hashingtext(text, hashedkey)
    print("Hashed text -> ", finalhash)
