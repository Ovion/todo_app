from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMessageBox
from datetime import datetime
import sqlite3


conn = sqlite3.connect("todo.db")
c = conn.cursor()
c.execute("""CREATE TABLE if not exists remain_list(
    list_item text)
    """)
c.execute("""CREATE TABLE if not exists completed_list(
    list_item text)
    """)
conn.commit()
conn.close()

class Ui_ToDoApp(object):
    def setupUi(self, ToDoApp):
        ToDoApp.setObjectName("ToDoApp")
        ToDoApp.resize(1115, 845)
        self.verticalLayout = QtWidgets.QVBoxLayout(ToDoApp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(ToDoApp)
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.top_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.todo_label = QtWidgets.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.todo_label.setFont(font)
        self.todo_label.setObjectName("todo_label")
        self.verticalLayout_2.addWidget(self.todo_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.input_frame = QtWidgets.QFrame(self.top_frame)
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.input_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_lineEdit = QtWidgets.QLineEdit(self.input_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(75)
        self.add_lineEdit.setFont(font)
        self.add_lineEdit.setObjectName("add_lineEdit")
        self.horizontalLayout.addWidget(self.add_lineEdit)
        self.add_pushButton = QtWidgets.QPushButton(self.input_frame, clicked=lambda:self.add_it())
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setObjectName("add_pushButton")
        self.horizontalLayout.addWidget(self.add_pushButton)
        self.verticalLayout_2.addWidget(self.input_frame, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.top_frame, 0, QtCore.Qt.AlignTop)
        self.mid_frame = QtWidgets.QFrame(ToDoApp)
        self.mid_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mid_frame.setObjectName("mid_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.mid_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.remain_label = QtWidgets.QLabel(self.mid_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.remain_label.setFont(font)
        self.remain_label.setObjectName("remain_label")
        self.gridLayout.addWidget(self.remain_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.complete_label = QtWidgets.QLabel(self.mid_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.complete_label.setFont(font)
        self.complete_label.setObjectName("complete_label")
        self.gridLayout.addWidget(self.complete_label, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.remain_listWidget = QtWidgets.QListWidget(self.mid_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(75)
        self.remain_listWidget.setFont(font)
        self.remain_listWidget.setObjectName("remain_listWidget")
        self.gridLayout.addWidget(self.remain_listWidget, 1, 0, 1, 1)
        self.complete_listWidget = QtWidgets.QListWidget(self.mid_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(75)
        self.complete_listWidget.setFont(font)
        self.complete_listWidget.setObjectName("complete_listWidget")
        self.gridLayout.addWidget(self.complete_listWidget, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.mid_frame)
        self.bottom_frame = QtWidgets.QFrame(ToDoApp)
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.complete_pushButton = QtWidgets.QPushButton(self.bottom_frame, clicked=lambda:self.complete_it())
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.complete_pushButton.setFont(font)
        self.complete_pushButton.setObjectName("complete_pushButton")
        self.horizontalLayout_2.addWidget(self.complete_pushButton)
        self.save_pushButton = QtWidgets.QPushButton(self.bottom_frame, clicked=lambda:self.save_all())
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_pushButton.setFont(font)
        self.save_pushButton.setObjectName("save_pushButton")
        self.horizontalLayout_2.addWidget(self.save_pushButton)
        self.clear_pushButton = QtWidgets.QPushButton(self.bottom_frame, clicked=lambda:self.clear_it())
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear_pushButton.setFont(font)
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.horizontalLayout_2.addWidget(self.clear_pushButton)
        self.clear_all_pushButton = QtWidgets.QPushButton(self.bottom_frame, clicked=lambda:self.clear_all())
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear_all_pushButton.setFont(font)
        self.clear_all_pushButton.setObjectName("clear_all_pushButton")
        self.horizontalLayout_2.addWidget(self.clear_all_pushButton)
        self.verticalLayout.addWidget(self.bottom_frame)

        self.retranslateUi(ToDoApp)
        QtCore.QMetaObject.connectSlotsByName(ToDoApp)

        self.grab_remain()

    def grab_remain(self):
        conn = sqlite3.connect("todo.db")
        c = conn.cursor()

        c.execute("SELECT * FROM remain_list")
        remains = c.fetchall()

        c.execute("SELECT * FROM completed_list")
        completes = c.fetchall()

        conn.commit()
        conn.close()
        
        for record in remains:
            self.remain_listWidget.addItem(str(record[0]))

        for record in completes:
            self.complete_listWidget.addItem(str(record[0]))

    def add_it(self):
        it = self.add_lineEdit.text()
        current_date = datetime.today().strftime('%d-%m-%Y %H:%M')
        item = f"{it: <20}  {current_date}"
        self.remain_listWidget.addItem(item)
        self.add_lineEdit.setText("")

    def complete_it(self):
        item = self.remain_listWidget.currentItem().text()
        num = self.remain_listWidget.currentRow()
        self.complete_listWidget.addItem(item)
        self.remain_listWidget.takeItem(num)

    def save_all(self):
        conn = sqlite3.connect("todo.db")
        c = conn.cursor()

        c.execute("DELETE FROM remain_list;",)
        c.execute("DELETE FROM completed_list;",)

        remain_its = [self.remain_listWidget.item(i) for i in range(self.remain_listWidget.count())]
        complete_its = [self.complete_listWidget.item(i) for i in range(self.complete_listWidget.count())]


        for remain_it in remain_its:
            c.execute("INSERT INTO remain_list VALUES (:item)",
            {
                "item":remain_it.text(),
            })
        
        for complete_it in complete_its:
            c.execute("INSERT INTO completed_list VALUES (:item)",
            {
                "item":complete_it.text(),
            })

        conn.commit()
        conn.close()
        
        msg = QMessageBox()
        msg.setWindowTitle("Saved to Database!")
        msg.setText("Your records have been saved!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        

    def clear_it(self):
        num = self.remain_listWidget.currentRow()
        self.remain_listWidget.takeItem(num)
        

    def clear_all(self):
        self.remain_listWidget.clear()
        self.complete_listWidget.clear()

    def retranslateUi(self, ToDoApp):
        _translate = QtCore.QCoreApplication.translate
        ToDoApp.setWindowTitle(_translate("ToDoApp", "ToDoApp"))
        self.todo_label.setText(_translate("ToDoApp", "To Do List"))
        self.add_pushButton.setText(_translate("ToDoApp", "Add"))
        self.remain_label.setText(_translate("ToDoApp", "Remaining"))
        self.complete_label.setText(_translate("ToDoApp", "Completed"))
        self.complete_pushButton.setText(_translate("ToDoApp", "Complete"))
        self.save_pushButton.setText(_translate("ToDoApp", "Save"))
        self.clear_pushButton.setText(_translate("ToDoApp", "Clear"))
        self.clear_all_pushButton.setText(_translate("ToDoApp", "Clear All"))


ToDoApp = QtWidgets.QWidget()
ui = Ui_ToDoApp()
ui.setupUi(ToDoApp)
ToDoApp.show()
