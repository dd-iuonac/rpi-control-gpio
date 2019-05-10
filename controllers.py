from typing import List

from RPi import GPIO
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QModelIndex

from data import Pin
from models import PinModel
from ui.main_window import Ui_MainWindow
from ui import digital_out, digital_input, pwm


class DigitalInputController(QtWidgets.QWidget):
    def __init__(self, pin_list, parent=None):
        super(DigitalInputController, self).__init__(parent)
        self.ui = digital_input.Ui_Form()
        self.ui.setupUi(self)
        self.current_model_index = QModelIndex()
        self._pin_list = pin_list

        self.ui.pushButton_read.clicked.connect(self.on_read_input)

    def on_read_input(self, checked):
        pin = self._pin_list[self.current_model_index.row()]
        value = GPIO.input(int(pin.id))
        self.ui.lineEdit_value.setText(str(value))

    def set_selection(self, current):
        self.current_model_index = current


class DigitalOutputController(QtWidgets.QWidget):
    def __init__(self, model: PinModel, pin_list, parent=None):
        super(DigitalOutputController, self).__init__(parent)
        self.ui = digital_out.Ui_Form()
        self.ui.setupUi(self)
        self.current_model_index = QModelIndex()
        self._pin_list = pin_list
        self.pin = self._pin_list[0]
        self.model = model
        self.data_mapper = QtWidgets.QDataWidgetMapper()
        self.data_mapper.setModel(self.model)
        self.data_mapper.addMapping(self.ui.slider_value, 5)
        self.data_mapper.addMapping(self.ui.spinbox_value, 5)

        self.ui.slider_value.valueChanged.connect(self.on_slider_value_changed)
        self.ui.spinbox_value.valueChanged.connect(self.on_spinbox_value_changed)

    def on_slider_value_changed(self, value):
        self.ui.spinbox_value.setValue(value)
        GPIO.output(int(self.pin.id), value)
    
    def on_spinbox_value_changed(self, value):
        self.ui.slider_value.setValue(value)
        GPIO.output(int(self.pin.id), value)

    def set_selection(self, current):
        
        self.current_model_index = current
        self.pin = self._pin_list[self.current_model_index.row()]
        self.data_mapper.setCurrentModelIndex(current)
    
    def showEvent(self, a0: QtGui.QShowEvent):
        a0.accept() 
        


