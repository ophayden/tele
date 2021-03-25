#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Author: Chironex
# Generated: Fri Jan 29 17:53:13 2021
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import histosink_gl
from gnuradio.wxgui import numbersink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.squelch_slider_0 = squelch_slider_0 = 0
        self.freq_slider = freq_slider = 2.44e9
        self.squelch = squelch = squelch_slider_0
        self.samp_rate = samp_rate = 10000000
        self.freq = freq = freq_slider

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit='Units',
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label='Number Plot',
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0.win)
        self.wxgui_histosink2_0 = histosink_gl.histo_sink_f(
        	self.GetWin(),
        	title='Histogram Plot',
        	num_bins=27,
        	frame_size=1000,
        )
        self.Add(self.wxgui_histosink2_0.win)
        _squelch_slider_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._squelch_slider_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_squelch_slider_0_sizer,
        	value=self.squelch_slider_0,
        	callback=self.set_squelch_slider_0,
        	label='squelch_slider_0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._squelch_slider_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_squelch_slider_0_sizer,
        	value=self.squelch_slider_0,
        	callback=self.set_squelch_slider_0,
        	minimum=0,
        	maximum=30,
        	num_steps=30,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_squelch_slider_0_sizer)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(True, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        _freq_slider_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_slider_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_slider_sizer,
        	value=self.freq_slider,
        	callback=self.set_freq_slider,
        	label='freq_slider',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_slider_sizer,
        	value=self.freq_slider,
        	callback=self.set_freq_slider,
        	minimum=2.42e9,
        	maximum=2.49e9,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_slider_sizer)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_float*1, '192.168.0.2', 9000, 1472, True)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(50000, 20, 4000)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.wxgui_histosink2_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.wxgui_numbersink2_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_conjugate_cc_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))

    def get_squelch_slider_0(self):
        return self.squelch_slider_0

    def set_squelch_slider_0(self, squelch_slider_0):
        self.squelch_slider_0 = squelch_slider_0
        self._squelch_slider_0_slider.set_value(self.squelch_slider_0)
        self._squelch_slider_0_text_box.set_value(self.squelch_slider_0)
        self.set_squelch(self.squelch_slider_0)

    def get_freq_slider(self):
        return self.freq_slider

    def set_freq_slider(self, freq_slider):
        self.freq_slider = freq_slider
        self.set_freq(self.freq_slider)
        self._freq_slider_slider.set_value(self.freq_slider)
        self._freq_slider_text_box.set_value(self.freq_slider)

    def get_squelch(self):
        return self.squelch

    def set_squelch(self, squelch):
        self.squelch = squelch

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_source_0.set_center_freq(self.freq, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
