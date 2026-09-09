class SeqLock:
    """Linux Sequential Lock (seqlock) Implementation."""
    def __init__(self):
        self.sequence = 0
        self.data = {}

    def write_lock(self):
        self.sequence += 1

    def write_unlock(self):
        self.sequence += 1

    def write(self, key, value):
        self.write_lock()
        self.data[key] = value
        self.write_unlock()

    def read(self, key):
        for attempt in range(10):
            seq1 = self.sequence
            if seq1 % 2 != 0:
                continue
            val = self.data.get(key)
            seq2 = self.sequence
            if seq1 == seq2:
                return {'val': val, 'consistent': True, 'attempts': attempt + 1}
        return {'val': self.data.get(key), 'consistent': False, 'attempts': 10}
