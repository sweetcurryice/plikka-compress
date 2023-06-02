import PySimpleGUI as ui

label1 = ui.Text("select file to compress :")
input1 = ui.Input()
button1 = ui.FilesBrowse("Browse", key = "file")

label2 = ui.Text("select destination folder :")
input2 = ui.Input()
button2 = ui.FolderBrowse("Browse", key = "folder")

compress_button = ui.Button("Compress")

display = ui.Window("File Compression", 
                    layout = [[label1, input1, button1],
                              [label2, input2, button2],
                              [compress_button]])

while True:
    event, values = display.read()
    if event == ui.WINDOW_CLOSED:
        break

    print(event, values)
    filename = values["file"].split(";")
    folder = values["folder"]
    print(f"\n{filename, folder}")


display.close()