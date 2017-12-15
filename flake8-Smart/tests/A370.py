import hashlib

hashlib.md5(1)

print hashlib.md5(2)

x = hashlib.md5('hello')

hashlib.md5(3).hexdigest()


hashlib.sha(1)

print hashlib.sha(2)

x = hashlib.sha('hello')

hashlib.sha(3).hexdigest()

hashlib.sha256('Nobody inspects the spammish repetition').hexdigest()

hashlib.sha1('Nobody inspects the spammish repetition').hexdigest()
