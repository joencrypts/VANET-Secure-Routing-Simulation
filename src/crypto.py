import hashlib
import random
import time

def generate_hashes(message: str, salt: str):
    message_bytes = message.encode()
    salted = message_bytes + salt.encode()
    hashes = {}
    
    def timed_hash(fn, key):
        start = time.time()
        result = fn(salted).hexdigest()
        hashes[key] = result
        hashes[f"{key}_time"] = time.time() - start

    timed_hash(hashlib.sha256, "sha256")
    timed_hash(hashlib.md5, "md5")
    timed_hash(hashlib.sha1, "sha1")
    timed_hash(hashlib.blake2b, "blake2b")
    timed_hash(hashlib.sha3_256, "sha3_256")
    
    return hashes
