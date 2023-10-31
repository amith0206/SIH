from googletrans import Translator
import os,glob


# Create a Translator object
translator = Translator()

dir_name='E://SIH//data'
file_paths=glob.glob(os.path.join(dir_name,"*"))
target_lang='en'


def translating():
    #fetch from database.
    for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()          #read file contents
                translated_text = translator.translate(text, dest=target_lang)
                print(translated_text.text+'\n')
                #cleaned=text_cleaning(translated_text.text)
                
                
translating()




