samples = ["창욱은 축구를 좋아한다",
          "중현은 축구를 싫어한다",
          "창욱은 도서관을 좋아한다",
          "중현은 도서관을 싫어한다",
          "창욱은 공부를 좋아한다",
          "중현은 공부를 싫어한다",
          "창욱은 축구를 좋아한다 중현은 축구를 싫어한다",
          "창욱은 도서관을 좋아한다 중현은 도서관을 싫어한다",
          "창욱은 공부를 좋아한다 중현은 공부를 싫어한다"]

token_sentences = []

for sentence in samples:
  token_sentences.append(sentence.split())

print("token_sentences : %s " %token_sentences)
word_list = " ".join(samples).split()
word_list = list(set(word_list))

print("word_list : %s" %word_list)

char_to_int = dict((c, i) for i, c in enumerate(word_list))
char_to_int