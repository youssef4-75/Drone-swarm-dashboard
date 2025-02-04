from threading import Thread
from time import sleep
from .temp import get_data



def launch(*layers):
    def loop(bloc, type_):
        while True:
            bloc.update_data(get_data(type_))
            sleep(.01)
    for lay in layers:
        th = Thread(target=lambda :loop(lay, None), daemon=True)
        th.start()
