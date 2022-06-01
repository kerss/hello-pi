# from gpiozero import LED
import time
import sys

# Dit is een voorbeeld van werken met classes
class Controller:
    # De init functie word automatisch aangeroepen wanneer er een object van dit type/class aangemaakt wordt
    def __init__(self, delta_t = 0.1) -> None:
        # Omdat deze functie altijd aangeroepen word (tijdens de initialisatie) 
        # is dit de perfecte plek om eventuele parameters te initialiseren
        # dit gaat als volgt:
        self.parameter1 = 10.
        self.parameter2 = 20.
        
        self.start_t = time.time()
        self.stap_idx = 0

        self.delta_t = delta_t

    def print_status(self):
        print(f'Huidige stap: {self.stap_idx} \t Verlopen tijd : {round(time.time() - self.start_t, 4)}')
        
    def start(self):
        self.start_t = time.time()
        self.stap_idx = 0    

    def wacht_tot_volgende_stap(self):
        self.stap_idx += 1
        wakeup_t = self.start_t + self.stap_idx * self.delta_t
        slaap_t = wakeup_t - time.time()
        time.sleep(slaap_t)


if __name__ == '__main__':
    # De volgende regel code initialiseerd een object van het type 'Controller'
    controller_obj = Controller(delta_t=.5)
    
    # Start de controller
    controller_obj.start()

    # Oneindige loop
    while True:
        # Voer uit:
        try:
            controller_obj.print_status()

            # Voer hier code uit

            controller_obj.wacht_tot_volgende_stap()

        # Keyboard clrl+c -> afsluiten
        except KeyboardInterrupt:
            print('Stopping software safely')
            sys.exit(0)
        
    
