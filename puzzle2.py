import gi
import threading
from puzzle1 import puzzle1
from gi.repository import Gtk, GLib


class NFCApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="NFC Puzzle 2")
        self.set_default_size(400, 200)

        # Contenedor vertical
        vbox = Gtk.VBox(spacing=10)
        self.add(vbox)

        # Etiqueta de instrucciones
        self.label_info = Gtk.Label(label="Please, login with your NFC card")
        vbox.pack_start(self.label_info, True, True, 0)

        # Etiqueta para mostrar el UID
        self.label_uid = Gtk.Label(label="UID: ----")
        vbox.pack_start(self.label_uid, True, True, 0)

        # Botón para limpiar
        self.button_clear = Gtk.Button(label="Clear")
        self.button_clear.connect("clicked", self.clear_label)
        vbox.pack_start(self.button_clear, True, True, 0)

        # Hilo para leer NFC
        self.nfc_thread = threading.Thread(target=self.read_nfc, daemon=True)
        self.nfc_thread.start()

    def read_nfc(self):
        """Ejecuta la función puzzle1() y actualiza la interfaz cuando se detecta una tarjeta."""
        uid = puzzle1()
        if uid:
            GLib.idle_add(self.update_label, uid.hex().upper())  # Actualizar interfaz gráfica

    def update_label(self, uid_hex):
        """Actualizar la etiqueta del UID en la interfaz."""
        self.label_uid.set_text(f"UID: {uid_hex}")

    def clear_label(self, widget):
        """Limpiar el UID cuando se presiona el botón."""
        self.label_uid.set_text("UID: ----")


def main():
    app = NFCApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
