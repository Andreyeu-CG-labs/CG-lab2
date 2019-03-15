import os

from PyQt5 import QtWidgets, QtCore
from PIL import Image

supported_extensions = ('.jpg', '.gif', '.tif', '.bmp', '.png', '.pcx')
mode_to_bpp = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32,
               "YCbCr": 24, "LAB": 24, "HSV": 24, "I": 32, "F": 32}


def add_file_dialog():
    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.DontUseNativeDialog
    filename, _ = QtWidgets.QFileDialog.getOpenFileName(
        None,
        "QFileDialog.getOpenFileName()",
        "./tagged_texts",
        ("All Files (*);; JPEG (*.jpg);; gif (*.gif);; tif (*.tif);; "
         + "bmp (*.bmp);; png (*.png);; pcx (*.pcx)"),
        options=options
    )
    return filename


def add_folder_dialog():
    folder = str(QtWidgets.QFileDialog.getExistingDirectory(
        None, "Select Directory")
    )
    return folder


def add_image(ui):
    filename = add_file_dialog()
    row_count = ui.tableWidget.rowCount()
    ui.tableWidget.insertRow(row_count)

    (size, dpi,
     color_depth, compression) = get_image_info(filename)

    insert_row(
        ui.tableWidget, row_count, filename=os.path.basename(filename),
        size=size, dpi=dpi, color_depth=color_depth, compression=compression
    )


def add_image_folder(ui):
    folder = add_folder_dialog()
    files = os.listdir(folder)
    ui.tableWidget.setRowCount(len(files))
    for row_number, filename in enumerate(files):
        if filename.endswith(supported_extensions):
            (size, dpi,
             color_depth, compression) = get_image_info(f'{folder}/{filename}')

            insert_row(
                ui.tableWidget, row_number, filename=filename, size=size,
                dpi=dpi, color_depth=color_depth, compression=compression
            )


def insert_row(table_widget, row_number, filename='',
               size='', dpi='', color_depth='', compression=''):
    table_widget.setItem(row_number, 0,
                         QtWidgets.QTableWidgetItem(filename))
    table_widget.setItem(row_number, 1,
                         QtWidgets.QTableWidgetItem(size))
    table_widget.setItem(row_number, 4,
                         QtWidgets.QTableWidgetItem(compression))
    item2 = QtWidgets.QTableWidgetItem()
    item2.setData(QtCore.Qt.DisplayRole, dpi)
    table_widget.setItem(row_number, 2, item2)
    item = QtWidgets.QTableWidgetItem()
    item.setData(QtCore.Qt.DisplayRole, color_depth)
    table_widget.setItem(row_number, 3, item)


def get_image_info(image_path):
    image = Image.open(image_path)
    size = f'{image.width}x{image.height}'
    try:
        color_depth = mode_to_bpp[image.mode]
    except KeyError:
        color_depth = ''
    try:
        dpi = int(image.info['dpi'][0])
    except KeyError:
        dpi = ''
    try:
        compression = image.info['compression']
    except KeyError:
        compression = ''
    return size, dpi, color_depth, compression

