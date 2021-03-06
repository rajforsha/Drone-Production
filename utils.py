"""
This is the util class which has 2 method
writeToOutputFile
readFromInputFile
"""
class Utils:

    # Given a list, writes to file
    def writeToOutputFile(self, filepath, data):
        with open(filepath, 'w') as file:
            for line in data:
                file.write(line + '\n')
            file.write('\n\n')
            file.close()

    # reads the contents from the file and return as list
    def readFromInputFile(self, filepath):
        data = None
        with open(filepath) as file:
            data = file.readlines()
        file.close()
        return data
