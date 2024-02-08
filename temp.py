# sinhalaTextToEnglishTranslator = {
#     'අ': 'a', 'ආ': 'aa', 'ඉ': 'i', 'ඊ': 'ii', 'උ': 'u', 'ඌ': 'uu', 'එ': 'e', 'ඔ': 'o',
#     'ා': 'aa', 'ි': 'i', 'ී': 'ii', 'ු': 'u', 'ූ': 'uu', 'ෙ': 'e', 'ේ': 'e', 'ො': 'o', 'ෝ': 'oo',
#     'ෞ': 'oo', 'ෟ': 'ai', 'ං': 'ng', 'ඃ': 'n', 'ඈ': 'ii', 'ඉය': 'ii', 'ඊය': 'uu', 'උය': 'uu', 'ඌය': 'uu',
#     'අය': 'ai', 'එය': 'ai', 'ඉයි': 'yii', 'ඉයු': 'yiyu', 'ඉයෙ': 'iyye', 'ඉයේ': 'iyye', 'ඉයෝ': 'iyyo', 'ඉයො': 'iyyo',
#     'ඉයෛ': 'iyya', 'ඉයා': 'iyya', 'ඊයි': 'eyyi', 'ඊයු': 'eyyyu', 'ඊයෙ': 'eyyyye', 'ඊයේ': 'eyyyye', 'ඊයෝ': 'eyyyo',
#     'ඊයො': 'eyyyo', 'ඊයෛ': 'eyyya', 'ඊයා': 'eyyya', 'උයි': 'uyi', 'උයු': 'uyyu', 'උයෙ': 'uyye', 'උයේ': 'uyye', 'උයෝ': 'uyyo',
#     'උයො': 'uyyo', 'උයෛ': 'uyya', 'උයා': 'uyya', 'ඌයි': 'oyi', 'ඌයු': 'oyyu', 'ඌයෙ': 'oyyye', 'ඌයේ': 'oyyye', 'ඌයෝ': 'oyyyo',
#     'ඌයො': 'oyyyo', 'ඌයෛ': 'oyya', 'ඌයා': 'oyya', 'එළහ': 'eylh', 'එළ': 'eyl', 'ඉළහ': 'ilh', 'ඉළ': 'il', 'ඊළහ': 'eylh', 'ඊළ': 'eyl',
#     'උළහ': 'ulh', 'උළ': 'ul', 'ඌළහ': 'olh', 'ඌළ': 'ol', 'ක': 'k', 'ඛ': 'ch', 'ග': 'g', 'ඝ': 'gh', 'ඞ': 'ng', 'ච': 'ch', 'ඡ': 'th',
#     'ජ': 'j', 'ඣ': 'q', 'ඤ': 'kh', 'ඥ': 'th', 'ඦ': 'ph', 'ට': 't', 'ඨ': 'th', 'ඩ': 'd', 'ඪ': 'th', 'ණ': 'n', 'ඬ': 'th', 'ත': 'th',
#     'ථ': 'th', 'ද': 'd', 'ධ': 'th', 'න': 'n', 'ප': 'p', 'ඵ': 'ph', 'බ': 'b', 'ම': 'm', 'ය': 'y', 'ර': 'r', 'ල': 'l', 'ව': 'v',
#     'ස': 'sh', 'හ': 'h', 'ළ': 'rh', 'ෆ': 'f', '්': '', 'යි': 'yi', 'යු': 'yu', 'යෙ': 'ye', 'යේ': 'ye', 'යෝ': 'yo', 'යො': 'yo',
#     'යෛ': 'ya', 'යා': 'ya', 'ය': 'yi', 'යා': 'ya', 'අයි': 'aiyi', 'අයු': 'aiyu', 'අයෙ': 'aiye', 'අයේ': 'aiye', 'අයෝ': 'aiyo',
#     'අයො': 'aiyo', 'අයෛ': 'aiya', 'අයා': 'aiya', 'අය': 'aiyi', 'අයා': 'aiya', 'එයි': 'eyi', 'එයු': 'eyyu', 'එයෙ': 'eyye',
#     'එයේ': 'eyye', 'එයෝ': 'eyyo', 'එයො': 'eyyo', 'එයෛ': 'eyya', 'එයා': 'eyya', 'එය': 'eyyi', 'එයා': 'eyya', 'ඉයි': 'iyi',
#     'ඉයු': 'iyyu', 'ඉයෙ': 'iyyye', 'ඉයේ': 'iyyye', 'ඉයෝ': 'iyyo', 'ඉයො': 'iyyo', 'ඉයෛ': 'iyya', 'ඉයා': 'iyya'
# }


