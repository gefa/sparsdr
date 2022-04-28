#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Sparsdr Pluto Combined Block 900Mhz
# GNU Radio version: 3.8.3.0

from gnuradio import analog
import math
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import lora_sdr
import sparsdr
import distutils.spawn
import zwave


class sparsdr_pluto_combined_block_900mhz(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Sparsdr Pluto Combined Block 900Mhz")

        ##################################################
        # Variables
        ##################################################
        self.freq1 = freq1 = 0*2.405e9+0*2.426e9+908.60e6
        self.freq0 = freq0 = 0*2.425e9+0*2.426e9+910290000
        self.bins0 = bins0 = 14*0+8*0+50
        self.samp_rate = samp_rate = bins0*61440000/1024
        self.freq_c = freq_c = 0*(freq1 - 14e6) + 0*2.425e9 + freq0
        variable_sparsdr_combined_pluto_receiver_0_bands = sparsdr.band_spec_vector()
        variable_sparsdr_combined_pluto_receiver_0_bands.push_back(sparsdr.band_spec(freq1+0*2.426e9, bins0))
        variable_sparsdr_combined_pluto_receiver_0_bands.push_back(sparsdr.band_spec(freq0, bins0))
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
        self.pay_len = pay_len = 23
        self.impl_head = impl_head = False
        self.freq2 = freq2 = 1*2.450e9+0*2.426e9
        self.cr = cr = 0

        ##################################################
        # Blocks
        ##################################################
        self.zwave_packet_sink_0 = zwave.packet_sink()
        self.rational_resampler_xxx_0_0_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=6,
                taps=[-0.128616616593872,	-0.212206590789194,	-0.180063263231421,	3.89817183251938e-17	,0.300105438719035	,0.636619772367581	,0.900316316157106,	1	,0.900316316157106,	0.636619772367581,	0.300105438719035,	3.89817183251938e-17,	-0.180063263231421,	-0.212206590789194,	-0.128616616593872],
                fractional_bw=None)
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                2.5*40e3,
                10e3,
                firdes.WIN_HAMMING,
                6.76))
        self.lora_sdr_hier_rx_0 = lora_sdr.hier_rx(125000, 125000, 7, impl_head, cr, pay_len, True, True)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, taps, -200e3, samp_rate)
        self.digital_clock_recovery_mm_xx_0_0 = digital.clock_recovery_mm_ff(int(samp_rate/40000), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_socket_pdu_0_0 = blocks.socket_pdu('UDP_CLIENT', '127.0.0.1', '52003', 10000, False)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf(2*(samp_rate)/(2*math.pi*20e3/8.0))


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lora_sdr_hier_rx_0, 'msg'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.zwave_packet_sink_0, 'out'), (self.blocks_socket_pdu_0_0, 'pdus'))
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.zwave_packet_sink_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_clock_recovery_mm_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0, 0), (self.lora_sdr_hier_rx_0, 0))
        self.connect((self.variable_sparsdr_combined_pluto_receiver_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.variable_sparsdr_combined_pluto_receiver_0, 1), (self.rational_resampler_xxx_0_0_0_0, 0))


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
        self.analog_quadrature_demod_cf_0_0.set_gain(2*(self.samp_rate)/(2*math.pi*20e3/8.0))
        self.digital_clock_recovery_mm_xx_0_0.set_omega(int(self.samp_rate/40000))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 2.5*40e3, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_freq_c(self):
        return self.freq_c

    def set_freq_c(self, freq_c):
        self.freq_c = freq_c

    def get_variable_sparsdr_combined_pluto_receiver_0(self):
        return self.variable_sparsdr_combined_pluto_receiver_0

    def set_variable_sparsdr_combined_pluto_receiver_0(self, variable_sparsdr_combined_pluto_receiver_0):
        self.variable_sparsdr_combined_pluto_receiver_0 = variable_sparsdr_combined_pluto_receiver_0

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.freq_xlating_fir_filter_xxx_0.set_taps(self.taps)

    def get_pay_len(self):
        return self.pay_len

    def set_pay_len(self, pay_len):
        self.pay_len = pay_len

    def get_impl_head(self):
        return self.impl_head

    def set_impl_head(self, impl_head):
        self.impl_head = impl_head

    def get_freq2(self):
        return self.freq2

    def set_freq2(self, freq2):
        self.freq2 = freq2

    def get_cr(self):
        return self.cr

    def set_cr(self, cr):
        self.cr = cr





def main(top_block_cls=sparsdr_pluto_combined_block_900mhz, options=None):
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
