from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from mainView import Ui_mainWindow

def load_project_structure(startpath, tree):
  
    from PyQt5.QtWidgets import QTreeWidgetItem	    
    from PyQt5.QtGui import QIcon
    
    for element in os.listdir(startpath):
        path_info = startpath + "/" + element
        parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
        if os.path.isdir(path_info):
            load_project_structure(path_info, parent_itm)
            parent_itm.setIcon(0, QIcon('folder.png')) 
        else:
              parent_itm.setIcon(0, QIcon('file.png'))
def getItemFullPath(item):
    out = item.text(0)

    if item.parent():
        out = getItemFullPath(item.parent()) + "/" + out
    else:
        out =  "../content/" + out
    return out;

def onItemClicked(it, col):
    print(it, col, it.text(col))	    # print(it, col, it.text(col))
    print(getItemFullPath(it))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    myapp = Ui_mainWindow()
    myapp.setupUi(window)


#    dir_path = os.path.split(os.path.expanduser("~/~user"))[0]
#    load_project_structure(dir_path, myapp.folder_widget)	        
#    myapp.folder_widget.itemClicked.connect(onItemClicked)	

    window.show()
    sys.exit(app.exec_())
