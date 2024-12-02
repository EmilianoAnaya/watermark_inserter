import time
import flet as ft
from Script import watermark_script

class watermark_inserter():
    def main(self, page: ft.Page):
        self.page = page
        self.page.title = "Watermark Inserter"
        self.page.window.width = 300
        self.page.window.height = 200
        self.page.window.maximizable = False
        self.page.window.resizable = False
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.file_picker = ft.FilePicker(on_result=self.pick_files_result)
        self.text_result = ft.Text(color=ft.Colors.AMBER, weight=ft.FontWeight.BOLD)

        self.page.overlay.append(self.file_picker)

        self.page.add(
            ft.Text(value="Pick the images to Watermark"),
            ft.ElevatedButton(
                "Pick Files",
                icon=ft.Icons.UPLOAD_FILE,
                on_click=lambda _: self.file_picker.pick_files(
                    allow_multiple=True
                ),
            ),
            self.text_result
        )
        self.page.update()
    
    def pick_files_result(self,e: ft.FilePickerResultEvent):
        if not e.files:
            self.text_result.value="No selected Files"
            self.text_result.update()
            time.sleep(2)
            self.text_result.value=""
            self.text_result.update()
            return
        for file in e.files:
            path = file.path.replace("\\","/")
            watermark_script(path)
        self.text_result.value="Done!"
        self.text_result.update()
        time.sleep(1)
        self.text_result.value=""
        self.text_result.update()

if __name__ == "__main__":
    app = watermark_inserter()
    ft.app(target=app.main)