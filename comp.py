import PySimpleGUI as ui
from zip_creator import make_archive as zip

label1 = ui.Text("select file to compress :")
input1 = ui.Input()
button1 = ui.FilesBrowse("Browse", key = "file")

label2 = ui.Text("select destination folder :")
input2 = ui.Input()
button2 = ui.FolderBrowse("Browse", key = "folder")

compress_button = ui.Button("Compress", key = "compress")

display = ui.Window("File Compression", 
                    layout = [[label1, input1, button1],
                              [label2, input2, button2],
                              [compress_button]])

while True:
    event, values = display.read()
    if event == ui.WINDOW_CLOSED:
        break

    #print(event)
    filename = values["file"].split(";")
    folder = values["folder"]
    #print(f"\n{filename, folder}")

    #if event == compress_button:
    zip_lable = ui.Text("Input the archive name")
    zip_input = ui.Input()
    zip_button = ui.Button("Confirm", key = "name")
    zip_display = ui.Window("Archive name", layout = [[zip_lable],[zip_input],[zip_button]])

    while True:
        event, values = zip_display.read()
        if event == ui.WINDOW_CLOSED:
            break

        if event == "name":
            zip_name = str(values[0])+".zip"
            zip(filename, folder, zip_name)
            ui.Prom
            break
    display.close()


display.close()