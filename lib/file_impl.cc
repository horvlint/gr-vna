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

#include <gnuradio/io_signature.h>
#include "file_impl.h"
#include <string.h>
#include <iostream>
#include <fstream>
#include <cstring>


using namespace std;

namespace gr {
  namespace howto {

    file::sptr
    file::make(string filename)
    {
      return gnuradio::get_initial_sptr
        (new file_impl(filename));
    }

    /*
     * The private constructor
     */
    file_impl::file_impl(string _filename)
      : gr::sync_block("file",
              gr::io_signature::make(2, 2, sizeof(float)),
              gr::io_signature::make(0, 0, 0))
    {
    	filename = _filename;
    	myfile.open (filename.c_str(),ios::trunc);
    	myfile.close();
	myfile.open (filename.c_str(),ios::out | ios::app | ios::binary);    	
    }

    /*
     * Our virtual destructor.
     */
    file_impl::~file_impl()    
    {
    	myfile.close();
    }

    int
    file_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const float *in = (const float *) input_items[0];
        
        int ninputs = input_items.size ();
        
        for(int i = 0; i<noutput_items; ++i){
        	for(int j=0; j<ninputs; ++j){   		
			myfile << ((float *) input_items[j])[i];
			if(j==(ninputs-1)) myfile << ";" ;
			else myfile << "," ;
		}
		myfile << "\n";
	}

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace howto */
} /* namespace gr */

