
import os
import docx2txt

with open('Phrases.txt', 'r', encoding='utf-8') as f:
    text = f.read()

sentences = {}
sentence_id = 1

for line in text.split('.'):
    if ')' in line:
        sentence = line.split(')')[1]
        clean_sentence = f"{sentence.strip()}"
        if clean_sentence:
            # Сохраняем фразу и её уникальный номер в словаре sentences
            sentences[clean_sentence] = sentence_id
            sentence_id += 1

# Проходим по всем файлам .docx в папке files
for filename in os.listdir('files'):
    if filename.endswith('.docx'):
        doc_path = os.path.join('files', filename)

        # Получаем текст файла .docx с помощью библиотеки docx2txt
        full_text = docx2txt.process(doc_path)

        # Проходим по всем фразам и проверяем, есть ли они в файле .docx
        for sentence, sentence_id in sentences.items():
            if sentence in full_text:
                print(f"'{sentence}', (фраза #{sentence_id}) найдена в файле {filename}.")

