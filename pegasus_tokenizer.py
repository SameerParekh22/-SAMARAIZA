# -*- coding: utf-8 -*-
"""Pegasus_tokenizer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xWaLHFwEsmMTNb7-stDw11ft1juVvWab
"""

!pip install torch==1.8.2+cu111 torchvision==0.9.2+cu111 torchaudio===0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html

!pip install transformers

pip install sentencepiece

from transformers import PegasusForConditionalGeneration, PegasusTokenizer

tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")

model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

text = "Today videos organisation freed online shopping Government and private sector organisations Catering and Tourism industry or other Institutions offer Customer services are concerned about their customers and ask for feedback every single time we use the services consider the fact that these companies may be receiving enormous amount of he is a fact every single day and it will become quite tedious for the management in analyse each of those were the technology today we have reached the election was they who was the task of human beings and the field which makes this happen is machine learning the Machines have KEM Re KEM understand human language is used in National Knowledge Commission today uses of being done in the field of text analytics and ones application of text analytics and foetus is a which helps in summarising and not with the Axes of environment can be done in an algorithm to ready for the subtext but keeping his what is the meaning of giving a great insight in the original text if you're interested and Data Analytics and you will find turning about natural language processing very useful Passion Pro visor elements live"

tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

summary = model.generate(**tokens)

check = tokenizer.decode(summary[0])
# print(len(check),len(text))
print(check)