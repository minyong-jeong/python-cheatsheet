import hashlib

HASH_NAME = "md5"

txt = input("Enter the text to convert: ")

text = txt.encode('utf-8')
md5 = hashlib.new(HASH_NAME)
md5.update(text)
result = md5.hexdigest()

print("type: %s" % HASH_NAME)
print("text: %s" % txt)
print("hash: %s" % result)
