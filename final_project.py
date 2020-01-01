#coding=gbk
'''
该程序可提取文本人物关系
作者：岑道前
'''
import codecs
import jieba.posseg as pseg
import jieba
import csv

names = {}
relationships = {}
lineNames = []

jieba.load_userdict("F:\person.txt")
with codecs.open("F:\lm.txt", 'r') as f:
    for line in f.readlines():
        poss = pseg.cut(line)
        lineNames.append([])
        for w in poss:
            if w.flag != 'nr' or len(w.word) < 2:
                continue  
            lineNames[-1].append(w.word)  
            if names.get(w.word) is None:  
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1

for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1


with codecs.open("F:\People_node.txt", "w", "utf8") as f:
    f.write("ID Label Weight\r\n")
    for name, times in names.items():
        if times > 10:
            f.write(name + " " + name + " " + str(times) + "\r\n")



with codecs.open("F:\People_edge.txt", "w", "utf8") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 10:
                f.write(name + " " + v + " " + str(w) + "\r\n")

with open('F:\People_node.csv', 'w+',newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
   
    with open('F:\People_node.txt', 'r',encoding='utf-8') as filein:
        for line in filein:
            line_list = line.strip('\n').split('\t')
            spamwriter.writerow(line_list)

with open('F:\People_edge.csv', 'w+',newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
   
    with open('F:\People_edge.txt', 'r',encoding='utf-8') as filein:
        for line in filein:
            line_list = line.strip('\n').split('\t')
            spamwriter.writerow(line_list)
