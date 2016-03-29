import string
class Comp(object):
    def __init__(self):
        self.wordnum={}
        self.dirctory={}
    def creatWord(self):
        fileopen=open('word.txt','r')
        line=fileopen.readline()
        while line:
            flag=0
            snum=''
            word=''
            for i in range(len(line)):
                if line[i]=='\t':
                    flag=flag+1
                    continue
                elif flag==2:
                    break
                elif flag==0:
                    word=word+line[i]
                elif flag==1:
                    snum=snum+line[i]
            num=int(snum)
            self.wordnum.update({word:num})
            #print num
            #print word
            line=fileopen.readline()
        fileopen.close()
    def update(self,category,matrx):
        tfidf={}
        if self.dirctory.has_key(category):
            tfidf=self.dirctory[category]
        else:
            self.dirctory.update({category:{}})
            tfidf=self.dirctory[category]
        words=self.wordnum.keys()
        for word in words:
            num=self.wordnum[word]
            val=matrx[num]
            if val==0:
                continue
            if tfidf.has_key(word):
                tfidf[word]=tfidf[word]+val
            else:
                tfidf.update({word:val})
    def writeFile(self):
        cates=self.dirctory.keys()
        total={}# first 1000
        for cate in cates:
            filename=cate+'.txt'
            tfidf=self.dirctory[cate]
            fileobj=open(filename,'w')
            sort_tfidf=sorted(tfidf.iteritems(),
            key=lambda d:d[1],reverse=True)
            i=0
            for dirc in sort_tfidf:
                word=dirc[0]
                val=dirc[1]
                fileobj.write(word+'\t'+str(val)+'\n')
                if i<1000:
                    if total.has_key(word):
                        if total[word]<val:
                            total[word]=val
                    else:
                        total.update({word:val})
                i=i+1
            fileobj.close()
        sort_total=sorted(total.iteritems(),
        key=lambda d:d[1],reverse=True)
        filetotal=open("total.txt","w")
        i=0
        for dirc in sort_total:
            if i==1000:
                break
            i=i+1
            filetotal.write(dirc[0]+'\t'+str(dirc[1])+'\n')
        filetotal.close()