# def translate_word_to_latin(sinhala_word):
#     translated_word = ""
#     for char in sinhala_word:
#         if char in sinhalaTextToEnglishTranslator:
#             translated_word += sinhalaTextToEnglishTranslator[char]
#     return translated_word

# def translate_sentence_to_latin(sinhala_sentence):
#     sinhala_words = sinhala_sentence.split(' ')
#     translated_sentence = ""
#     for word in sinhala_words:
#         translated_word = translate_word_to_latin(word)
#         translated_sentence += translated_word + " "
#     return translated_sentence.strip()

# # Example usage:
# sinhala_input = 'අයුම්කරුවන්ගේ පරිශීලක උපදෙස් තුන්වන අයුරු'
# latin_output = translate_sentence_to_latin(sinhala_input)
# print(latin_output)

#kkep it if it wasnt there
sinhala_unicode_mapping_1 = {
    'අ': 'a', 'ආ': 'aa', 'ඇ': 'A', 'ඈ': 'Aa', 'ඉ': 'i', 'ඊ': 'ii', 'උ': 'u', 'ඌ': 'uu', 'ඍ': 'Ru',
    'ඎ': 'Ru', 'එ': 'e', 'ඒ': 'ee', 'ඓ': 'ai', 'ඔ': 'o', 'ඕ': 'oo', 'ඖ': 'au',
    'ක': 'ka', 'කා': 'kaa', 'කැ': 'kA', 'කෑ': 'kAa', 'කි': 'ki', 'කී': 'kii', 'කු': 'ku', 'කූ': 'kuu', 'කෘ': 'kru',
    'කෙ': 'ke', 'කේ': 'kee', 'කෛ': 'kai', 'කො': 'ko', 'කෝ': 'koo', 'කෞ': 'kau', 'කෲ': 'kruu', 'ක්‍ය': 'kya', 'ක්‍ර': 'kra',
    'ග': 'ga', 'ගා': 'gaa', 'ගැ': 'gA', 'ගෑ': 'gAa', 'ගි': 'gi', 'ගී': 'gii', 'ගු': 'gu', 'ගූ': 'guu', 'ගෘ': 'guru',
    'ගෙ': 'ge', 'ගේ': 'gee', 'ගෛ': 'gai', 'ගො': 'go', 'ගෝ': 'goo', 'ගෞ': 'gau', 'ග්‍ය': 'gya', 'ග්‍ර': 'gra',
    'ච': 'cha', 'චා': 'chaa', 'චැ': 'chA', 'චෑ': 'chAa', 'චි': 'chi', 'චී': 'chii', 'චු': 'chu', 'චූ': 'chuu',
    'චෙ': 'che', 'චේ': 'chee', 'චෛ': 'chai', 'චො': 'cho', 'චෝ': 'choo', 'චෞ': 'chau', 'ච්‍ය': 'chya', 'ච්‍ර': 'chra',
    'ජ': 'ja', 'ජා': 'jaa', 'ජැ': 'jA', 'ජෑ': 'jAa', 'ජි': 'ji', 'ජී': 'jii', 'ජු': 'ju', 'ජූ': 'juu', 'කෘ': 'jru',
    'ජෙ': 'je', 'ජේ': 'jee', 'ජෛ': 'jai', 'ජො': 'jo', 'ජෝ': 'joo', 'ජෞ': 'jau', 'ජ්‍ය': 'jya', 'ජ්‍ර': 'jra',
    'ට': 'ta', 'ටා': 'taa', 'ටැ': 'tA', 'ටෑ': 'tAa', 'ටි': 'ti', 'ටී': 'tii', 'ටු': 'tu', 'ටූ': 'tuu', 'කෘ': 'tru',
    'ටෙ': 'te', 'ටේ': 'tee', 'ටෛ': 'tai', 'ටො': 'to', 'ටෝ': 'too', 'ටෞ': 'tau', 'ටඃ': 'taH', 'ට්‍ය': 'tya', 'ට්‍ර': 'tra',
    'ඩ': 'da', 'කා': 'daa', 'ඩැ': 'dA', 'ඩෑ': 'dAa', 'ඩි': 'di', 'ඩී': 'dii', 'ඩු': 'du', 'ඩූ': 'duu', 'ඩෘ': 'dru',
    'ඩෙ': 'de', 'ඩේ': 'dee', 'ඩෛ': 'dai', 'ඩො': 'do', 'ඩෝ': 'doo', 'ඩෞ': 'dau', 'ඩ්‍ය': 'dya', 'ඩ්‍ර': 'dra',
    'න': 'na', 'නා': 'naa', 'නැ': 'nA', 'නෑ': 'nAa', 'නි': 'ni', 'නී': 'nii', 'නු': 'nu', 'නූ': 'nuu', 'නෘ': 'nru',
    'නෙ': 'ne', 'නේ': 'nee', 'නෛ': 'nai', 'නො': 'no', 'නෝ': 'noo', 'නෞ': 'nau', 'න්‍ය': 'nya', 'න්‍ර': 'nra',
    'ප': 'pa', 'පා': 'paa', 'පැ': 'pA', 'පෑ': 'pAa', 'පි': 'pi', 'පී': 'pii', 'පු': 'pu', 'පූ': 'puu', 'පෘ': 'pru',
    'පෙ': 'pe', 'පේ': 'pee', 'පෛ': 'pai', 'පො': 'po', 'පෝ': 'poo', 'පෞ': 'pau', 'ප්‍ය': 'pya', 'ප්‍ර': 'pra',
    'බ': 'ba', 'බා': 'baa', 'බැ': 'bA', 'බෑ': 'bAa', 'බි': 'bi', 'බී': 'bii', 'බු': 'bu', 'බූ': 'buu', 'බෘ': 'bru',
    'බෙ': 'be', 'බේ': 'bee', 'බෛ': 'bai', 'බො': 'bo', 'බෝ': 'boo', 'බෞ': 'bau', 'බ්‍ය': 'bya', 'බ්‍ර': 'bra',
    'භ': 'bha', 'භා': 'bhaa', 'භැ': 'bhA', 'භෑ': 'bhAa', 'භි': 'bhi', 'භී': 'bhii', 'භු': 'bhu', 'භූ': 'bhuu',
    'භෘ': 'bhru', 'භෙ': 'bhe', 'භේ': 'bhee', 'භෛ': 'bhai', 'භො': 'bho', 'භෝ': 'bhoo', 'භෞ': 'bhau',
    'භ්‍ය': 'bhya', 'භ්‍ර': 'bhra', 'ම': 'm',
    'ස': 'sa', 'සා': 'saa', 'සැ': 'sA', 'සෑ': 'sAa', 'සි': 'si', 'සී': 'sii', 'සු': 'su', 'සූ': 'suu', 'සෘ': 'sru',
    'සෙ': 'se', 'සේ': 'see', 'සෛ': 'sai', 'සො': 'so', 'සෝ': 'soo', 'සෞ': 'sau', 'ස්‍ය': 'sya', 'ස්‍ර': 'sra',
    'හ': 'ha', 'හා': 'haa', 'හැ': 'hA', 'හෑ': 'hAa', 'හි': 'hi', 'හී': 'hii', 'හු': 'hu', 'හූ': 'huu', 'හෘ': 'hru',
    'හෙ': 'he', 'හේ': 'hee', 'හෛ': 'hai', 'හො': 'ho', 'හෝ': 'hoo', 'හෞ': 'hau', 'හ්‍ය': 'hya', 'හ්‍ර': 'hra',
    'යා': 'yaa', 'යැ': 'yA', 'යෑ': 'yAa', 'යි': 'yi', 'යී': 'yii', 'යු': 'yu', 'යූ': 'yuu', 'යෘ': 'yru', 'යෙ': 'ye',
    'යේ': 'yee', 'යෛ': 'yai', 'යො': 'yo', 'යෝ': 'yoo', 'යෞ': 'yau',
    'රා': 'raa', 'රැ': 'rA', 'රෑ': 'rAa', 'රි': 'ri', 'රී': 'rii', 'රු': 'ru', 'රූ': 'ruu', 'රෘ': 'rru', 'රෙ': 're',
    'රේ': 'ree', 'රෛ': 'rai', 'රො': 'ro', 'රෝ': 'roo', 'රෞ': 'rau',
    # 'ා': 'aa', 'ැ': 'A', 'ෑ': 'Aa', 'ි': 'i', 'ී': 'ii', 'ු': 'u', 'ූ': 'uu', 'ෘ': 'ru', 'ෙ': 'e', 'ේ': 'ee', 'ෛ': 'ai',
    # 'ො': 'o', 'ෝ': 'oo', 'ෞ': 'au',
    # '්‍ය': 'ya', '්‍ර': 'ra'
}

