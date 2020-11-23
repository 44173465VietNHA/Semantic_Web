from pyvi import ViTokenizer, ViPosTagger
import os
import pandas as pd
import csv

# run in sematic_web (project root dir)

dir = "CrawlData/craw/historyRelic/"

def sent2postagging(sent):
 doc = ViTokenizer.tokenize(sent)
 sent = ViPosTagger.postagging(doc)
 result = ''
 for i in range(len(sent[0])):
  result = result + sent[0][i] + " " + sent[1][i] + "\n"
 return result

def sent2postagging_formatArray(sent):
 doc = ViTokenizer.tokenize(sent)
 sent = ViPosTagger.postagging(doc)
 result = []
 for i in range(len(sent[0])):
  result.append([sent[0][i],sent[1][i]])
 return result

# example = 'TRƯỜNG LÀ ĐẠI HỌC TOP ĐẦU CỦA CẢ NƯỚC, được nhiều trường đại học quốc tế công nhận chương trình đào tạo và thiết lập quan hệ đào tạo, trong đó có Đại học'
# print(sent2postagging(example))

path = ""

# for filename in os.listdir(dir):
#  if filename.endswith(".txt"):
#   path = os.path.join(dir, filename)
#   f = open(path, 'r', encoding = 'utf-8')
#   text = f.read()
#   result = sent2postagging_formatArray(text)
#   pd.DataFrame(result).to_csv('Tagging_CRF/historyRelic/' + filename.split('.')[0]+'.csv', header = False, index = False, encoding='utf-8')

for filename in os.listdir(dir):
 if filename.endswith(".txt"):
  path = os.path.join(dir, filename)
  f = open(path, 'r', encoding = 'utf-8')
  text = f.read()
  fresult = open('Tagging_CRF/historyRelic/'+filename, 'wb')
  fresult.write(sent2postagging(text).encode('utf-8'))
  fresult.close()
  f.close()
