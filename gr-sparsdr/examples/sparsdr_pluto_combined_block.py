#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Sparsdr Pluto Combined Block
# GNU Radio version: 3.8.3.0

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sparsdr
import distutils.spawn


class sparsdr_pluto_combined_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Sparsdr Pluto Combined Block")

        ##################################################
        # Variables
        ##################################################
        self.freq = freq = 0*2.475e9+1*2.426e9+0*2.425e9
        self.freq_c = freq_c = freq - 14e6
        variable_sparsdr_combined_pluto_receiver_0_bands = sparsdr.band_spec_vector()
        variable_sparsdr_combined_pluto_receiver_0_bands.push_back(sparsdr.band_spec(freq+0*2.426e9, 64))
        self.variable_sparsdr_combined_pluto_receiver_0 = variable_sparsdr_combined_pluto_receiver_0 = sparsdr.combined_pluto_receiver(uri='ip:192.168.2.1', buffer_size=1024 * 1024, fft_size=1024, center_frequency=int(freq_c+0*2412000000), bands=variable_sparsdr_combined_pluto_receiver_0_bands, reconstruct_path=distutils.spawn.find_executable('/home/gnuradio/.cargo/bin/sparsdr_reconstruct'), zero_gaps=False)
        self.variable_sparsdr_combined_pluto_receiver_0.set_frequency(int(freq_c+0*2412000000))
        self.variable_sparsdr_combined_pluto_receiver_0.set_gain_control_mode('manual')
        self.variable_sparsdr_combined_pluto_receiver_0.set_gain(60)
        self.variable_sparsdr_combined_pluto_receiver_0.stop_all()
        self.variable_sparsdr_combined_pluto_receiver_0.set_shift_amount(6)
        self.variable_sparsdr_combined_pluto_receiver_0.set_fft_size(1024)
        self.variable_sparsdr_combined_pluto_receiver_0.load_rounded_hann_window(1024)
        self.variable_sparsdr_combined_pluto_receiver_0.set_bin_spec('0..1024:204800')
        self.variable_sparsdr_combined_pluto_receiver_0.start_all()

        ##################################################
        # Blocks
        ##################################################
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_gr_complex*1, '', "")
        self.blocks_tag_debug_0.set_display(True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.variable_sparsdr_combined_pluto_receiver_0, 0), (self.blocks_tag_debug_0, 0))


    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_freq_c(self.freq - 14e6)

    def get_freq_c(self):
        return self.freq_c

    def set_freq_c(self, freq_c):
        self.freq_c = freq_c

    def get_variable_sparsdr_combined_pluto_receiver_0(self):
        return self.variable_sparsdr_combined_pluto_receiver_0

    def set_variable_sparsdr_combined_pluto_receiver_0(self, variable_sparsdr_combined_pluto_receiver_0):
        self.variable_sparsdr_combined_pluto_receiver_0 = variable_sparsdr_combined_pluto_receiver_0





def main(top_block_cls=sparsdr_pluto_combined_block, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
