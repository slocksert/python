from abc import ABC, abstractmethod

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self,aumentar):
        pass
    def reduzir_claridade(self,reduzir):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, aumentar):
        print(f'Aumentando claridade em {aumentar}')
    def reduzir_claridade(self, reduzir):
        print(f'Reduzindo claridade em {reduzir}')

monitor=MonitorFullHD()
monitor.aumentar_claridade(5)
monitor.reduzir_claridade(5)