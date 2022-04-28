#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Pluto single-channel reconstruct
# GNU Radio version: 3.8.3.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sparsdr
import distutils.spawn

from gnuradio import qtgui

class pluto_single_channel(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Pluto single-channel reconstruct")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Pluto single-channel reconstruct")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "pluto_single_channel")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        variable_sparsdr_reconstruct_0_bands = sparsdr.band_spec_vector()
        variable_sparsdr_reconstruct_0_bands.push_back(sparsdr.band_spec(26e6, 64))
        self.variable_sparsdr_reconstruct_0 = variable_sparsdr_reconstruct_0 = sparsdr.reconstruct(bands=variable_sparsdr_reconstruct_0_bands, reconstruct_path=distutils.spawn.find_executable('sparsdr_reconstruct'), sample_format='Pluto v2', zero_gaps=False, compression_fft_size=1024)

        ##################################################
        # Blocks
        ##################################################
        self.sparsdr_compressing_pluto_source_0 = sparsdr.compressing_pluto_source('ip:192.168.2.1', 1024 * 16)
        self.sparsdr_compressing_pluto_source_0.set_frequency(int(2.4e9))
        self.sparsdr_compressing_pluto_source_0.set_gain_control_mode('manual')
        self.sparsdr_compressing_pluto_source_0.set_gain(60)
        self.sparsdr_compressing_pluto_source_0.stop_all()
        self.sparsdr_compressing_pluto_source_0.set_shift_amount(6)
        self.sparsdr_compressing_pluto_source_0.set_fft_size(1024)
        self.sparsdr_compressing_pluto_source_0.load_rounded_hann_window(1024)
        self.sparsdr_compressing_pluto_source_0.set_bin_spec('416..450:12800')
        self.sparsdr_compressing_pluto_source_0.set_average_interval(2 ** 16)
        self.sparsdr_compressing_pluto_source_0.start_all()
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            64, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            2.426e9, #fc
            64.0 / 1024.0 * 61.44e6, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.blocks_probe_rate_0 = blocks.probe_rate(gr.sizeof_int*1, 500.0, 0.15)
        self.blocks_message_debug_0 = blocks.message_debug()


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_probe_rate_0, 'rate'), (self.blocks_message_debug_0, 'print'))
        self.connect((self.sparsdr_compressing_pluto_source_0, 0), (self.blocks_probe_rate_0, 0))
        self.connect((self.sparsdr_compressing_pluto_source_0, 0), (self.variable_sparsdr_reconstruct_0, 0))
        self.connect((self.variable_sparsdr_reconstruct_0, 0), (self.qtgui_waterfall_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pluto_single_channel")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_sparsdr_reconstruct_0(self):
        return self.variable_sparsdr_reconstruct_0

    def set_variable_sparsdr_reconstruct_0(self, variable_sparsdr_reconstruct_0):
        self.variable_sparsdr_reconstruct_0 = variable_sparsdr_reconstruct_0





def main(top_block_cls=pluto_single_channel, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
