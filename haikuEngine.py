#!/usr/bin/python
import random
#from textstat import textstat
import util.SyllableCounter

class HaikuEngine( object ):
	"""
		Markov chains lead to
		a solution insightful
		for RAGE Feb challenge Haiku!
	"""

	def __init__( self, order ):
		self.graph = {}
		self.text = None
		self.order = order
		self.group_size = self.order + 1
		return

	def train( self, filename ):
		'''
			Makes chains from training data
			More the merrier.
			Unoptimized way!
		'''
		self.text = file( filename ).read().split()
		self.text = self.text + self.text[ : self.order ]

		for i in xrange(0, len( self.text ) - self.group_size ):
			key = tuple( self.text[ i : i + self.order ] )
			value = self.text[ i + self.order ]

			if key in self.graph:
				self.graph[ key ].append( value )
			else:
				self.graph[ key ] = [ value ]
		return

	def generateHaiku2( self ):
		'''
			The one we call on,
			To make poetic haiku.
			Bless worthy Not yet
		'''
		index = random.randint( 0, len( self.text ) - self.order )
		result = self.text[ index : index + self.order ]
		length =  5 + 7 + 5  #As many words as expected Syllables
		for i in xrange( length ):
			state = tuple( result[ len( result ) - self.order : ] )
			nextWord = random.choice(self.graph[ state ] )
			result.append( nextWord )


		syllables, line = 0, 1
		for word in result:
			print word,
			#syllables += textstat.textstat.syllable_count( word )
			syllables += util.SyllableCounter.CountSyllables( word )
			if syllables >=5 and line != 2:
				print
				line += 1
				syllables = 0
				if line > 3:
					return
			elif syllables >= 7 and line == 2:
				print
				line += 1
				syllables = 0
			
					
	def generateHaiku( self ):
		'''
			The one we call on,
			To make poetic haiku.
			Bless worthy Not yet
		'''
		index = random.randint( 0, len( self.text ) - self.order )
		result = self.text[ index : index + self.order ]
		length =  5 + 7 + 5  #As many words as expected Syllables
		for i in xrange( length ):
			state = tuple( result[ len( result ) - self.order : ] )
			nextWord = random.choice(self.graph[ state ] )
			result.append( nextWord )


		syllables, line = 0, 1
		for word in result:
			print word,
			#syllables += textstat.textstat.syllable_count( word )
			syllables += util.SyllableCounter.CountSyllables( word )
			if syllables >=5 and line != 2:
				print
				line += 1
				syllables = 0
				if line > 3:
					return
			elif syllables >= 7 and line == 2:
				print
				line += 1
				syllables = 0
	
	def avg_value(self):
		'''
			A helper function!
			to gauge strength of the trained chains
			1.2 or more fine.
		'''
		vals = [len(x) for x in self.graph.values()]
		return float(sum(vals)) / len(vals)
		

def makeHaiku(filename, order, length):
	m = HaikuEngine(order)
	m.train(filename)
	print m.generate(length)
	return m
