# 全文索引
# 基于倒排索引，维护词项到包含该词项的文档列表的映射

# 打分算法TF-IDF和BM25，都是基于词频（TF）

# Term Frequency(TF)
# 一个单词在文档中出现的频率（越多越重要）

# Inverse Document Frequency(IDF)
# 表示一个词对整个文集的重要性（越少越重要）

# BM25对TF-IDF进行了优化，使用了饱和函数，避免在极端情况下IDF过于极端，k1和b

# 大模型应用:RAG
