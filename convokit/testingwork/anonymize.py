from convokit.phrasing_motifs import censorNouns
from convokit.text_processing import textParser, TextProcessor
# convokit documentation on textparser is useful, tells what tok, rt, etc is
# the documentation on the phrasing motifs is less so
import spacy
from spacy import displacy
#visualizes spacy parses to see dependency
import nltk
import re
import json
import pandas as pd


def preprocess_text(text):
    """
    we can pull over a lot of anonymize.py from user-friendly and add them to
    this method
    """
    email_regex = email = re.compile('\S+@\S+.\S+')
    text = text.replace(email_regex, ' email@address ')

prep = TextProcessor(proc_fn=preprocess_text, output_field='clean_text')
nlp = spacy.load('en_core_web_sm')
string = 'Hello my name is Emma'
parse = textParser.process_text(string, mode='parse', sent_tokenizer=None, spacy_nlp = nlp)
print("Parsed version of: Hello my name is Emma")
print(censorNouns.censor_nouns(parse))
#displacy.serve(nlp(string), style="dep")
onbase = 'This ticket is for creation of Dons OnBase account. There is a separate ticket that Les has for creation of the Network ID account and provisioning of it.  Please follow up with Gayle Bauer with any account information.  Dons Network ID is: dhasseltine,1968'
parse_ticket = textParser.process_text(onbase, mode='parse', sent_tokenizer=None, spacy_nlp = nlp)
displacy.serve(nlp(onbase), style="dep")
print(onbase)
parsed_list = censorNouns.censor_nouns(parse_ticket)
df = pd.DataFrame(parsed_list)
print(df.head())
#it's very hard to understand these but there does seem to be 2 NN in my simple statement
