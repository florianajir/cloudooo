##############################################################################
#
# Copyright (c) 2010 Nexedi SA and Contributors. All Rights Reserved.
#                    Priscila Manhaes  <psilva@iff.edu.br>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from magic import Magic
from cloudooo.handler.ffmpeg.handler import FFMPEGHandler
from cloudooo.handler.tests.handlerTestCase import HandlerTestCase, make_suite


file_detector = Magic(mime=True)


class TestAllFormats(HandlerTestCase):

  def afterSetUp(self):
    self.data = open("./data/test.ogv").read()
    self.kw = dict(env=dict(PATH=self.env_path))
    self.input = FFMPEGHandler(self.tmp_url, self.data, "ogv", **self.kw)

  def testAviFormat(self):
    """Test convert file to avi format the reverse convertion"""
    output_data = self.input.convert("avi")
    output_format = file_detector.from_buffer(output_data)
    output = FFMPEGHandler(self.tmp_url, output_data, "avi", **self.kw)
    input_data = output.convert("ogv")
    input_format = file_detector.from_buffer(input_data)
    self.assertEquals(output_format, 'video/avi')
    self.assertEquals(input_format, 'video/ogg')

  def testMp4Format(self):
    """Test convert file to mp4 format the reverse convertion"""
    output_data = self.input.convert("mp4")
    output_format = file_detector.from_buffer(output_data)
    output = FFMPEGHandler(self.tmp_url, output_data, "mp4", **self.kw)
    input_data = output.convert("ogv")
    input_format = file_detector.from_buffer(input_data)
    self.assertEquals(output_format, 'video/mp4')
    self.assertEquals(input_format, 'video/ogg')

  def testWebMFormat(self):
    """Test convert file to WebM format and the reverse convertion"""
    output_data = self.input.convert("webm")
    output_format = file_detector.from_buffer(output_data)
    output = FFMPEGHandler(self.tmp_url, output_data, "webm", **self.kw)
    input_data = output.convert("ogv")
    input_format = file_detector.from_buffer(input_data)
    self.assertEquals(output_format, 'video/webm')
    self.assertEquals(input_format, 'video/ogg')

  def testFlvFormat(self):
    """Test convert file to flash format the reverse convertion"""
    output_data = self.input.convert("flv")
    output_format = file_detector.from_buffer(output_data)
    output = FFMPEGHandler(self.tmp_url, output_data, "flv", **self.kw)
    input_data = output.convert("ogv")
    input_format = file_detector.from_buffer(input_data)
    self.assertEquals(output_format, 'application/x-shockwave-flash')
    self.assertEquals(input_format, 'video/ogg')

  def testMpegFormat(self):
    """Test convert file to Mpeg format the reverse convertion"""
    output_data = self.input.convert("mpeg")
    output_format = file_detector.from_buffer(output_data)
    output = FFMPEGHandler(self.tmp_url, output_data, "mpeg", **self.kw)
    input_data = output.convert("ogv")
    input_format = file_detector.from_buffer(input_data)
    self.assertEquals(output_format, 'video/mpeg')
    self.assertEquals(input_format, 'video/ogg')

  def testMkvFormat(self):
    """Test convert file to matroska format the reverse convertion"""
    output_data = self.input.convert("mkv")
    output_format = file_detector.from_buffer(output_data)
    output = FFMPEGHandler(self.tmp_url, output_data, "mkv", **self.kw)
    input_data = output.convert("ogv")
    input_format = file_detector.from_buffer(input_data)
    self.assertEquals(output_format, 'video/x-matroska')
    self.assertEquals(input_format, 'video/ogg')

  def testOggFormat(self):
    """Test convert file to ogg format the reverse convertion"""
    output_data = self.input.convert("ogg")
    output_format = file_detector.from_buffer(output_data)
    output = FFMPEGHandler(self.tmp_url, output_data, "ogg", **self.kw)
    input_data = output.convert("ogv")
    input_format = file_detector.from_buffer(input_data)
    self.assertEquals(output_format, 'application/ogg')
    self.assertEquals(input_format, 'video/ogg')


def test_suite():
  return make_suite(TestAllFormats)
