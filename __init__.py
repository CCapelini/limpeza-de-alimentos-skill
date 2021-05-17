from mycroft import MycroftSkill, intent_file_handler


class LimpezaDeAlimentos(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('alimentos.de.limpeza.intent')
    def handle_alimentos_de_limpeza(self, message):
        self.speak_dialog('alimentos.de.limpeza')


def create_skill():
    return LimpezaDeAlimentos()

