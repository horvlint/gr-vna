#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Mon Mar 17 11:25:07 2014
##################################################

execfile("/home/balint/.grc_gnuradio/meas_block.py")
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.im_part = im_part = 0
        self.dc_offset = dc_offset = 0

        ##################################################
        # Blocks
        ##################################################
        _im_part_sizer = wx.BoxSizer(wx.VERTICAL)
        self._im_part_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_im_part_sizer,
        	value=self.im_part,
        	callback=self.set_im_part,
        	label='im_part',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._im_part_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_im_part_sizer,
        	value=self.im_part,
        	callback=self.set_im_part,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_im_part_sizer)
        _dc_offset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._dc_offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_dc_offset_sizer,
        	value=self.dc_offset,
        	callback=self.set_dc_offset,
        	label='dc_offset',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._dc_offset_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_dc_offset_sizer,
        	value=self.dc_offset,
        	callback=self.set_dc_offset,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_dc_offset_sizer)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.meas_block_1 = meas_block(
            stop_freq=1e3,
            filename_phase_data="/home/balint/workspace/gr-vna/apps/phase.dat",
            filename_mag_data="/home/balint/workspace/gr-vna/apps/mag.dat",
            samp_rate=32e3,
            start_freq=-1e3,
            num_steps=10,
            sweep_rate=32e3,
            poll_rate=32e3,
        )
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 8e2, 1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.001, 0)
        self.analog_const_source_x_0_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, dc_offset)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, im_part)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0_0, 0), (self.meas_block_1, 1))
        self.connect((self.meas_block_1, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.meas_block_1, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_im_part(self):
        return self.im_part

    def set_im_part(self, im_part):
        self.im_part = im_part
        self.analog_const_source_x_0.set_offset(self.im_part)
        self._im_part_slider.set_value(self.im_part)
        self._im_part_text_box.set_value(self.im_part)

    def get_dc_offset(self):
        return self.dc_offset

    def set_dc_offset(self, dc_offset):
        self.dc_offset = dc_offset
        self.analog_const_source_x_0_0_0.set_offset(self.dc_offset)
        self._dc_offset_slider.set_value(self.dc_offset)
        self._dc_offset_text_box.set_value(self.dc_offset)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()

