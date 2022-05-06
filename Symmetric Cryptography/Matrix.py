from pprint import pprint
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    #return bytes(matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])))
    return bytes(sum(matrix,[]))
matrix = (
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
)

ciphertext = b'\xd1O\x14j\xa4+O\xb6\xa1\xc4\x08B)\x8f\x12\xdd'
if __name__ == "__main__":
    pprint(bytes2matrix(b'crypto{inmatrix}'))
