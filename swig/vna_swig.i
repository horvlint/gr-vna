/* -*- c++ -*- */

#define VNA_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "vna_swig_doc.i"

%{
#include "vna/sweep.h"
#include "vna/sweep_par.h"
#include "vna/file.h"
%}


%include "vna/sweep.h"
GR_SWIG_BLOCK_MAGIC2(vna, sweep);

%include "vna/sweep_par.h"
GR_SWIG_BLOCK_MAGIC2(vna, sweep_par);

%include "vna/file.h"
GR_SWIG_BLOCK_MAGIC2(vna, file);
