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
#include "sweep_impl.h"
#include<math.h>

#define PI 3.14159265359
#define STEPS 10

namespace gr {
  namespace vna {

    sweep::sptr
    sweep::make()
    {
      return gnuradio::get_initial_sptr
        (new sweep_impl());
    }

    /*
     * The private constructor
     */
    sweep_impl::sweep_impl()
      : gr::sync_block("sweep",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(1, 1, sizeof(float)))
    {}

    /*
     * Our virtual destructor.
     */
    sweep_impl::~sweep_impl()
    {
    }

    int
    sweep_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const float *in = (const float *) input_items[0];
        float *out = (float *) output_items[0];

        static float fReg = 0;
        static int times = 0;
        int tLimit = 64e3;
/*        
        int fVec[STEPS];
        for(int i=0;i<STEPS;++i){
                fVec[i] = floor(i*1e2/STEPS);
        }
       */ 
        for(int i=0;i<noutput_items;i++){
                out[i] = (fReg-STEPS/2)*200;
        }
        
        times++;
        // modify freq after X number of samples
        if(times == tLimit) {
                times = 0; 
                fReg++;
                fReg = fmod(fReg,STEPS);
        }
        
        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace vna */
} /* namespace gr */

