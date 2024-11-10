import gi
gi.require_version('Atk', '4.0')
from gi.repository import Atk

class AccessibleApp:
    def __init__(self):
        self.window = Atk.Window.new(None)
        self.label = Atk.Label.new_with_mnemonic('Hello, World!')

    def run(self):
        self.window.add_child(self.label)
        Atk.Object.set_name(self.window, 'Accessible App')
        Atk.Object.set_description(self.window, 'This is an accessible app')
        Atk.Object.set_role(self.window, Atk.Role.APPLICATION)
        self.window.show_all()

app = AccessibleApp()
app.run()
