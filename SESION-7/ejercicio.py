class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer_mobilephone = manufacturer
        self.screen_size_mobilephone = screen_size
        self.num_cores_mobilephone = num_cores
        self.power_on = False

    def turn_on(self):
        print("Encendido")
        self.power_on = True

    def turn_off(self):
        print("Apagado")
        self.power_on = False

    def install_app(self, app):
        self.app_MobilePhone = app
        print("Instalando...")

    def uninstall_app(self, app):
        self.app_MobilePhone = app
        print("Desinstalando...")

samsung_s9 = MobilePhone("Samsung", 16.4, 7)
print("Características = Fabricante: ", samsung_s9.manufacturer_mobilephone, " Pantalla: ", samsung_s9.screen_size_mobilephone, " Nucleos: ", samsung_s9.num_cores_mobilephone)

samsung_s9.turn_on()
print("power on", samsung_s9.power_on)

samsung_s9.turn_off()
print("power on", samsung_s9.power_on)

samsung_s9.install_app(["Whatsapp", "Messenger", "Candy Crush", "Facebook", "Instagram"])
print(samsung_s9.app_MobilePhone)

samsung_s9.uninstall_app(["Whatsapp", "Messenger", "Candy Crush", "Facebook", "Instagram"])
print(samsung_s9.app_MobilePhone)

