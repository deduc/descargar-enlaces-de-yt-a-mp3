import os
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube


class Main:
    def validar_entrada(self, input_url):
        url = input_url.get()

        if url == "":
            messagebox.showerror("Error", "No puedes poner una url vacía, tron")
            return None
        else:
            # Aquí puedes agregar la lógica para manejar la URL y la ruta del archivo
            messagebox.showinfo("Éxito", f"Comienza la descarga de \n  - URL: {url}\n")
            ruta_descargas = self._get_directorio_descargas()
            self.descargar_audio_yt(url, ruta_descargas)

    def descargar_audio_yt(self, url, ruta):
        yt = YouTube(str(url))
        
        # extraer el audio
        video = yt.streams.filter(only_audio=True).first()

        # descargar fichero
        out_file = video.download(output_path=ruta)

        # guardar el fichero
        base, ext = os.path.splitext(out_file)

        # renombrar fichero
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        messagebox.showinfo("Información", f"{yt.title} ha sido descargado en tu directorio de descargas.\n {ruta}")

    def crear_ventana_principal(self) -> tk.Tk:
        # Crear la ventana principal
        ventana: tk.Tk = tk.Tk()
        ventana.title("Formulario")

        # Establecer las dimensiones de la ventana
        ventana.geometry("500x300")

        return ventana

    def crear_inputs_y_botones(self, ventana):
        # Etiqueta y campo de entrada para la URL
        label_url: tk.Label = tk.Label(ventana, text="URL del vídeo que quieras descargar a mp3:")
        label_url.pack(pady=(10, 0))
        entry_url: tk.Entry = tk.Entry(ventana, width=40)
        entry_url.pack()

        # Botón para validar la entrada
        boton_validar = tk.Button(ventana, text="Validar Entrada", command=lambda: self.validar_entrada(entry_url))
        boton_validar.pack(pady=10)

        return ventana

    def ejecutar_ventana(self, ventana):
        # Ejecutar la ventana
        ventana.mainloop()

    def _get_directorio_descargas(self):
        downloads_dir = os.path.join(os.environ['USERPROFILE'], 'Downloads')

        return downloads_dir

    def run_app(self):
        ventana: tk.Tk = self.crear_ventana_principal()
        ventana = self.crear_inputs_y_botones(ventana)
        self.ejecutar_ventana(ventana)


main_window = Main()
main_window.run_app()
