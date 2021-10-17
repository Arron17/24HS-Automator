from PyQt6.QtCore import Qt
from logging import getLogger

from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton

from AutomatorGUI.gui.rescuecommands import RescueCommandsWindow
from AutomatorGUI.gui.sysinfo import SysInfoWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.logger = getLogger('AutomatorGUI')
        self.logger.info('Starting up...')

        main_widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel('24HS-Automator')
        default_font = title.font()
        default_font.setPointSize(24)
        title.setFont(default_font)
        layout.addWidget(title)
        layout.setAlignment(title, Qt.AlignmentFlag.AlignHCenter)

        button_data = [
            ('SFC / DISM / CHKDSK scans', 'rescuecommands', lambda: RescueCommandsWindow(self).exec()),
            ('MSInfo32 Report (Sysinfo)', 'sysinfo', lambda: SysInfoWindow(self).exec()),
            ('Check for updates', 'updates', None),
            ('Flash ISOs', 'isoflash', None),
            ('Enter safe mode', 'safemode', None),
            ('Enter BIOS', 'bios', None),
            ('Auto-DDU', 'ddu', None),
        ]
        for button_text, button_id, callback in button_data:
            button = QPushButton(button_text)
            button.setObjectName(button_id)
            button.setFixedWidth(300)
            if callback:
                button.clicked.connect(callback)
            else:
                button.setEnabled(False)
            layout.addWidget(button)
            layout.setAlignment(button, Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch()

        main_widget.setLayout(layout)
        self.setWindowTitle('24HS-Automator')
        self.setMinimumSize(500, 300)
        self.setCentralWidget(main_widget)
