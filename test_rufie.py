from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout,QVBoxLayout, QPushButton
from PyQt5.QtCore import *
from instr import *
p1, p2, p3 = 0, 0 , 0

def error_int(intg):
    try:
        return int(intg)
    except:
        return False
class Person():
    def __init__(self, name, age):
            self.name = name
            self.age = age

class Experiment():
    def __init__(self,person, test1, test2, test3):
        self.person = person
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

class InstrScr(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.connects()
        self.set_appear()
        self.show()

    def connects(self):
        self.btn.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_w, win_h)
        self.move(win_x, win_y)

    def initUi(self):
        self.lbl_instr = QLabel(txt_instruction)
        self.lbl_name = QLabel ('Введите имя')
        self.inp_name = QLineEdit()
        self.lbl_age= QLabel('Введите возраст')
        self.inp_age = QLineEdit('7')
        self.btn = QPushButton('нАЧАТЬ')

        self.line = QVBoxLayout()
        self.h_line_name = QHBoxLayout()
        self.h_line_age = QHBoxLayout()

        self.h_line_name.addWidget(self.lbl_name)
        self.h_line_name.addWidget(self.inp_name)
        self.h_line_age.addWidget(self.lbl_age)
        self.h_line_age.addWidget(self.inp_age)
        self.line.addWidget(self.lbl_instr, alignment = Qt.AlignCenter)
        self.line.addLayout(self.h_line_name)
        self.line.addLayout(self.h_line_age)
        self.line.addWidget(self.btn, alignment = Qt.AlignCenter)
        self.setLayout(self.line)

    def next_click(self):
        global name, age
        name = self.inp_name.text()
        age = int(self.inp_age.text())
        self.ps = PulseScr()
        self.hide()

class PulseScr(QWidget):
    def __init__(self):
        super().__init__()
        
        self.set_appear()
        self.show()
        self.initUi()
        self.connects()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_w, win_h)
        self.move(win_x, win_y)

    def initUi(self):
        self.init = QLabel('test')
        self.text_vvod = QLabel('Введите результат...')
        self.instr = QLabel(txt_starttest1)
        self.text_age = QLabel(txt_age)
        self.line_p1 = QLineEdit('0')
        self.btn_next = QPushButton(txt_next, self)
        self.h_line = QHBoxLayout()
        self.h_line.addWidget(self.text_vvod)
        self.h_line.addWidget(self.line_p1)
        self.line = QVBoxLayout()
        self.line.addWidget(self.instr)
        self.line.addLayout(self.h_line)
        self.line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.line)

    def next_click(self):
        global p1
        p1 = int(self.line_p1.text())
        self.ps = CheckSits()
        self.hide()

class CheckSits(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.set_appear()
        self.connects()
        self.show()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_w, win_h)
        self.move(win_x, win_y)

    def initUi(self):
        self.instr = QLabel(txt_starttest1)
        self.btn_next = QPushButton(txt_next, self)
        self.line = QVBoxLayout()
        self.line.addWidget(self.instr, alignment = Qt.AlignCenter)
        self.line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.line)

    def next_click(self):
        self.tw = PulseScr2()
        self.hide()

class PulseScr2(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUi()
        self.show()
        self.connects()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_w, win_h)
        self.move(win_x, win_y)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def initUi(self):
        self.instr = QLabel(txt_instruction)
        self.text_p2= QLabel ('Введите результат')
        self.line_p2 = QLineEdit('0')
        self.text_p3= QLabel('Введите результат после отдыха:')
        self.line_p3 = QLineEdit('0')
        self.btn_next = QPushButton(txt_next)

        self.line = QVBoxLayout()
        self.h_line_name = QHBoxLayout()
        self.h_line_age = QHBoxLayout()

        self.h_line_name.addWidget(self.text_p2)
        self.h_line_name.addWidget(self.line_p2)
        self.h_line_age.addWidget(self.text_p3)
        self.h_line_age.addWidget(self.line_p3)
        self.line.addWidget(self.instr, alignment = Qt.AlignCenter)
        self.line.addLayout(self.h_line_name)
        self.line.addLayout(self.h_line_age)
        self.line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.line)

    def next_click(self):
        global p2, p3
        p2 = int(self.line_p2.text())
        p3 = int(self.line_p3.text())
        self.tw = Result()
        self.hide()

class Result(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUi()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_w, win_h)
        self.move(win_x, win_y)

    def initUi(self):
        self.w_text = QLabel(txt_workheart + self.results())
        self.i_text = QLabel(txt_index + str(self.index))

        self.line = QVBoxLayout()
        self.line.addWidget(self.i_text, alignment = Qt.AlignCenter)
        self.line.addWidget(self.w_text, alignment = Qt.AlignCenter)
        self.setLayout(self.line)

    def results(self):
        if age < 7:
            self.index = 0
            return "Нет данных для аткого возраста"
        self.index = (4 * (p1+p2+p3)-200) / 10
        
        if age == 7 or age == 8:
            if self.index >= 21:
                return text_res1
            if self.index <21 and self.index >= 17:
                return text_res2
            if self.index <17 and self.index >=12:
                return text_res3
            if self.index < 12 and self.index >= 6.5:
                return text_res4
            return text_res5

        if age == 9 or age == 10:
            if self.index >= 19.5:
                return text_res1
            if self.index <19.5 and self.index >= 15.5:
                return text_res2
            if self.index <15.5 and self.index >=10.5:
                return text_res3
            if self.index < 10.5 and self.index >= 5:
                return text_res4
            return text_res5

        if age == 11 or age == 12:
            if self.index >= 18:
                return text_res1
            if self.index <18 and self.index >= 14:
                return text_res2
            if self.index <14 and self.index >=9:
                return text_res3
            if self.index < 9 and self.index >= 3.5:
                return text_res4
            return text_res5

        if age == 13 or age == 14:
            if self.index >= 16.5:
                return text_res1
            if self.index <16.5 and self.index >= 12.5:
                return text_res2
            if self.index <12.5 and self.index >= 7.5:
                return text_res3
            if self.index < 7.5 and self.index >= 2:
                return text_res4
            return text_res5

        if age >= 15:
            if self.index >= 15:
                return text_res1
            if self.index <15 and self.index >= 11:
                return text_res2
            if self.index <11 and self.index >=6:
                return text_res3
            if self.index < 6 and self.index >= 0.5:
                return text_res4
            return text_res5

app = QApplication([])
MW = InstrScr()
app.exec_()
