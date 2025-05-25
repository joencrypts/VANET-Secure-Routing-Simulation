import random
from src.crypto import generate_hashes

class Vehicle:
    def __init__(self, vid, speed, position):
        self.id = vid
        self.speed = speed
        self.position = position
        self.salt = "vanet" + str(random.random())

    def move(self, dt):
        self.position = [
            self.position[0] + self.speed * dt * random.uniform(-0.1, 1.1),
            self.position[1] + self.speed * dt * random.uniform(-0.1, 1.1)
        ]

    def check_collision(self, other, threshold=1.0):
        dx = self.position[0] - other.position[0]
        dy = self.position[1] - other.position[1]
        return (dx**2 + dy**2) ** 0.5 < threshold

    def generate_message(self):
        msg = {
            "vehicle_id": self.id,
            "speed": self.speed,
            "position": self.position
        }
        hash_digest = generate_hashes(str(msg), self.salt)
        return msg, hash_digest

    def verify_message(self, msg, hashes):
        expected_hashes = generate_hashes(str(msg), self.salt)
        for key in ["sha256", "md5", "sha1", "blake2b", "sha3_256"]:
            if hashes.get(key) != expected_hashes[key]:
                return False
        return True
