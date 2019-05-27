from RPi import GPIO
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QModelIndex, Qt

from db import PIN_LIST
from package.models import PinModel
from package.ui.digital_input import Ui_DigitalInput
from package.ui.digital_out import Ui_DigitalOutput
from package.ui.license import Ui_License
from package.ui.main_window import Ui_MainWindow
from package.ui.pulse_width_modulation import Ui_PulseWidthModulation


# DigitalInputController is a QWidget and controls the digital input UI Form
class DigitalInputController(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=Qt.Widget):
        super(DigitalInputController, self).__init__(parent, flags=flags)
        self.ui = Ui_DigitalInput()
        self.ui.setupUi(self)
        self.current_model_index = None

        # Connect signal for pressing Read button
        self.ui.pushButton_read.clicked.connect(self.on_read_input)

    """
        on_read_input 
            - get current pin
            - read input value
            - set the value to line edit in UI
    """
    def on_read_input(self, checked):
        pin = PIN_LIST[self.current_model_index.row()]
        if pin.enable:
            value = GPIO.input(pin.id)
            self.ui.lineEdit_value.setText(str(value))

    def set_selection(self, current):
        # Update current index
        self.current_model_index = current


# DigitalOutputController controls the UI form for digital output
class DigitalOutputController(QtWidgets.QWidget):
    def __init__(self, model: PinModel, parent=None, flags=Qt.Widget):
        super(DigitalOutputController, self).__init__(parent, flags=flags)
        self.ui = Ui_DigitalOutput()
        self.ui.setupUi(self)
        self.current_model_index = None
        self.model = model
        self.pin = PIN_LIST[0]

        # Connect slider and spinbox signals to slots
        self.ui.slider_value.valueChanged.connect(self.on_slider_value_changed)
        self.ui.spinbox_value.valueChanged.connect(self.on_spinbox_value_changed)

    """
        on_slider_value_changed
            - sets value to spinbox
            - outputs value to GPIO pin
            - save value to pin data structure
    """
    def on_slider_value_changed(self, value):
        self.ui.spinbox_value.setValue(value)
        GPIO.output(self.pin.id, value)
        self.pin.value = value

    # similar to on_slider_value_changed
    def on_spinbox_value_changed(self, value):
        self.ui.slider_value.setValue(value)
        GPIO.output(self.pin.id, value)
        self.pin.value = value

    """
        set_selection
            - save current index
            - update current pin reference
    """
    def set_selection(self, current):
        self.current_model_index = current
        self.pin = PIN_LIST[self.current_model_index.row()]

    """
        showEvent
            - when a show event is received then accept it
            - update spinbox and slider value
    """
    def showEvent(self, a0: QtGui.QShowEvent):
        a0.accept()
        self.ui.slider_value.setValue(self.pin.value)
        self.ui.spinbox_value.setValue(self.pin.value)


# PulseWidthModulationController controls the UI form for PWM
class PulseWidthModulationController(QtWidgets.QWidget):
    def __init__(self, model: PinModel, parent=None, flags=Qt.Widget):
        super(PulseWidthModulationController, self).__init__(parent=parent, flags=flags)
        self.ui = Ui_PulseWidthModulation()
        self.ui.setupUi(self)
        self.model = model
        self.current_model_index = None
        self.pin = PIN_LIST[0]

        # Connect signals for sliders spinboxes and pwm start/stop button
        self.ui.slider_frequency.valueChanged.connect(self.on_slider_frequency)
        self.ui.slider_duty_cycle.valueChanged.connect(self.on_slider_duty_cycle)
        self.ui.spinbox_frequency.valueChanged.connect(self.on_spinbox_frequency)
        self.ui.spinbox_duty_cycle.valueChanged.connect(self.on_spinbox_duty_cycle)
        self.ui.button_pwm.clicked.connect(self.on_button_pwm)

    """
    on_button_pwm
        if button is pressed then 
            - set Stop text 
            - start PWM instance
            - changeFrequency
        else
            - set Start text
            - stop pwm instance
    """
    def on_button_pwm(self, value):
        if value:
            self.ui.button_pwm.setText("Stop")
            self.pin.pwm_instance.start(self.pin.duty_cycle)
            self.pin.pwm_instance.ChangeFrequency(self.pin.frequency)
        else:
            self.ui.button_pwm.setText("Start")
            self.pin.pwm_instance.stop()

    """
        on_spinbox_duty_cycle
            - update slider value
            - if pwm instance is not null then change duty cycle
            - save value to pin structure
    """
    def on_spinbox_duty_cycle(self, value):
        self.ui.slider_duty_cycle.setValue(value)
        if self.pin.pwm_instance and value > 0:
            self.pin.pwm_instance.ChangeDutyCycle(value)
            self.pin.duty_cycle = value

    # similar to on_spinbox_duty_cycle
    def on_spinbox_frequency(self, value):
        self.ui.slider_frequency.setValue(value)
        if self.pin.pwm_instance and value > 0:
            self.pin.pwm_instance.ChangeFrequency(value)
            self.pin.frequency = value

    # similar to on_spinbox_duty_cycle
    def on_slider_frequency(self, value):
        self.ui.spinbox_frequency.setValue(value)
        if self.pin.pwm_instance and value > 0:
            self.pin.pwm_instance.ChangeFrequency(value)
            self.pin.frequency = value

    # similar to on_spinbox_duty_cycle
    def on_slider_duty_cycle(self, value):
        self.ui.spinbox_duty_cycle.setValue(value)
        if self.pin.pwm_instance and value > 0:
            self.pin.pwm_instance.ChangeDutyCycle(value)
            self.pin.duty_cycle = value

    def set_selection(self, current):
        self.current_model_index = current
        self.pin = PIN_LIST[self.current_model_index.row()]

    # update values to sliders and spinboxes when controller shows
    def showEvent(self, a0: QtGui.QShowEvent):
        a0.accept()
        self.ui.slider_frequency.setValue(self.pin.frequency)
        self.ui.spinbox_frequency.setValue(self.pin.frequency)
        self.ui.spinbox_duty_cycle.setValue(self.pin.duty_cycle)
        self.ui.slider_duty_cycle.setValue(self.pin.duty_cycle)


