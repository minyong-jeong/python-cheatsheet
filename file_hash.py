import hashlib


def file_hash(path):
    f = open(path, 'rb')
    data = f.read()
    hash = hashlib.md5(data).hexdigest()
    return hash


if __name__ == "__main__":
    hash = file_hash("./README.md")
    print(hash)
