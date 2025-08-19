from hangul_romanize import Transliter
from hangul_romanize.rule import academic
import re
from transformers import AutoTokenizer, MarianMTModel

# 3 possibilities:
# 1) fully korean line
# 2) fully english line
# 3) mixed english and korean

# huggingface model for korean to english translation
src = "ko"
trg = "en"
model_name = f"Helsinki-NLP/opus-mt-ko-en"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# uses academic for romanization rules because korean rule N/A
transliter = Transliter(academic)

def has_english(text):
    # check whether the line contains any english characters. if not, it is fully korean
    return bool(re.search(r'[A-Za-z]+', text))

def has_korean(text):
    # check whether the line contains any korean characters. if not, it is fully english
    return bool(re.search(r'[가-힣]+', text))

def get_english(text):
    # retrieve all english parts from a mixed line
    return re.findall(r'[A-Za-z\s]+', text)

def get_korean(text):
    # retrieve all korean parts from a mixed line
    return re.findall(r'[가-힣\s]+', text)

def romanize_mixed_line(line, transliter):
    korean_parts = get_korean(line)
    for korean in korean_parts:
        romanized = transliter.translit(korean)
        line = line.replace(korean, romanized, 1)
    return line

def translate(text):
        batch = tokenizer([text], return_tensors="pt")
        generated_ids = model.generate(**batch)
        translation = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return translation

def translate_korean_segments(line):
    korean_parts = get_korean(line)
    korean_phrase = ' '.join(korean_parts)
    translated = translate(korean_phrase)
    line = re.sub(r'([가-힣\s]+)', translated, line, 1)
    return line

# open file and read lines
with open('lyrics.txt', 'r', encoding='utf-8') as infile, \
     open('example.py/output.txt', 'w', encoding='utf-8') as outfile:
    lines = infile.readlines()

    for line in lines:
        line = line.strip()
        if not has_english(line):
            # fully korean line
            outfile.write(f"Korean: {line}\n")
            translation = translate(line)
            outfile.write(f"Romanized: {transliter.translit(line)}\n")
            outfile.write(f"English: {translation.replace('.', '')}\n")
            outfile.write("-" * 90 + "\n")
        elif not has_korean(line):
            # fully english line
            outfile.write(f"English:, {line}\n")
            outfile.write("-" * 90 + "\n")
        else:
            # mixed korean + english line
            outfile.write(f"Korean + English: {line}\n")
            outfile.write(f"Romanized: {romanize_mixed_line(line, transliter)}\n")
            outfile.write(f"English: {translate_korean_segments(line).replace('.', ' ')}\n")
            outfile.write("-" * 90 + "\n")