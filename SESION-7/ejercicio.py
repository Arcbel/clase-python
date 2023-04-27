class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = False

    def turn_on(self):
        print("Encendido")
        self.status = True

    def turn_off(self):
        print("Apagado")
        self.status = False

    def install_app(self, app):
        self.apps.append (app)
        print("Instalando...")

    def uninstall_app(self, app):
        if app in self.apps:
            self.apps.remove (app)
            print("Desinstalando...")

samsung_s9 = MobilePhone("Samsung", 16.4, 7)
print("Características = Fabricante: ", samsung_s9.manufacturer, " Pantalla: ", samsung_s9.screen_size, " Nucleos: ", samsung_s9.num_cores)

samsung_s9.turn_on()
print("power on", samsung_s9.status)

samsung_s9.turn_off()
print("power on", samsung_s9.status)

samsung_s9.install_app("Whatsapp")
samsung_s9.install_app("Candy Crush")
samsung_s9.install_app("Messenger")
print(samsung_s9.apps)

samsung_s9.uninstall_app("Candy Crush")
print(samsung_s9.apps)

