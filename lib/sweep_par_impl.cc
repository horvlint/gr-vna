/* -*- c++ -*- */
/* 
 * Copyright 2014 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <iostream>

#include <gnuradio/io_signature.h>
#include "sweep_par_impl.h"

namespace gr {
  namespace vna {

    sweep_par::sptr
    sweep_par::make(float rate,float start_freq, float stop_freq, int num_steps)
    {
      return gnuradio::get_initial_sptr
        (new sweep_par_impl(rate, start_freq, stop_freq, num_steps));
    }

    /*
     * The private constructor
     */
    sweep_par_impl::sweep_par_impl(float _rate,float _start_freq, float _stop_freq, int _num_steps)
      : gr::sync_block("sweep_par",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(1, 1, sizeof(float)))
    {
        if(_num_steps <= 0){
        	std::cout << "invalid number of steps (<= 0)" << std::endl;
        	exit(-1);
        }
        if(_stop_freq < start_freq){
        	std::cout << "cannot perform sweep: stop_freq < start_freq" << std::endl;
        	exit(-1);
        }    
    
    	rate = _rate;
    	start_freq = _start_freq;
    	stop_freq = _stop_freq;
    	num_steps = _num_steps;    	    
        
        float freq_step = (stop_freq - start_freq)/num_steps;
        freq_vec = new float[num_steps];
        for(int i=0;i<num_steps;++i){
                freq_vec[i] = start_freq + i*freq_step;
        }
    }

    /*
     * Our virtual destructor.
     */
    sweep_par_impl::~sweep_par_impl()
    {
    	delete [] freq_vec;
    }

    int
    sweep_par_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        float *out = (float *) output_items[0];
	
	static int freq_reg = 0;
	static int rate_cnt = 0;
	static int step_cnt = 0;

        for(int i=0; i<noutput_items;i++){
        	out[i] = freq_vec[freq_reg];
        }
        
        ++rate_cnt;
        if(rate_cnt == (int) this->rate){
        	rate_cnt = 0;
        	++freq_reg;
        	freq_reg %= num_steps;
	       	++step_cnt;
	       	if(step_cnt == num_steps){
	       		step_cnt = 0;
	       		std::cout << "Full sweep performed" << std::endl;
	       		//exit(-1);
	       	}
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace vna */
} /* namespace gr */

