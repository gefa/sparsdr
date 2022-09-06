#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Sparsdr Freq 900Mhz 4Band
# GNU Radio version: 3.8.3.0

from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import zeromq
import sparsdr
import distutils.spawn


class sparsdr_freq_900mhz_4band(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Sparsdr Freq 900Mhz 4Band")

        ##################################################
        # Variables
        ##################################################
        self.freq1 = freq1 = 0*2.405e9+0*2.426e9+908.60e6
        self.freq0 = freq0 = 0*2.425e9+0*2.426e9+910290000
        self.bins0 = bins0 = 14*0+8*0+50
        self.samp_rate = samp_rate = bins0*61440000/1024
        self.freq_c = freq_c = 0*(freq1 - 14e6) + 0*2.425e9 + freq0
        self.freq3 = freq3 = 923.29e6
        self.freq2 = freq2 = 0*2.450e9+0*2.426e9+916e6
        variable_sparsdr_combined_pluto_receiver_0_bands = sparsdr.band_spec_vector()
        variable_sparsdr_combined_pluto_receiver_0_bands.push_back(sparsdr.band_spec(freq1, bins0))
        variable_sparsdr_combined_pluto_receiver_0_bands.push_back(sparsdr.band_spec(freq0, bins0))
        variable_sparsdr_combined_pluto_receiver_0_bands.push_back(sparsdr.band_spec(freq2, bins0))
        variable_sparsdr_combined_pluto_receiver_0_bands.push_back(sparsdr.band_spec(freq3, bins0))
        self.variable_sparsdr_combined_pluto_receiver_0 = variable_sparsdr_combined_pluto_receiver_0 = sparsdr.combined_pluto_receiver(uri='ip:192.168.2.1', buffer_size=1024 * 1024, fft_size=1024, center_frequency=int(freq_c+0*2412000000), bands=variable_sparsdr_combined_pluto_receiver_0_bands, reconstruct_path=distutils.spawn.find_executable('/home/gnuradio/.cargo/bin/sparsdr_reconstruct'), zero_gaps=False)
        self.variable_sparsdr_combined_pluto_receiver_0.set_frequency(int(freq_c+0*2412000000))
        self.variable_sparsdr_combined_pluto_receiver_0.set_gain_control_mode('slow_attack')
        self.variable_sparsdr_combined_pluto_receiver_0.stop_all()
        self.variable_sparsdr_combined_pluto_receiver_0.set_shift_amount(6)
        self.variable_sparsdr_combined_pluto_receiver_0.set_fft_size(1024)
        self.variable_sparsdr_combined_pluto_receiver_0.load_rounded_hann_window(1024)
        self.variable_sparsdr_combined_pluto_receiver_0.set_bin_spec('0..1024:204800')
        self.variable_sparsdr_combined_pluto_receiver_0.start_all()
        self.taps = taps = firdes.low_pass(1,samp_rate,150e3,50e3,firdes.WIN_HAMMING)
        self.plen = plen = 0

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_pub_sink_0_0_0_0 = zeromq.pub_sink(gr.sizeof_gr_complex, 1, 'tcp://*:55558', 100, False, -1)
        self.zeromq_pub_sink_0_0_0 = zeromq.pub_sink(gr.sizeof_gr_complex, 1, 'tcp://*:55557', 100, False, -1)
        self.zeromq_pub_sink_0_0 = zeromq.pub_sink(gr.sizeof_gr_complex, 1, 'tcp://*:55556', 100, False, -1)
        self.zeromq_pub_sink_0 = zeromq.pub_sink(gr.sizeof_gr_complex, 1, 'tcp://*:55555', 100, False, -1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.variable_sparsdr_combined_pluto_receiver_0, 0), (self.zeromq_pub_sink_0, 0))
        self.connect((self.variable_sparsdr_combined_pluto_receiver_0, 1), (self.zeromq_pub_sink_0_0, 0))
        self.connect((self.variable_sparsdr_combined_pluto_receiver_0, 2), (self.zeromq_pub_sink_0_0_0, 0))
        self.connect((self.variable_sparsdr_combined_pluto_receiver_0, 3), (self.zeromq_pub_sink_0_0_0_0, 0))


    def get_freq1(self):
        return self.freq1

    def set_freq1(self, freq1):
        self.freq1 = freq1
        self.set_freq_c(0*(self.freq1 - 14e6) + 0*2.425e9 + self.freq0)

    def get_freq0(self):
        return self.freq0

    def set_freq0(self, freq0):
        self.freq0 = freq0
        self.set_freq_c(0*(self.freq1 - 14e6) + 0*2.425e9 + self.freq0)

    def get_bins0(self):
        return self.bins0

    def set_bins0(self, bins0):
        self.bins0 = bins0
        self.set_samp_rate(self.bins0*61440000/1024)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_taps(firdes.low_pass(1,self.samp_rate,150e3,50e3,firdes.WIN_HAMMING))

    def get_freq_c(self):
        return self.freq_c

    def set_freq_c(self, freq_c):
        self.freq_c = freq_c

    def get_freq3(self):
        return self.freq3

    def set_freq3(self, freq3):
        self.freq3 = freq3

    def get_freq2(self):
        return self.freq2

    def set_freq2(self, freq2):
        self.freq2 = freq2

    def get_variable_sparsdr_combined_pluto_receiver_0(self):
        return self.variable_sparsdr_combined_pluto_receiver_0

    def set_variable_sparsdr_combined_pluto_receiver_0(self, variable_sparsdr_combined_pluto_receiver_0):
        self.variable_sparsdr_combined_pluto_receiver_0 = variable_sparsdr_combined_pluto_receiver_0

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps

    def get_plen(self):
        return self.plen

    def set_plen(self, plen):
        self.plen = plen





def main(top_block_cls=sparsdr_freq_900mhz_4band, options=None):
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
