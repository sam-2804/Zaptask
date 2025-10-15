                                #GUI Code for application

from PySide6.QtWidgets import QApplication, QWidget,QPushButton,QMainWindow,QLabel,QGridLayout,QHBoxLayout,QFrame,QVBoxLayout,QScrollBar,QLineEdit
from PySide6.QtCore import Slot,Qt,QTimer
from PySide6.QtGui import QFont,QIcon
import sys
import os
import storage_optimizer
import File_organizer
import Focus_mode


def create_button(name,frame,function_name,height = None):
    button_X = QPushButton(name)
    frame.addWidget(button_X)
    button_X.clicked.connect(function_name)
    if height is not None:
        button_X.setFixedHeight(height)

def create_label(name,frame,Align_1 = Qt.AlignmentFlag.AlignCenter,Align_2 = Qt.AlignmentFlag.AlignHCenter,font_size = None):
    label_X = QLabel(name)
    frame.addWidget(label_X)
    label_X.setAlignment(Align_1 | Align_2)
    if font_size is not None:
        font.setPointSize(20) # type: ignore

        label_X.setFont(font_size)

def clear_widget(main_layout):
    while main_layout.count():
        item = main_layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.setParent(None)
            widget.deleteLater()

    
def update_label():
    pass

class mainwindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ZAPTASK")
        self.setGeometry(300,100,800,600)
        logo = QIcon('LOGO_ZAPTASK')
        self.setWindowIcon(logo)
        self.setStyleSheet("background-image: (LOGO_ZAPTASK.png);")
        
        container = QWidget()
        main_layout = QVBoxLayout()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        font = QFont()    

        top_layout = QHBoxLayout()
        middle_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        #frame_left
        frame_left = QFrame()
        frame_left_layout = QVBoxLayout()
        frame_left.setLayout(frame_left_layout)
        frame_left.setFrameShape(QFrame.Box) # type: ignore
        frame_left.setFrameShadow(QFrame.Raised) # type: ignore
        
        create_label("STORAGE OPTIMIZER",frame_left_layout)
        create_label("Clears temporary files and clear \n caches built up in the system",frame_left_layout)
   
        
        def cycle_files():
            clear_widget(frame_right_layout)
            create_label("DONE",frame_right_layout)
            create_label(f"{storage_optimizer.Current_MB} MB of temp files present in system",frame_right_layout)
        
        def SO_function():
            clear_widget(frame_right_layout)
            create_label("Done optimizing",frame_right_layout)
            storage_optimizer.optimize_storage()

            

        create_button("Scan",frame_left_layout,cycle_files)
        create_button("Optimize",frame_left_layout,SO_function)
        
        #frame_middle
        frame_middle = QFrame()
        frame_middle_layout = QVBoxLayout()
        frame_middle.setLayout(frame_middle_layout)
        frame_middle.setFrameShape(QFrame.Box) # type: ignore
        frame_middle.setFrameShadow(QFrame.Raised) #type: ignore
        
        
        label_FO = QLabel("FILE ORGANIZER")
        label_FO.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
       
        label_2 = QLabel("Organizes the files by their \n extension type")
        label_2.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)
        
        frame_middle_layout.addWidget(label_FO)
        frame_middle_layout.addWidget(label_2)
        
        input_line = QLineEdit()
        input_line.setPlaceholderText("Enter path to organize files...")
        
        def start():

            clear_widget(frame_right_layout)
            input_line = QLineEdit()       
            input_line.setPlaceholderText("Enter path to organize files...")
            frame_right_layout.addWidget(input_line)

    
        def organize_files():
            user_path = input_line.text()
            print("Organizing   :", user_path)
            File_organizer.master(user_path)
            clear_widget(frame_right_layout)
            create_label("Processing..........\n \n \n Files are done organizied",frame_right_layout)  

        create_button("Start",frame_middle_layout,start)
        create_button("organize",frame_middle_layout,organize_files)
        
        
        #frame_Right
        frame_right = QFrame()
        
        frame_right_layout = QVBoxLayout()
        frame_right.setLayout(frame_right_layout)
        frame_right.setFrameShape(QFrame.Box)  # type: ignore
        frame_right.setFrameShadow(QFrame.Raised) # type: ignore
        
        create_label("    Welcome to ZAPTASK \n \n A application that aims to automate \n day-to-day basic tasks",frame_right_layout)

        #frame_top
        frame_top = QFrame()
        frame_top_layout = QHBoxLayout()
        frame_top.setLayout(frame_top_layout)
        frame_top.setFrameShadow(QFrame.Raised) # type: ignore
        create_label("ZAPTASK DASHBOARD \n Manage storage,Organize files and enter FOCUS MODE",frame_top_layout)
       
        frame_top.setFixedHeight(80)
        frame_middle.setFixedHeight(350)


        #frame_bottom or FM_frame
        frame_bottom = QFrame()
        frame_bottom_layout = QHBoxLayout()
        frame_bottom.setLayout(frame_bottom_layout)
        frame_bottom.setFrameShadow(QFrame.Raised) # type: ignore

        def FM_function():
            clear_widget(frame_bottom_layout)
            clear_widget(frame_right_layout)
            create_label("Focus Mode : ON",frame_bottom_layout)
            create_label("FOCUS MODE : ACTIVE ",frame_right_layout)
            create_button("Disable focus mode",frame_bottom_layout,FM_function_disable,30)
            create_label(f'Websites Blocked : {Focus_mode.websites_to_block}',frame_right_layout)
            Focus_mode.website_block()

        
        def FM_function_disable():
            Focus_mode.website_unblock()
            print("hi")
            clear_widget(frame_right_layout)
            clear_widget(frame_bottom_layout)
            
            create_button("FOCUS MODE",frame_bottom_layout,FM_function,30)
            create_label("       Welcome to ZAPTASK \n \n A application that aims to automate \n day-to-day basic tasks",frame_right_layout)
       
                 

        create_button("FOCUS MODE",frame_bottom_layout,FM_function,30)
        

        middle_layout.addWidget(frame_left)
        middle_layout.addWidget(frame_middle)
        middle_layout.addWidget(frame_right)
        
        top_layout.addWidget(frame_top)
        bottom_layout.addWidget(frame_bottom)
      
        
        main_layout.addLayout(top_layout)
        main_layout.addLayout(middle_layout)
        main_layout.addLayout(bottom_layout)

    

app = QApplication(sys.argv)
window = mainwindow()

window.show()
app.exec()

