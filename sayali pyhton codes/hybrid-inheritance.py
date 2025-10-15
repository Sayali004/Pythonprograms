class Device:
    def feature(self):
        print("Basic electronic device.")

class Light(Device):
    def feature(self):
        print("I am a Smart Light. I can turn ON/OFF.")

class Speaker(Device):
    def feature(self):
        print("I am a Smart Speaker. I can play music.")

class SmartAssistant(Light, Speaker):
    def feature(self):
        print("I am a Smart Assistant. I can control lights and play music.")

alexa = SmartAssistant()
alexa.feature()

