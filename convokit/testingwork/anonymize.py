from convokit.phrasing_motifs import censorNouns
from convokit.text_processing import textParser
# convokit documentation on textparser is useful, tells what tok, rt, etc is
# the documentation on the phrasing motifs is less so
import spacy


nlp = spacy.load('en_core_web_sm')
parse = textParser.process_text('Hello my name is Emma', mode='parse', sent_tokenizer=None, spacy_nlp = nlp)
print(censorNouns.censor_nouns(parse))
parse_ticket = textParser.process_text('This ticket is for creation of Dons OnBase account. There is a separate ticket that Les has for creation of the Network ID account and provisioning of it.  Please follow up with Gayle Bauer with any account information.  Dons Network ID is: dhasseltine,1968', mode='parse', sent_tokenizer=None, spacy_nlp = nlp)
print(censorNouns.censor_nouns(parse_ticket))