sinhala_unicode_mapping_2 = {
    'අ': 'a','ඉ': 'i', 'ඊ': 'ii', 'උ': 'u', 'ඍ': 'Ru','එ': 'e', 'ඔ': 'o', 'ක': 'k', 'ග': 'g', 'ච': 'ch', 
    'ජ': 'j','ට': 't','ඩ': 'd', 'ඩෙ': 'd', 'න': 'n','ප': 'p', 'බ': 'b', 
    'භ': 'bh', 'ස': 's', 'හ': 'h','ය': 'y','ර': 'r', 'ම': 'm'
    # 'ා': 'aa', 'ැ': 'A', 'ෑ': 'Aa', 'ි': 'i', 'ී': 'ii', 'ු': 'u', 'ූ': 'uu', 'ෘ': 'ru', 'ෙ': 'e', 'ේ': 'ee', 'ෛ': 'ai',
    # 'ො': 'o', 'ෝ': 'oo', 'ෞ': 'au',
    # '්‍ය': 'ya', '්‍ර': 'ra'
}

sinhala_unicode_mapping_3 = {
    'ා': 'aa', 'ැ': 'A', 'ෑ': 'Aa', 'ි': 'i', 'ී': 'ii', 'ු': 'u', 'ූ': 'uu', 'ෘ': 'ru', 'ෙ': 'e', 'ේ': 'ee', 'ෛ': 'ai',
    'ො': 'o', 'ෝ': 'oo', 'ෞ': 'au',
    '්‍ය': 'ya', '්‍ර': 'ra'
}
def to_sinhala_unicode(input_text):
    temp_array = []

    for i, char in enumerate(input_text):
        print(char)
        temp_char_1 = sinhala_unicode_mapping_2.get(char)
        temp_char_2 = sinhala_unicode_mapping_3.get(char)

        if temp_char_1 is not None:
            temp_array.append(temp_char_1)

        elif temp_char_2 is not None:
            temp_array.append(temp_char_2)

        if char == " " or i == len(input_text) - 1:
            temp_array.append("a")
        if char == " ":
            temp_array.append(" ")

    print(temp_array)

# Example usage
input_text = "ඔබ කැමති නම් මට කියන්න"
to_sinhala_unicode(input_text)


