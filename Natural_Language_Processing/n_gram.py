def n_gram(stext, n):
  unigram = stext.split()
  ngram = []
  for i in range(len(unigram)-n+1):
    gram = ' '.join(unigram[i : i+n])
    ngram.append(gram)
  return ngram

stext = "Colaboratory(또는 줄여서 'Colab')를 사용하면 브라우저에서 Python을 작성하고 실행할 수 있습니다."

ngram = n_gram(stext, 4)
print(ngram)
