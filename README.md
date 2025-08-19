# Korean-English-Lyrics-Translator

This project takes song lyrics originally written in Korean and outputs:  
ORIGINAL TEXT: Original Korean, English, and Korean + English song lyrics  
TRANSLATION: Korean -> English  
TRANSLITERATION (ROMANIZATION): Use of Latin alphabet to represent Korean words  
  
This translator is designed to handle phrases and sentences in Korean, English, and a mix of both languages.  
It utilizes line-by-line parsing to output a translation and romanization for each line.  
  
## Features
Romanization through ('hangul-romanize')  
Machine Translation with [Helsinki-NLP/opus-mt-ko-en](https://huggingface.co/Helsinki-NLP/opus-mt-ko-en)   
Regex text processing  

## Installation + Usage
1. Clone the repo  
```git clone https://github.com/tiya-kumar/Korean-English-Lyrics-Translator```  
2. Install Packages  
```pip install -r requirements.txt``` 
3. Input lyrics into lyrics.txt file  
4. Run Script  
```python main.py lyrics.txt```  
  

  
## Optimizations
Batch Translation: The translator struggled with sentences that any occurances of English. Utilizing batch translation to batch Korean phrases and rejoin with the full phrase including the English term(s), improved the performance of the model.  
  
Post-process Cleaning: Removing excess periods from Hugging Face translations.  

## Future Improvements
-Improve batch translation accuracy by utilizing larger batches (entire verse or song) to improve accuracy given context.    
-Support Korean songs with languages other than Korean and English (Spanish, French, Japanese, etc.)  

## License
This project is licensed under the terms of the MIT license. See ```license.txt``` for details.
