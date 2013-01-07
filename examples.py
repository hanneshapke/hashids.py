from hashids import hashids;

hashids_lib = hashids("this is my salt")
hash = hashids_lib.encrypt(1, 2, 3)
numbers = hashids_lib.decrypt(hash)

print(hash)
print(numbers)