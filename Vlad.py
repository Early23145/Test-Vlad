class Vlad():
    def chat(self):
        print('Choise: Hello; Halo; Grüsgot')
        user = input('Your choise: ')
        if user == 'Choise':
            print('What???')
        elif user == 'Hello':
            print('Sehr gut')
        elif user == 'Halo':
            print('Deuthschland')
        elif user == 'Grüsgot':
            print('Yoi')
        else:
            print("Ich verstehe nicht")
vd = Vlad()
vd.chat()
