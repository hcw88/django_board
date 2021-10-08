from googletrans import Translator
 
 
text1 = "안녕하세요. 저는 학생입니다."
 
translator = Translator() 
trans1 = translator.translate(text1, src='ko', dest='ja')

print("English to Japanese: ", trans1.text)
