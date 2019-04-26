from beacon import Beacon


class Tracker:
    def __init__(self, bounds):
        self.bounds = bounds
        self.beacons = []

    def beacon(self):
        beacon = Beacon(self.bounds)
        self.beacons.append(beacon)
        return beacon.ping

    def results(self):
        return "".join([beacon.result() + "\n" for beacon in self.beacons]).rstrip()

    def scents(self):
        return [beacon.position for beacon in self.beacons if beacon.lost]
