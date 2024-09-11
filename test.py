from sequence import Sequence
from pattern import Pattern
from pydub import AudioSegment
import flet as ft
from fletmint import *
# test = Sequence()
# test = Pattern("test")
# test2 = Sequence()
# print(test2.BPM)
# print(test.audio)

"""
audio = AudioSegment.from_wav(f"./assets/matrix.wav")
audio2 = AudioSegment.from_wav(f"./assets/strawberry.wav")
audio3 = audio + audio2
audio3.export("audio3.mp3", format="mp3")
"""

# this works :OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# lightwork audio work ig

def main(page: ft.Page):
    page.title = "test"
    page.add(ft.Text("Hello World!"))
    page.add(Button())

    # file_picker = ft.FilePicker()
    # page.overlay.append(file_picker)
    # page.update()
    # ft.ElevatedButton("Choose files...",
                      # on_click=lambda _: file_picker.get_directory_path()
                      # )

    def on_dialog_result(e: ft.FilePickerResultEvent):
        # print("Selected files: ", e.files)
        print("Selected file or directory: ", e.path)

    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)

    page.add(Button(label = "Import Project", on_click= lambda _: file_picker.get_directory_path_async()))
    
ft.app(main)
