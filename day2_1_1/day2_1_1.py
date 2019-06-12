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

integer_encoded = []
for token_sentence in token_sentences:
  integer_encoded.append([char_to_int[char] for char in token_sentence])  
  
print(integer_encoded)

from tensorflow.keras import preprocessing
# 전시간에 배운 preprocessing의 Tokenizer 함수를 이용하여 Instance를 만든다.
# fit_on_texts 함수에 Token하고자 하는 copus 를 넣는다.
# 문장을 index 처리 한다.

tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(samples) 
sequence = tokenizer.texts_to_sequences(samples) 

word_index = tokenizer.word_index

print("token_sentences : %s " %sequence)
print("word_list : %s" %word_index)