class PulseWidthModulationController(QtWidgets.QWidget):
    def __init__(self, model: PinModel, pin_list, parent=None):
        super(PulseWidthModulationController, self).__init__(parent)
        self.ui = pwm.Ui_Form()
        self.ui.setupUi(self)
        self.model = model
        self._pin_list = pin_list
        self.current_model_index = QModelIndex()
        self.data_mapper = QtWidgets.QDataWidgetMapper()
        self.data_mapper.setModel(self.model)
        self.pin = self._pin_list[0]

        self.data_mapper.addMapping(self.ui.spinbox_frequency, 3)
        self.data_mapper.addMapping(self.ui.slider_frequency, 3)
        self.data_mapper.addMapping(self.ui.spinbox_duty_cycle, 4)
        self.data_mapper.addMapping(self.ui.slider_duty_cycle, 4)

        self.ui.slider_frequency.valueChanged.connect(self.on_slider_frequency)
        self.ui.slider_duty_cycle.valueChanged.connect(self.on_slider_duty_cycle)
        self.ui.spinbox_frequency.valueChanged.connect(self.on_spinbox_frequency)
        self.ui.spinbox_duty_cycle.valueChanged.connect(self.on_spinbox_duty_cycle)
        self.ui.button_pwm.clicked.connect(self.on_button_pwm)

    def on_button_pwm(self, checked):
        if checked:
            if not self.pin.pwm_instance:
                self.pin.pwm_instance = GPIO.PWM(int(self.pin.id), self.pin.frequency)
            self.pin.pwm_instance.start(self.pin.duty_cycle)
            self.pin.pwm_instance.ChangeFrequency(self.pin.frequency)
            self.ui.button_pwm.setText("Stop")
        else:
            self.ui.button_pwm.setText("Start")
            self.pin.pwm_instance.stop()
            self.pin.pwm_instance = None

    def on_spinbox_duty_cycle(self, value):
        self.ui.slider_duty_cycle.setValue(value)
        if self.pin.pwm_instance:
            self.pin.pwm_instance.ChangeDutyCycle(value)

    def on_spinbox_frequency(self, value):
        self.ui.slider_frequency.setValue(value)
        if self.pin.pwm_instance and value > 0:
            self.pin.pwm_instance.ChangeFrequency(value)

    def on_slider_frequency(self, value):
        self.ui.spinbox_frequency.setValue(value)
        if self.pin.pwm_instance and value > 0:
            self.pin.pwm_instance.ChangeFrequency(value)

    def on_slider_duty_cycle(self, value):
        self.ui.spinbox_duty_cycle.setValue(value)
        if self.pin.pwm_instance:
            self.pin.pwm_instance.ChangeDutyCycle(value)

    def set_selection(self, current):
        self.current_model_index = current
        self.pin = self._pin_list[self.current_model_index.row()]
        self.data_mapper.setCurrentModelIndex(current)
        
    def showEvent(self, a0: QtGui.QShowEvent):
        a0.accept()
      

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, pin_list: List[Pin], parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._pin_list = pin_list
        self.data_mapper = QtWidgets.QDataWidgetMapper()
        self.model = PinModel(pin_list)
        self.current_model_index = QModelIndex()

        self.data_mapper.setModel(self.model)
        self.ui.listView.setModel(self.model)

        self.data_mapper.addMapping(self.ui.lineEdit_name, 0)
        self.data_mapper.addMapping(self.ui.comboBox_type, 1)
        self.data_mapper.addMapping(self.ui.comboBox_mode, 2)
        self.data_mapper.toFirst()

        self.ui.listView.selectionModel().currentChanged.connect(self.set_selection)

        self.digital_input_controller = DigitalInputController(pin_list, self)
        self.digital_output_controller = DigitalOutputController(self.model, pin_list, self)
        self.pwm_controller = PulseWidthModulationController(self.model, pin_list, self)
        self.ui.layout_values.addWidget(self.digital_input_controller)
        self.ui.layout_values.addWidget(self.digital_output_controller)
        self.ui.layout_values.addWidget(self.pwm_controller)

        self.ui.comboBox_type.currentTextChanged.connect(self.on_type_changed)
        self.ui.comboBox_mode.currentTextChanged.connect(self.on_mode_changed)

    def on_mode_changed(self, text: str):
        pin_type = self.ui.comboBox_type.currentText()
        pin = self._pin_list[self.current_model_index.row()]
        if text.__eq__("Digital"):
            if pin_type.__eq__("Input"):
                self.digital_input_controller.setVisible(True)
                self.digital_output_controller.setVisible(False)
                self.pwm_controller.setVisible(False)
                GPIO.setup(int(pin.id), GPIO.IN)
                
            else:
                self.digital_input_controller.setVisible(False)
                self.digital_output_controller.setVisible(True)
                self.pwm_controller.setVisible(False)
                GPIO.setup(int(pin.id), GPIO.OUT)
                GPIO.output(int(pin.id), pin.value)
                
            if pin.pwm_instance:
                pin.pwm_instance.stop()
                self.pwm_controller.ui.button_pwm.setText("Start")
                self.pwm_controller.ui.button_pwm.setChecked(False)
        else:
            if pin_type.__eq__("Input"):
                self.digital_input_controller.setVisible(False)
                self.digital_output_controller.setVisible(False)
                self.pwm_controller.setVisible(False)
                if pin.pwm_instance:
                    pin.pwm_instance.stop()
                    self.pwm_controller.ui.button_pwm.setText("Start")
                    self.pwm_controller.ui.button_pwm.setChecked(False)
            else:
                self.digital_input_controller.setVisible(False)
                self.digital_output_controller.setVisible(False)
                self.pwm_controller.setVisible(True)
                

    def on_type_changed(self, text):
        pin_mode = self.ui.comboBox_mode.currentText()
        pin = self._pin_list[self.current_model_index.row()]

        if text.__eq__("Input"):
            if pin_mode.__eq__("Digital"):
                self.digital_input_controller.setVisible(True)
                self.digital_output_controller.setVisible(False)
                self.pwm_controller.setVisible(False)
                GPIO.setup(int(pin.id), GPIO.IN)
            else:
                self.digital_input_controller.setVisible(False)
                self.digital_output_controller.setVisible(False)
                self.pwm_controller.setVisible(False)
                
            if pin.pwm_instance:
                pin.pwm_instance.stop()
                self.pwm_controller.ui.button_pwm.setText("Start")
                self.pwm_controller.ui.button_pwm.setChecked(False)
        else:
            if pin_mode.__eq__("Digital"):
                self.digital_input_controller.setVisible(False)
                self.digital_output_controller.setVisible(True)
                self.pwm_controller.setVisible(False)
                GPIO.setup(int(pin.id), GPIO.OUT)
                GPIO.output(int(pin.id), pin.value)
                if pin.pwm_instance:
                    pin.pwm_instance.stop()
                    self.pwm_controller.ui.button_pwm.setText("Start")
                    self.pwm_controller.ui.button_pwm.setChecked(False)
            else:
                self.digital_input_controller.setVisible(False)
                self.digital_output_controller.setVisible(False)
                self.pwm_controller.setVisible(True)
                

    def set_selection(self, current: QModelIndex, old: QModelIndex):      
        self.current_model_index = current
        self.data_mapper.setCurrentModelIndex(current)
        
        self.pwm_controller.set_selection(current)
        self.digital_output_controller.set_selection(current)
        self.digital_input_controller.set_selection(current)
       
            
    def showEvent(self, a0: QtGui.QShowEvent):
        pin_type = self.ui.comboBox_type.currentText()
        pin_mode = self.ui.comboBox_mode.currentText()
        if pin_type.__eq__("Input"):
            if pin_mode.__eq__("Digital"):
                self.digital_input_controller.setVisible(True)
                self.digital_output_controller.setVisible(False)
                self.pwm_controller.setVisible(False)
            else:
                self.digital_input_controller.setVisible(False)
                self.digital_output_controller.setVisible(False)
                self.pwm_controller.setVisible(False)
        else:
            if pin_mode.__eq__("Digital"):
                self.digital_input_controller.setVisible(False)
                self.digital_output_controller.setVisible(True)
                self.pwm_controller.setVisible(False)
            else:
                self.digital_input_controller.setVisible(False)
                self.digital_output_controller.setVisible(False)
                self.pwm_controller.setVisible(True)
                

