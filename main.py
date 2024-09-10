import flet as ft
from fletmint import *

def main(page: ft.Page):
    page.title = "Joey Renderer"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.expand = True
    # page.add(ft.SafeArea(ft.Text("Hello, Flet!")))

    joeyTagline = ft.Text(value="Joey", color = "#A4A4A4", text_align = ft.TextAlign.CENTER, size=40, weight = ft.FontWeight.BOLD)
    
    topbar = ft.Container(
        content= ft.Row(
            controls= [ft.Container(),
            ft.Column(
                    controls = [joeyTagline,
                         # ft.Text(value="The Koala Renderer", color = "#A4A4A4", text_align = ft.TextAlign.CENTER, size=15, weight = ft.FontWeight.BOLD, italic = True)], 
                         ft.Text(value="The Koala Sequencer", color = "#A4A4A4",  size=15, weight = ft.FontWeight.BOLD, italic = True, text_align= ft.TextAlign.CENTER)], 
                    # controls = [ft.Text(value="The Koala Renderer", color = "#A4A4A4", text_align = ft.TextAlign.CENTER, size=20, weight = ft.FontWeight.BOLD, italic = True) ],
                    # alignment = ft.alignment.center,
                    alignment = ft.MainAxisAlignment.CENTER,
                    
                ),
            ft.Column(
                    controls = [Stepper(initial_value = 140, suffix = "bpm", ), ft.Text("Length: 00:00:00")]
                )
            ],
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        ),
    padding = 5)

    fileExplorer = ft.Container(width = 250, height = 100, border_radius = 5, padding = 2, bgcolor = "#181A21")
        
    bottombar = ft.Container(
        content = ft.Row(
            controls = [
                fileExplorer,
                ft.Image(src=f"/Joey.png", width = 125, height = 125, fit=ft.ImageFit.CONTAIN, ),
                Button(label="Export")
                
            ], alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        ), 
    )

    # meat = ft.Container(
    #     content = [
    #         ft.Container(width = 250, height = 250, bgcolor = ft.colors.GREEN_50)
    #     ]
    # )

    sequenceBeats = 10
    trueBeats = sequenceBeats + 1
    meat = ft.GridView(
        expand = 1,
        # run_count = 5,
        # max_extent = page.window.width / trueBeats,
        max_extent = page.window.width,
        spacing = 5,
        run_spacing = 5,
        # width = page.window.width - 100,
        # height = page.window.height - 100,
        # horizontal = ft.MainAxisAlignment.CENTER
        # vertical = True        
         
    )

    meat2 = ft.Column(controls = [meat], expand = 1, horizontal_alignment= ft.CrossAxisAlignment.CENTER, alignment = ft.MainAxisAlignment.CENTER, spacing = 100 )
    
    # meat.horizontali
    for i in range(sequenceBeats):
        meat.controls.append(ft.Container(width = 50, height = 50, bgcolor = ft.colors.PURPLE_200, border_radius=30))
    meat.controls.append(ft.Container(width = 50, height = 50, bgcolor = ft.colors.GREEN_200, border_radius=30))
    # page.add(
    #          ft.Container(
    #                      content = [topbar, meat, bottombar],
    #                      alignment = ft.MainAxisAlignment.SPACE_AROUND
    #                      )
    #         )
    # page.update()
    page.add(ft.Column(controls = [topbar,meat2,bottombar], height = page.window.height - 50, width = page.window.width - 50, alignment= ft.MainAxisAlignment.SPACE_BETWEEN, expand=True ))
    # page.add(ft.Column(controls = [topbar,meat,bottombar], height = page.window.height, expand=True))
    # page.add(ft.Image(src=f"/assets/Joey.png", width = 1024, height = 1024))
    # meat.controls.append(ft.Container(width = 50, height = 50, bgcolor = ft.colors.GREEN_100))
    # meat.controls.append(ft.Container(width = 50, height = 50, bgcolor = ft.colors.PURPLE_200))
    # meat.controls.append(ft.Container(width = 50, height = 50, bgcolor = ft.colors.RED_500))
    page.update()
ft.app(main, assets_dir="assets")