# The main window controller
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, flags=Qt.Window):
        super(MainWindow, self).__init__(parent, flags)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data_mapper = QtWidgets.QDataWidgetMapper()
        self.model = PinModel(PIN_LIST)
        self.current_model_index = None

        # Set the model to data mapper and to list view
        self.data_mapper.setModel(self.model)
        self.ui.listView.setModel(self.model)

        # Set mapping for data mapper
        self.data_mapper.addMapping(self.ui.lineEdit_name, 0)
        self.data_mapper.addMapping(self.ui.comboBox_type, 1)
        self.data_mapper.addMapping(self.ui.comboBox_mode, 2)
        self.data_mapper.toFirst()

        # When list view's current index changes then set_selection is called
        self.ui.listView.selectionModel().currentChanged.connect(self.set_selection)

        # Instantiate the others controllers and add them to the layout
        self.license_controller = LicenseController()
        self.digital_input_controller = DigitalInputController(self)
        self.digital_output_controller = DigitalOutputController(self.model, self)
        self.pwm_controller = PulseWidthModulationController(self.model, self)
        self.ui.layout_values.addWidget(self.digital_input_controller)
        self.ui.layout_values.addWidget(self.digital_output_controller)
        self.ui.layout_values.addWidget(self.pwm_controller)

        # Set slots for combo boxes signals and button enable
        self.ui.comboBox_type.currentTextChanged.connect(self.on_type_changed)
        self.ui.comboBox_mode.currentTextChanged.connect(self.on_mode_changed)
        self.ui.button_enable.clicked.connect(self.on_button_enable)

        # Set slots for actions triggers signals
        self.ui.action_exit.triggered.connect(QtWidgets.qApp.quit)
        self.ui.action_license.triggered.connect(self.license_controller.show)
        self.ui.action_about.triggered.connect(self.on_action_about)
        self.ui.action_load.triggered.connect(self.on_action_load)
        self.ui.action_save.triggered.connect(self.on_action_save)

    def set_selection(self, current: QModelIndex, old: QModelIndex):
        self.current_model_index = current
        self.data_mapper.setCurrentModelIndex(current)

        self.pwm_controller.set_selection(current)
        self.digital_output_controller.set_selection(current)
        self.digital_input_controller.set_selection(current)
        self.on_update_ui(current.row())

    def on_mode_changed(self, text: str):
        pin_type = self.ui.comboBox_type.currentText()
        self.on_update_controllers(pin_type, text)

    def on_type_changed(self, text):
        pin_mode = self.ui.comboBox_mode.currentText()
        self.on_update_controllers(text, pin_mode)

    def showEvent(self, a0: QtGui.QShowEvent):
        pin_type = self.ui.comboBox_type.currentText()
        pin_mode = self.ui.comboBox_mode.currentText()
        self.on_update_controllers(pin_type, pin_mode)
        self.on_update_ui(0)

    # This method updates the ui values when a new pin is selected in the list view
    def on_update_ui(self, index: int):
        pin = PIN_LIST[index]
        self.ui.comboBox_mode.setEnabled(not pin.enable)
        self.ui.comboBox_type.setEnabled(not pin.enable)
        self.pwm_controller.ui.button_pwm.setEnabled(pin.enable)
        self.pwm_controller.ui.slider_duty_cycle.setEnabled(pin.enable)
        self.pwm_controller.ui.slider_frequency.setEnabled(pin.enable)
        self.pwm_controller.ui.spinbox_frequency.setEnabled(pin.enable)
        self.pwm_controller.ui.spinbox_duty_cycle.setEnabled(pin.enable)
        self.digital_input_controller.ui.pushButton_read.setEnabled(pin.enable)
        self.digital_output_controller.ui.slider_value.setEnabled(pin.enable)
        self.digital_output_controller.ui.spinbox_value.setEnabled(pin.enable)
        self.ui.button_enable.setChecked(pin.enable)
        if pin.enable:
            self.ui.button_enable.setText("Disable")
        else:
            self.ui.button_enable.setText("Enable")

    # This method updates the ui values and sets GPIO values also
    def on_button_enable(self, value):
        self.ui.comboBox_type.setEnabled(not value)
        self.ui.comboBox_mode.setEnabled(not value)
        self.pwm_controller.ui.button_pwm.setEnabled(value)
        self.pwm_controller.ui.slider_duty_cycle.setEnabled(value)
        self.pwm_controller.ui.slider_frequency.setEnabled(value)
        self.pwm_controller.ui.spinbox_frequency.setEnabled(value)
        self.pwm_controller.ui.spinbox_duty_cycle.setEnabled(value)
        self.digital_input_controller.ui.pushButton_read.setEnabled(value)
        self.digital_output_controller.ui.slider_value.setEnabled(value)
        self.digital_output_controller.ui.spinbox_value.setEnabled(value)
        pin = PIN_LIST[self.current_model_index.row()]
        pin.enable = value

        if value:
            self.ui.button_enable.setText("Disable")

            if pin.type.__eq__("Input") and pin.mode.__eq__("Digital"):
                GPIO.setup(pin.id, GPIO.IN)
            else:
                if pin.mode.__eq__("Digital"):
                    GPIO.setup(pin.id, GPIO.OUT)
                    GPIO.output(pin.id, pin.value)
                else:
                    GPIO.setup(pin.id, GPIO.OUT)
                    if not pin.pwm_instance:
                        pin.pwm_instance = GPIO.PWM(pin.id, pin.frequency)

        else:
            self.ui.button_enable.setText("Enable")
            self.pwm_controller.ui.button_pwm.setText("Start")
            self.pwm_controller.ui.button_pwm.setChecked(False)
            self.pwm_controller.ui.button_pwm.setEnabled(False)

            if pin.type.__eq__("Input") and pin.mode.__eq__("Digital"):
                GPIO.setup(pin.id, GPIO.IN)
            else:
                if pin.mode.__eq__("Digital"):
                    GPIO.setup(pin.id, GPIO.OUT)
                    GPIO.output(pin.id, 0)
                else:
                    if pin.pwm_instance:
                        pin.pwm_instance.stop()
                        pin.pwm_instance = None

    # This method shows or hides the controllers based on the selection made to pin mode and type
    def on_update_controllers(self, pin_type: str, pin_mode: str):
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

    # About method show a message box
    def on_action_about(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Raspberry Pi GPIO Control About")
        msg.setText("This tool has been made by Daniel-Domiţian Iuonac and Sebastian Mecheş.")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    """
        This is called when Save configuration is pressed
        A FileDialog is shown and a file name must be provided 
        Saves the current pins configuration
    """
    def on_action_save(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        path = os.getcwd() + "/db/"

        file_path = file_dialog.getSaveFileName(QtWidgets.QWidget(), "Save G.P.I.O Configuration", path,
                                                filter="Json file (*.json)")
        filename = file_path[0]

        if filename:
            if ".json" not in filename:
                filename += ".json"
            from db import save_configuration
            save_configuration(filename)

    """ 
        This method is load the pins configuration when Load button is pressed
        It opens a File Dialog and lets user to select the configuration file
    """
    def on_action_load(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        path = os.getcwd() + "/db/"

        file_path = file_dialog.getOpenFileName(QtWidgets.QWidget(), "Load G.P.I.O Configuration", path,
                                                filter="Json file (*.json)")
        filename = file_path[0]

        if filename:
            if ".json" not in filename:
                filename += ".json"
            from db import load_configuration
            load_configuration(filename)
            self.model.removeRows(0, 27)
            for pin in PIN_LIST:
                self.model.insert([0, pin])


# This controller is for License Ui Form
class LicenseController(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LicenseController, self).__init__(parent, flags=Qt.Widget)
        self.ui = Ui_License()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModal)
        self.ui.button_close.clicked.connect(self.close)
        file = open("LICENSE", "r")
        text = file.read()
        file.close()
        self.ui.text.setPlainText(text)
