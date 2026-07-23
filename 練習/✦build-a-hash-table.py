class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key: str) -> int:
        return sum(ord(char) for char in key)

    def add(self, key: str, value) -> None:
        hash_key = self.hash(key)
        
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        
        self.collection[hash_key][key] = value

    def remove(self, key: str) -> None:
        hash_key = self.hash(key)
        
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]
            
            if not self.collection[hash_key]:
                del self.collection[hash_key]

    def lookup(self, key: str):
        hash_key = self.hash(key)
        
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
        
        return None