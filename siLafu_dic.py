#!/user/bin/python3
# _*_coding:utf-8 _*_

''' 利用斯拉夫字母和英语字母外形相似的特性，替换相似的英语字母
    斯拉夫字母：
        大写：АВЕКМНОРСТУХЫЬ
        小写：авекмнорстухыь
    英语字母：aBekMHopcTyXblb
    写一个函数：传入任意单词，替换为斯拉夫字母的单词
'''
class Word2Slf:
    def __init__(self,word):
        self.name = "斯拉夫字母转换"
        self.slf_dic = {'bl': 'ы', 'bI': 'Ы', 'A': 'А', 'a': 'а', 'B': 'В', 'b': 'ь', 'E': 'Е', 'e': 'е', 'K': 'К', 'k': 'к','M': 'М', 'm': 'м',
                        'H': 'Н', 'O': 'О', 'o': 'о','P': 'Р', 'p': 'р', 'C': 'С', 'c': 'с', 'T': 'Т', 'X': 'Х', 'x': 'х', 'Y': 'У', 'y': 'у'}

        self.word = word
        self.word1 = word
        self.word2 = word
        self.new_word = []                  #self.new_word[0] 为原始字符串，self.new_word 为去重后的结果
        # self.slf()
        # self.check()                        #检查self.new_word 是否存在斯拉夫字母，不存在返回false

    def toSlf1(self,char):
        self.word1 = self.word1.replace(char,self.slf_dic[char])
        return self.word1
    
    def toSlf2(self,char):
        return self.word2.replace(char,self.slf_dic[char])

    def slf(self):
        for i in self.slf_dic:
            if i in self.word1:
                self.new_word.append(self.toSlf1(i))
            if i in self.word2:
                self.new_word.append(self.toSlf2(i))

        self.new_word.append(self.word1)
        new_word = list(set(self.new_word))
        new_word.insert(0, self.word)
        self.new_word = new_word
        return self.new_word

    def check(self):                                                #检查self.new_word 是否存在斯拉夫字母，不存在返回false
        if len(self.new_word) >= 2:
            if self.new_word[0] == self.new_word[1]:
                self.new_word = self.new_word[0]
                return False
            else:
                return True
        else:
            return False
def main():
    slf = Word2Slf(input("请输入一个字符串："))
    print(slf.slf(),slf.check(),5)

if __name__ == '__main__':
    main()

