# public
&lt;-:->
针对斯拉夫部分字母和英语字母相似的特性，当用户注册或其他字母输入情况未限制输入为26个字母时，可通过斯拉夫字母来对相似字母进行替换，在某些场景可以起到迷惑性的效果！
小程序未考虑字符替换排列组合的情况，仅生成了1个字符替换、2个、。。。。全部替换的情况，替换后返回的列表中，new_word[0]未原始字符串，其余的为替换后去重的字符串。
