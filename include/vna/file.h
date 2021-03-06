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


#ifndef INCLUDED_VNA_FILE_H
#define INCLUDED_VNA_FILE_H

#include <vna/api.h>
#include <gnuradio/sync_block.h>
#include <string.h>

namespace gr {
  namespace vna {

    /*!
     * \brief <+description of block+>
     * \ingroup vna
     *
     */
    class VNA_API file : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<file> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of vna::file.
       *
       * To avoid accidental use of raw pointers, vna::file's
       * constructor is in a private implementation
       * class. vna::file::make is the public interface for
       * creating new instances.
       */
      static sptr make(std::string filename);
    };

  } // namespace vna
} // namespace gr

#endif /* INCLUDED_VNA_FILE_H */

