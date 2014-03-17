#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Meas Block
# Generated: Mon Mar 17 11:31:30 2014
##################################################

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
import howto
import threading
import time
import vna
import wx

class meas_block(grc_wxgui.top_block_gui):

    def __init__(self, samp_rate=32e3, sweep_rate=32e3, poll_rate=32e3, start_freq=-1e3, stop_freq=1e3, num_steps=10, filename_phase_data="/home/balint/workspace/gr-vna/apps/phase.dat", filename_mag_data="/home/balint/workspace/gr-vna/apps/mag.dat"):
        grc_wxgui.top_block_gui.__init__(self, title="Meas Block")

        ##################################################
        # Parameters
        ##################################################
        self.samp_rate = samp_rate
        self.sweep_rate = sweep_rate
        self.poll_rate = poll_rate
        self.start_freq = start_freq
        self.stop_freq = stop_freq
        self.num_steps = num_steps
        self.filename_phase_data = filename_phase_data
        self.filename_mag_data = filename_mag_data

        ##################################################
        # Variables
        ##################################################
        self.sweep_freq = sweep_freq = 0
        self.im_part = im_part = 1
        self.dc_offset = dc_offset = 0

        ##################################################
        # Blocks
        ##################################################
        self.blocks_probe_signal_x_0 = blocks.probe_signal_f()
        def _sweep_freq_probe():
        	while True:
        		val = self.blocks_probe_signal_x_0.level()
        		try: self.set_sweep_freq(val)
        		except AttributeError, e: pass
        		time.sleep(1.0/(poll_rate))
        _sweep_freq_thread = threading.Thread(target=_sweep_freq_probe)
        _sweep_freq_thread.daemon = True
        _sweep_freq_thread.start()
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
        self.vna_sweep_par_0 = vna.sweep_par(sweep_rate, start_freq, stop_freq, num_steps)
        self.howto_file_0_0 = howto.file(filename_mag_data)
        self.howto_file_0 = howto.file(filename_phase_data)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(1, 1, 10)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, sweep_freq, 1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.001, 0)
        self.analog_const_source_x_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, im_part)
        self.analog_const_source_x_0_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, dc_offset)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, sweep_freq)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.vna_sweep_par_0, 0), (self.blocks_probe_signal_x_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.howto_file_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.howto_file_0, 1))
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.howto_file_0_0, 1))
        self.connect((self.analog_const_source_x_0, 0), (self.howto_file_0_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.analog_const_source_x_0_1, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_conjugate_cc_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_sweep_rate(self):
        return self.sweep_rate

    def set_sweep_rate(self, sweep_rate):
        self.sweep_rate = sweep_rate

    def get_poll_rate(self):
        return self.poll_rate

    def set_poll_rate(self, poll_rate):
        self.poll_rate = poll_rate

    def get_start_freq(self):
        return self.start_freq

    def set_start_freq(self, start_freq):
        self.start_freq = start_freq

    def get_stop_freq(self):
        return self.stop_freq

    def set_stop_freq(self, stop_freq):
        self.stop_freq = stop_freq

    def get_num_steps(self):
        return self.num_steps

    def set_num_steps(self, num_steps):
        self.num_steps = num_steps

    def get_filename_phase_data(self):
        return self.filename_phase_data

    def set_filename_phase_data(self, filename_phase_data):
        self.filename_phase_data = filename_phase_data

    def get_filename_mag_data(self):
        return self.filename_mag_data

    def set_filename_mag_data(self, filename_mag_data):
        self.filename_mag_data = filename_mag_data

    def get_sweep_freq(self):
        return self.sweep_freq

    def set_sweep_freq(self, sweep_freq):
        self.sweep_freq = sweep_freq
        self.analog_const_source_x_0.set_offset(self.sweep_freq)
        self.analog_sig_source_x_1.set_frequency(self.sweep_freq)

    def get_im_part(self):
        return self.im_part

    def set_im_part(self, im_part):
        self.im_part = im_part
        self.analog_const_source_x_0_1.set_offset(self.im_part)
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
    parser.add_option("", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(32e3),
        help="Set samp_rate [default=%default]")
    parser.add_option("", "--sweep-rate", dest="sweep_rate", type="eng_float", default=eng_notation.num_to_str(32e3),
        help="Set sweep_rate [default=%default]")
    parser.add_option("", "--poll-rate", dest="poll_rate", type="eng_float", default=eng_notation.num_to_str(32e3),
        help="Set poll_rate [default=%default]")
    parser.add_option("", "--start-freq", dest="start_freq", type="eng_float", default=eng_notation.num_to_str(-1e3),
        help="Set start_freq [default=%default]")
    parser.add_option("", "--stop-freq", dest="stop_freq", type="eng_float", default=eng_notation.num_to_str(1e3),
        help="Set stop_freq [default=%default]")
    parser.add_option("", "--num-steps", dest="num_steps", type="intx", default=10,
        help="Set num_steps [default=%default]")
    parser.add_option("", "--filename-phase-data", dest="filename_phase_data", type="string", default="/home/balint/workspace/gr-vna/apps/phase.dat",
        help="Set filename_phase_data [default=%default]")
    parser.add_option("", "--filename-mag-data", dest="filename_mag_data", type="string", default="/home/balint/workspace/gr-vna/apps/mag.dat",
        help="Set filename_mag_data [default=%default]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    tb = meas_block(samp_rate=options.samp_rate, sweep_rate=options.sweep_rate, poll_rate=options.poll_rate, start_freq=options.start_freq, stop_freq=options.stop_freq, num_steps=options.num_steps, filename_phase_data=options.filename_phase_data, filename_mag_data=options.filename_mag_data)
    tb.Start(True)
    tb.Wait()

