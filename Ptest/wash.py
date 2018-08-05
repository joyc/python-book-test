class Washer:

    def __init__(self, water=10, scour=2):
        self.water = water
        self.scour = scour

    @staticmethod
    def spins_ml(spins):
        return spins * 0.4

    @classmethod
    def get_washer(cls, water, scour):
        return cls(water, cls.spins_ml(scour))

    def add_water(self):
        print('Add water:', self.water)

    def add_scour(self):
        print('Add scour:', self.scour)

    def start_wash(self):
        self.add_water()
        self.add_scour()
        print('Start washing...')


if __name__ == '__main__':
    w = Washer()
    # w.add_water(10)
    # w.add_scour(2)
    w.start_wash()