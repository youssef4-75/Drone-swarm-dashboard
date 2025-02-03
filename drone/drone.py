from dataclasses import dataclass


@dataclass
class Drone:
    battery: int
    ...

    # all data that define the state of a drone are here, also those that describe the environment the drone exists in, like humidity, temperature ...
    # ill generate it later by AI just to work with it, it will be easier to handle an object with predefined attributes than making it with dict
    