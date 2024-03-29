#If you want to remove leading and ending spaces, use str.strip():

sentence = ' hello  apple'
sentence.strip()
# 'hello  apple'

#If you want to remove all spaces, use str.replace():

sentence = ' hello  apple'
sentence.replace(" ", "")
# 'helloapple'

#If you want to remove duplicated spaces, use str.split():

sentence = ' hello  apple'
" ".join(sentence.split())
# 'hello apple'
