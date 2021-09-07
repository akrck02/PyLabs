

def readTextFile(filename):
    """Reads text file and returns a string"""
    with open(filename, 'r') as f:
        return f.read();

def writeTextFile(filename, text):
    """Writes text to file"""
    with open(filename, 'w') as f:
        f.write(text)

def appendTextFile(filename, text):
    """Appends text to file"""
    with open(filename, 'a') as f:
        f.write(text)


def readBinaryFile(filename):
    """Reads binary file and returns a string"""
    with open(filename, 'rb') as f:
        return f.read();



writeTextFile('res/fileio.txt', '# Hello world!\n')
appendTextFile('res/fileio.txt', '# How r u doing?\n')
print(readTextFile('res/fileio.txt'))
#print(readBinaryFile('res/image.jpg'))

