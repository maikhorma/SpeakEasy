'''
Created on Feb 12, 2014

@author: mark
'''
import engine_sapi5 as esapi
import sys
from win32com.client           import Dispatch, getevents, constants
from win32com.client.gencache  import EnsureDispatch
from pywintypes                import com_error

class Sapi5InprocEngine(esapi.Sapi5Engine):
    _name = "sapi5inproc"
    
    @classmethod
    def is_available(cls):
        """ Check whether this engine is available. """
        try:
            Dispatch("SAPI.SpInProcRecognizer")
        except com_error:
            return False
        return True    

    #-----------------------------------------------------------------------

    def __init__(self):
        print "ME INIT!!"
        EnsureDispatch("SAPI.SpInProcRecognizer")
        EnsureDispatch("SAPI.SpVoice")
        EnsureDispatch("SAPI.SpMMAudioIn")
        self._recognizer  = Dispatch("SAPI.SpInProcRecognizer")
        self._recognizer.AudioInputStream = Dispatch("SAPI.SpMMAudioIn")
        self._speaker     = Dispatch("SAPI.SpVoice")
        self._compiler    = esapi.Sapi5Compiler()

        self._recognition_observer_manager = None

    #-----------------------------------------------------------------------
    # Methods for working with grammars.

    def load_grammar(self, grammar):
        """ Load the given *grammar*. """
        self._log.debug("Loading grammar %s." % grammar.name)
        grammar.engine = self
        context = self._recognizer.CreateRecoContext()
        handle = self._compiler.compile_grammar(grammar, context)
        wrapper = InProcGrammarWrapper(grammar, handle, context, self)
        self._set_grammar_wrapper(grammar, wrapper)

        self.activate_grammar(grammar)
        for l in grammar.lists:
            l._update()

    
class InProcGrammarWrapper(esapi.GrammarWrapper):
    def phrase_start_callback(self, stream_number, stream_position):
        self.grammar.process_begin(sys.executable, sys.executable,
                                   sys.executable)    