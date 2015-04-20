#FLM: Component Dump
# Version 2.0
#
# Will look through a font and write out a text file that lists any glyph with a
# component(s), one glyph per line of the file. On each line, the script writes
# the glyph name, the width of the glyph, and then each component name and x, y
# offset for that compnent. These values are all semicolon seperated.
#
# Examples:
# Agrave;587.0;A;0;0;grave;70;0
# Aringacute;587.0;A;0;0;ring;155;139;acute;155;312
#
# This script was originally written in 2006 for John Hudson at Tiro Typeworks
#
# Version 2.0: Tested to work in RoboFont, license changed from GPL to MIT, and
#              put on Github.
#
# ---------------------
# The MIT License (MIT)
# 
# Copyright (c) 2015 Typefounding
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


#Imports
from robofab.world import CurrentFont
from robofab.interface.all.dialogs import PutFile, Message, ProgressBar

#Script
font = CurrentFont()
defaultName = font.info.fontName + '.txt'
filePath = PutFile('Save dump file', defaultName)
file = open(filePath, 'w')
tickCount = len(font)
bar = ProgressBar('Writing dump file', tickCount)
tick = 0
outList = []
for glyph in font:
	bar.tick(tick)
	tick = tick+1
	if len(glyph.components) != 0:
		output = glyph.name + ';' + str(glyph.width)
		componentNumber = 0
		while componentNumber < len(glyph.components):
			x, y = glyph.components[componentNumber].offset
			output = output + ';' + glyph.components[componentNumber].baseGlyph + ';' + str(x) + ';' + str(y)
			componentNumber = componentNumber + 1
		output = output + '\n'
		outList.append((glyph.index, output))
outDictionary = dict(outList)
outKeys = outDictionary.keys()
outKeys.sort()
keyCount = 0
while keyCount < len(outKeys):
	file.write(outDictionary[outKeys[keyCount]])
	keyCount = keyCount + 1

bar.close()
file.close()
Message('Dump file written')