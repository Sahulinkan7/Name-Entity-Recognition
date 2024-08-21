from ner_src.exception import NerException
import os,sys 
from ner_src.logger import logging

try:
    print(9/0)
except Exception as e:
    print(NerException(e,sys))
    logging.info(NerException(e,sys))