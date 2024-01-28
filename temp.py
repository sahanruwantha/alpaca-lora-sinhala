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


sinhala_to_english = {
    'අ': 'a', 'ආ': 'aa', 'ඇ': 'A', 'ඈ': 'Aa', 'ඉ': 'i', 'ඊ': 'ii', 'උ': 'u', 'ඌ': 'uu', 'ඍ': 'R',
    'ඎ': 'Ru', 'එ': 'e', 'ඒ': 'ee', 'ඓ': 'ai', 'ඔ': 'o', 'ඕ': 'oo', 'ඖ': 'au',
    'ක': 'ka', 'ක්': 'k', 'කා': 'kaa', 'කැ': 'kA', 'කෑ': 'kAa','කි': 'ki', 'කී': 'kii', 'කු': 'ku', 'කූ': 'kuu', 'කෘ': 'kru', 'කෲ': 'kruu', 'කෙ': 'ke','කේ': 'kee', 'කෛ': 'kai', 'කො': 'ko', 'කෝ': 'koo', 'කෞ': 'kau', 'කඃ': 'kaH', 'කං': 'kax','කඞ': 'kaX', 'ක්‍ය': 'kya', 'ක්‍ර': 'kra',
    'ග': 'ga', 'ග්': 'g', 'ගා': 'gaa', 'ගැ': 'gA', 'ගෑ': 'gAa','ගි': 'gi', 'ගී': 'gii', 'ගු': 'gu', 'ගූ': 'guu', '': 'gru', 'කෲ': 'gruu', 'කෙ': 'ge','කේ': 'gee', 'කෛ': 'gai', 'කො': 'go', 'කෝ': 'goo', 'කෞ': 'gau', 'කඃ': 'gaH', 'කං': 'gax','කඞ': 'gaX', 'ක්‍ය': 'gya', 'ක්‍ර': 'gra',
    'ච': 'cha', 'ක්': 'ch', 'කා': 'chaa', 'කැ': 'chA', 'කෑ': 'chAa','කි': 'chi', 'කී': 'chii', 'කු': 'chu', 'කූ': 'chuu', 'කෘ': 'chru', 'කෲ': 'chruu', 'කෙ': 'che','කේ': 'chee', 'කෛ': 'chai', 'කො': 'cho', 'කෝ': 'choo', 'කෞ': 'chau', 'කඃ': 'chaH', 'කං': 'chax','කඞ': 'chaX', 'ක්‍ය': 'chya', 'ක්‍ර': 'chra',
    'ජ': 'ja', 'ක්': 'j', 'කා': 'jaa', 'කැ': 'jA', 'කෑ': 'jAa','කි': 'ji', 'කී': 'jii', 'කු': 'ju', 'කූ': 'juu', 'කෘ': 'jru', 'කෲ': 'jruu', 'කෙ': 'je','කේ': 'jee', 'කෛ': 'jai', 'කො': 'jo', 'කෝ': 'joo', 'කෞ': 'jau', 'කඃ': 'jaH', 'කං': 'jax','කඞ': 'jaX', 'ක්‍ය': 'jya', 'ක්‍ර': 'jra',
    'ට': 'ta', 'ක්': 't', 'කා': 'taa', 'කැ': 'tA', 'කෑ': 'tAa','කි': 'ti', 'කී': 'tii', 'කු': 'tu', 'කූ': 'tuu', 'කෘ': 'tru', 'කෲ': 'truu', 'කෙ': 'te','කේ': 'tee', 'කෛ': 'tai', 'කො': 'to', 'කෝ': 'too', 'කෞ': 'tau', 'කඃ': 'taH', 'කං': 'tax','කඞ': 'taX', 'ක්‍ය': 'tya', 'ක්‍ර': 'tra',
    'ඩ': 'da', 'ක්': 'd', 'කා': 'daa', 'කැ': 'dA', 'කෑ': 'dAa','කි': 'di', 'කී': 'dii', 'කු': 'du', 'කූ': 'duu', 'කෘ': 'dru', 'කෲ': 'druu', 'කෙ': 'de','කේ': 'dee', 'කෛ': 'dai', 'කො': 'do', 'කෝ': 'doo', 'කෞ': 'dau', 'කඃ': 'daH', 'කං': 'dax','කඞ': 'daX', 'ක්‍ය': 'dya', 'ක්‍ර': 'dra',
    'ත': 'tha', 'ක්': 'th', 'කා': 'thaa', 'කැ': 'thA', 'කෑ': 'thAa','කි': 'thi', 'කී': 'thii', 'කු': 'thu', 'කූ': 'thuu', 'කෘ': 'thru', 'කෲ': 'thruu', 'කෙ': 'the','කේ': 'thee', 'කෛ': 'thai', 'කො': 'tho', 'කෝ': 'thoo', 'කෞ': 'thau', 'කඃ': 'thaH', 'කං': 'thax','කඞ': 'thaX', 'ක්‍ය': 'thya', 'ක්‍ර': 'thra',
    'ද': 'dha','ක්': 'dh', 'කා': 'dhaa', 'කැ': 'dhA', 'කෑ': 'dhAa','කි': 'dhi', 'කී': 'dhii', 'කු': 'dhu', 'කූ': 'dhuu', 'කෘ': 'dhru', 'කෲ': 'dhruu', 'කෙ': 'dhe','කේ': 'dhee', 'කෛ': 'dhai', 'කො': 'dho', 'කෝ': 'dhoo', 'කෞ': 'dhau', 'කඃ': 'dhaH', 'කං': 'dhax','කඞ': 'dhaX', 'ක්‍ය': 'dhya', 'ක්‍ර': 'dhra',
    'න': 'na', 'ක්': 'n', 'කා': 'naa', 'කැ': 'nA', 'කෑ': 'nAa','කි': 'ni', 'කී': 'nii', 'කු': 'nu', 'කූ': 'nuu', 'කෘ': 'nru', 'කෲ': 'nruu', 'කෙ': 'ne','කේ': 'nee', 'කෛ': 'nai', 'කො': 'no', 'කෝ': 'noo', 'කෞ': 'nau', 'කඃ': 'naH', 'කං': 'nax','කඞ': 'naX', 'ක්‍ය': 'nya', 'ක්‍ර': 'nra',
    'ණ': 'Na', 'ක්': 'N', 'කා': 'Naa', 'කැ': 'NA', 'කෑ': 'NAa','කි': 'Ni', 'කී': 'Nii', 'කු': 'Nu', 'කූ': 'Nuu', 'කෘ': 'Nru', 'කෲ': 'Nruu', 'කෙ': 'Ne','කේ': 'Nee', 'කෛ': 'Nai', 'කො': 'No', 'කෝ': 'Noo', 'කෞ': 'Nau', 'කඃ': 'NaH', 'කං': 'Nax','කඞ': 'NaX', 'ක්‍ය': 'Nya', 'ක්‍ර': 'Nra',
    'ප': 'pa', 'ක්': 'p', 'කා': 'paa', 'කැ': 'pA', 'කෑ': 'pAa','කි': 'pi', 'කී': 'pii', 'කු': 'pu', 'කූ': 'puu', 'කෘ': 'pru', 'කෲ': 'pruu', 'කෙ': 'pe','කේ': 'pee', 'කෛ': 'pai', 'කො': 'po', 'කෝ': 'poo', 'කෞ': 'pau', 'කඃ': 'paH', 'කං': 'pax','කඞ': 'paX', 'ක්‍ය': 'pya', 'ක්‍ර': 'pra',
    'බ': 'ba', 'ක්': 'b', 'කා': 'baa', 'කැ': 'bA', 'කෑ': 'bAa','කි': 'bi', 'කී': 'bii', 'කු': 'bu', 'කූ': 'buu', 'කෘ': 'bru', 'කෲ': 'bruu', 'කෙ': 'be','කේ': 'bee', 'කෛ': 'bai', 'කො': 'bo', 'කෝ': 'boo', 'කෞ': 'bau', 'කඃ': 'baH', 'කං': 'bax','කඞ': 'baX', 'ක්‍ය': 'bya', 'ක්‍ර': 'bra',
    'ම': 'ma', 'ක්': 'm', 'කා': 'maa', 'කැ': 'mA', 'කෑ': 'mAa','කි': 'mi', 'කී': 'mii', 'කු': 'mu', 'කූ': 'muu', 'කෘ': 'mru', 'කෲ': 'mruu', 'කෙ': 'me','කේ': 'mee', 'කෛ': 'mai', 'කො': 'mo', 'කෝ': 'moo', 'කෞ': 'mau', 'කඃ': 'maH', 'කං': 'max','කඞ': 'maX', 'ක්‍ය': 'mya', 'ක්‍ර': 'mra',
    'ය': 'ya', 'ක්': 'y', 'කා': 'yaa', 'කැ': 'yA', 'කෑ': 'yAa','කි': 'yi', 'කී': 'yii', 'කු': 'yu', 'කූ': 'yuu', 'කෘ': 'yru', 'කෲ': 'yruu', 'කෙ': 'ye','කේ': 'yee', 'කෛ': 'yai', 'කො': 'yo', 'කෝ': 'yoo', 'කෞ': 'yau', 'කඃ': 'yaH', 'කං': 'yax','කඞ': 'yaX', 'ක්‍ය': 'yya', 'ක්‍ර': 'yra',
    'ර': 'ra', 'ක්': 'r', 'කා': 'raa', 'කැ': 'rA', 'කෑ': 'rAa','කි': 'ri', 'කී': 'rii', 'කු': 'ru', 'කූ': 'ruu', 'කෘ': 'rru', 'කෲ': 'rruu', 'කෙ': 're','කේ': 'ree', 'කෛ': 'rai', 'කො': 'ro', 'කෝ': 'roo', 'කෞ': 'rau', 'කඃ': 'raH', 'කං': 'rax','කඞ': 'raX', 'ක්‍ය': 'rya', 'ක්‍ර': 'rra',
    'ල': 'la','ක්': 'l', 'කා': 'laa', 'කැ': 'lA', 'කෑ': 'lAa','කි': 'li', 'කී': 'lii', 'කු': 'lu', 'කූ': 'luu', 'කෘ': 'lru', 'කෲ': 'lruu', 'කෙ': 'le','කේ': 'lee', 'කෛ': 'lai', 'කො': 'lo', 'කෝ': 'loo', 'කෞ': 'lau', 'කඃ': 'laH', 'කං': 'lax','කඞ': 'laX', 'ක්‍ය': 'lya', 'ක්‍ර': 'lra',
    'ළ': 'La', 'ක්': 'L', 'කා': 'Laa', 'කැ': 'LA', 'කෑ': 'LAa','කි': 'Li', 'කී': 'Lii', 'කු': 'Lu', 'කූ': 'Luu', 'කෘ': 'Lru', 'කෲ': 'Lruu', 'කෙ': 'Le','කේ': 'Lee', 'කෛ': 'Lai', 'කො': 'Lo', 'කෝ': 'Loo', 'කෞ': 'Lau', 'කඃ': 'LaH', 'කං': 'Lax','කඞ': 'LaX', 'ක්‍ය': 'Lya', 'ක්‍ර': 'Lra',
    'ව': 'wa', 'ක්': 'w', 'කා': 'waa', 'කැ': 'wA', 'කෑ': 'wAa','කි': 'wi', 'කී': 'wii', 'කු': 'wu', 'කූ': 'wuu', 'කෘ': 'wru', 'කෲ': 'wruu', 'කෙ': 'we','කේ': 'wee', 'කෛ': 'wai', 'කො': 'wo', 'කෝ': 'woo', 'කෞ': 'wau', 'කඃ': 'waH', 'කං': 'wax','කඞ': 'waX', 'ක්‍ය': 'wya', 'ක්‍ර': 'wra',
    'ස': 'sa', 'ක්': 's', 'කා': 'saa', 'කැ': 'sA', 'කෑ': 'sAa','කි': 'si', 'කී': 'sii', 'කු': 'su', 'කූ': 'suu', 'කෘ': 'sru', 'කෲ': 'sruu', 'කෙ': 'se','කේ': 'see', 'කෛ': 'sai', 'කො': 'so', 'කෝ': 'soo', 'කෞ': 'sau', 'කඃ': 'saH', 'කං': 'sax','කඞ': 'saX', 'ක්‍ය': 'sya', 'ක්‍ර': 'sra',
    'ශ': 'sha', 'ක්': 'sh', 'කා': 'shaa', 'කැ': 'shA', 'කෑ': 'shAa','කි': 'shi', 'කී': 'shii', 'කු': 'shu', 'කූ': 'shuu', 'කෘ': 'shru', 'කෲ': 'shruu', 'කෙ': 'she','කේ': 'shee', 'කෛ': 'shai', 'කො': 'sho', 'කෝ': 'shoo', 'කෞ': 'shau', 'කඃ': 'shaH', 'කං': 'shax','කඞ': 'shaX', 'ක්‍ය': 'shya', 'ක්‍ර': 'shra',
    'ෂ': 'Sa', 'ක්': 'S', 'කා': 'Sa', 'කැ': 'SA', 'කෑ': 'SAa','කි': 'Si', 'කී': 'Sii', 'කු': 'Su', 'කූ': 'Suu', 'කෘ': 'Sru', 'කෲ': 'Sruu', 'කෙ': 'Se','කේ': 'See', 'කෛ': 'Sai', 'කො': 'So', 'කෝ': 'Soo', 'කෞ': 'Sau', 'කඃ': 'SaH', 'කං': 'Sax','කඞ': 'SaX', 'ක්‍ය': 'Sya', 'ක්‍ර': 'Sra',
    'හ': 'ha', 'ක්': 'h', 'කා': 'haa', 'කැ': 'hA', 'කෑ': 'hAa','කි': 'hi', 'කී': 'hii', 'කු': 'hu', 'කූ': 'huu', 'කෘ': 'hru', 'කෲ': 'hruu', 'කෙ': 'he','කේ': 'hee', 'කෛ': 'hai', 'කො': 'ho', 'කෝ': 'hoo', 'කෞ': 'hau', 'කඃ': 'haH', 'කං': 'hax','කඞ': 'haX', 'ක්‍ය': 'hya', 'ක්‍ර': 'hra',
    'ෆ': 'fa','ක්': 'f', 'කා': 'faa', 'කැ': 'fA', 'කෑ': 'fAa','කි': 'fi', 'කී': 'fii', 'කු': 'fu', 'කූ': 'fuu', 'කෘ': 'fru', 'කෲ': 'fruu', 'කෙ': 'fe','කේ': 'fee', 'කෛ': 'fai', 'කො': 'fo', 'කෝ': 'foo', 'කෞ': 'fau', 'කඃ': 'faH', 'කං': 'fax','කඞ': 'faX', 'ක්‍ය': 'fya', 'ක්‍ර': 'fra',
    'ඛ': 'kha', 'ක්': 'kh', 'කා': 'khaa', 'කැ': 'khA', 'කෑ': 'khAa','කි': 'khi', 'කී': 'khii', 'කු': 'khu', 'කූ': 'khuu', 'කෘ': 'khru', 'කෲ': 'khruu', 'කෙ': 'khe','කේ': 'khee', 'කෛ': 'khai', 'කො': 'kho', 'කෝ': 'khoo', 'කෞ': 'khau', 'කඃ': 'khaH', 'කං': 'khax','කඞ': 'khaX', 'ක්‍ය': 'khya', 'ක්‍ර': 'khra',
    'ඝ': 'gha', 'ක්': 'gh', 'කා': 'ghaa', 'කැ': 'ghA', 'කෑ': 'ghAa','කි': 'ghi', 'කී': 'ghii', 'කු': 'ghu', 'කූ': 'ghuu', 'කෘ': 'ghru', 'කෲ': 'ghruu', 'කෙ': 'ghe','කේ': 'ghee', 'කෛ': 'ghai', 'කො': 'gho', 'කෝ': 'ghoo', 'කෞ': 'ghau', 'කඃ': 'ghaH', 'කං': 'ghax','කඞ': 'ghaX', 'ක්‍ය': 'ghya', 'ක්‍ර': 'ghra',
    'ඡ': 'cha', 'ක්': 'ch', 'කා': 'chaa', 'කැ': 'chA', 'කෑ': 'chAa','කි': 'chi', 'කී': 'chii', 'කු': 'chu', 'කූ': 'chuu', 'කෘ': 'chru', 'කෲ': 'chruu', 'කෙ': 'che','කේ': 'chee', 'කෛ': 'chai', 'කො': 'cho', 'කෝ': 'choo', 'කෞ': 'chau', 'කඃ': 'chaH', 'කං': 'chax','කඞ': 'chaX', 'ක්‍ය': 'chya', 'ක්‍ර': 'chra',
    'ඨ': 'Ta', 'ක්': 'T', 'කා': 'Taa', 'කැ': 'TA', 'කෑ': 'TAa','කි': 'Ti', 'කී': 'Tii', 'කු': 'Tu', 'කූ': 'Tuu', 'කෘ': 'Tru', 'කෲ': 'Truu', 'කෙ': 'Te','කේ': 'Tee', 'කෛ': 'Tai', 'කො': 'To', 'කෝ': 'Too', 'කෞ': 'Tau', 'කඃ': 'TaH', 'කං': 'Tax','කඞ': 'TaX', 'ක්‍ය': 'Tya', 'ක්‍ර': 'Tra',
    'ඪ': 'Da', 'ක්': 'D', 'කා': 'Daa', 'කැ': 'DA', 'කෑ': 'DAa','කි': 'Di', 'කී': 'Dii', 'කු': 'Du', 'කූ': 'Duu', 'කෘ': 'Dru', 'කෲ': 'Druu', 'කෙ': 'De','කේ': 'Dee', 'කෛ': 'Dai', 'කො': 'Do', 'කෝ': 'Doo', 'කෞ': 'Dau', 'කඃ': 'DaH', 'කං': 'Dax','කඞ': 'DaX', 'ක්‍ය': 'Dya', 'ක්‍ර': 'Dra',
    'ථ': 'thha', 'ක්': 'th', 'කා': 'thaa', 'කැ': 'thA', 'කෑ': 'thAa','කි': 'thi', 'කී': 'thii', 'කු': 'thu', 'කූ': 'thuu', 'කෘ': 'thru', 'කෲ': 'thruu', 'කෙ': 'the','කේ': 'thee', 'කෛ': 'thai', 'කො': 'tho', 'කෝ': 'thoo', 'කෞ': 'thau', 'කඃ': 'thaH', 'කං': 'thax','කඞ': 'thaX', 'ක්‍ය': 'thya', 'ක්‍ර': 'thra',
    'ධ': 'dhha','ක්': 'dh', 'කා': 'dhaa', 'කැ': 'dhA', 'කෑ': 'dhAa','කි': 'dhi', 'කී': 'dhii', 'කු': 'dhu', 'කූ': 'dhuu', 'කෘ': 'dhru', 'කෲ': 'dhruu', 'කෙ': 'dhe','කේ': 'dhee', 'කෛ': 'dhai', 'කො': 'dho', 'කෝ': 'dhoo', 'කෞ': 'dhau', 'කඃ': 'dhaH', 'කං': 'dhax','කඞ': 'dhaX', 'ක්‍ය': 'dhya', 'ක්‍ර': 'dhra',
    'ඵ': 'pha', 'ක්': 'ph', 'කා': 'phaa', 'කැ': 'phA', 'කෑ': 'phAa','කි': 'phi', 'කී': 'phii', 'කු': 'phu', 'කූ': 'phuu', 'කෘ': 'phru', 'කෲ': 'phruu', 'කෙ': 'phe','කේ': 'phee', 'කෛ': 'phai', 'කො': 'pho', 'කෝ': 'phoo', 'කෞ': 'phau', 'කඃ': 'phaH', 'කං': 'phax','කඞ': 'phaX', 'ක්‍ය': 'phya', 'ක්‍ර': 'phra',
    'භ': 'bha', 'ක්': 'bh', 'කා': 'bhaa', 'කැ': 'bhA', 'කෑ': 'bhAa','කි': 'bhi', 'කී': 'bhii', 'කු': 'bhu', 'කූ': 'bhuu', 'කෘ': 'bhru', 'කෲ': 'bhruu', 'කෙ': 'bhe','කේ': 'bhee', 'කෛ': 'bhai', 'කො': 'bho', 'කෝ': 'bhoo', 'කෞ': 'bhau', 'කඃ': 'bhaH', 'කං': 'bhax','කඞ': 'bhaX', 'ක්‍ය': 'bhya', 'ක්‍ර': 'bhra',
    'ඟ': 'zga', 'ක්': 'zg', 'කා': 'zgaa', 'කැ': 'zgA', 'කෑ': 'zgAa','කි': 'zgi', 'කී': 'zgii', 'කු': 'zgu', 'කූ': 'zguu', 'කෘ': 'zgru', 'කෲ': 'zgruu', 'කෙ': 'zge','කේ': 'zgee', 'කෛ': 'zgai', 'කො': 'zgo', 'කෝ': 'zgoo', 'කෞ': 'zgau', 'කඃ': 'zgaH', 'කං': 'zgax','කඞ': 'zgaX', 'ක්‍ය': 'zgya', 'ක්‍ර': 'zgra',
    'ඦ': 'zja', 'ක්': 'zj', 'කා': 'zjaa', 'කැ': 'zjA', 'කෑ': 'zjAa','කි': 'zji', 'කී': 'zjii', 'කු': 'zju', 'කූ': 'zjuu', 'කෘ': 'zjru', 'කෲ': 'zjruu', 'කෙ': 'zje','කේ': 'zjee', 'කෛ': 'zjai', 'කො': 'zjo', 'කෝ': 'zjoo', 'කෞ': 'zjau', 'කඃ': 'zjaH', 'කං': 'zjax','කඞ': 'zjaX', 'ක්‍ය': 'zjya', 'ක්‍ර': 'zjra',
    'ඬ': 'zda', 'ක්': 'zd', 'කා': 'zdaa', 'කැ': 'zdA', 'කෑ': 'zdAa','කි': 'zdi', 'කී': 'zdii', 'කු': 'zdu', 'කූ': 'zduu', 'කෘ': 'zdru', 'කෲ': 'zdruu', 'කෙ': 'zde','කේ': 'zdee', 'කෛ': 'zdai', 'කො': 'zdo', 'කෝ': 'zdoo', 'කෞ': 'zdau', 'කඃ': 'zdaH', 'කං': 'zdax','කඞ': 'zdaX', 'ක්‍ය': 'zdya', 'ක්‍ර': 'zdra',
    'ඳ': 'zdha', 'ක්': 'zdh', 'කා': 'zdhaa', 'කැ': 'zdhA', 'කෑ': 'zdhAa','කි': 'zdhi', 'කී': 'zdhii', 'කු': 'zdhu', 'කූ': 'zdhuu', 'කෘ': 'zdhru', 'කෲ': 'zdhruu', 'කෙ': 'zdhe','කේ': 'zdhee', 'කෛ': 'zdhai', 'කො': 'zdho', 'කෝ': 'zdhoo', 'කෞ': 'zdhau', 'කඃ': 'zdhaH', 'කං': 'zdhax','කඞ': 'zdhaX', 'ක්‍ය': 'zdhya', 'ක්‍ර': 'zdhra',
    'ඤ': 'zka','ක්': 'zk', 'කා': 'zkaa', 'කැ': 'zkA', 'කෑ': 'zkAa','කි': 'zki', 'කී': 'zkii', 'කු': 'zku', 'කූ': 'zkuu', 'කෘ': 'zkru', 'කෲ': 'zkruu', 'කෙ': 'zke','කේ': 'zkee', 'කෛ': 'zkai', 'කො': 'zko', 'කෝ': 'zkoo', 'කෞ': 'zkau', 'කඃ': 'zkaH', 'කං': 'zkax','කඞ': 'zkaX', 'ක්‍ය': 'zkya', 'ක්‍ර': 'zkra',
    'ඥ': 'zha', 'ක්': 'zh', 'කා': 'zhaa', 'කැ': 'zhA', 'කෑ': 'zhAa','කි': 'zhi', 'කී': 'zhii', 'කු': 'zhu', 'කූ': 'zhuu', 'කෘ': 'zhru', 'කෲ': 'zhruu', 'කෙ': 'zhe','කේ': 'zhee', 'කෛ': 'zhai', 'කො': 'zho', 'කෝ': 'zhoo', 'කෞ': 'zhau', 'කඃ': 'zhaH', 'කං': 'zhax','කඞ': 'zhaX', 'ක්‍ය': 'zhya', 'ක්‍ර': 'zhra',
    'ඹ': 'Ba', 'ක්': 'B', 'කා': 'Baa', 'කැ': 'BA', 'කෑ': 'BAa','කි': 'Bi', 'කී': 'Bii', 'කු': 'Bu', 'කූ': 'Buu', 'කෘ': 'Bru', 'කෲ': 'Bruu', 'කෙ': 'Be','කේ': 'Bee', 'කෛ': 'Bai', 'කො': 'Bo', 'කෝ': 'Boo', 'කෞ': 'Bau', 'කඃ': 'BaH', 'කං': 'Bax','කඞ': 'BaX', 'ක්‍ය': 'Bya', 'ක්‍ර': 'Bra',
    'ළු': 'Lu', 'ක්': 'k', 'කා': 'kaa', 'කැ': 'kA', 'කෑ': 'kAa','කි': 'ki', 'කී': 'kii', 'කු': 'ku', 'කූ': 'kuu', 'කෘ': 'kru', 'කෲ': 'kruu', 'කෙ': 'ke','කේ': 'kee', 'කෛ': 'kai', 'කො': 'ko', 'කෝ': 'koo', 'කෞ': 'kau', 'කඃ': 'kaH', 'කං': 'kax','කඞ': 'kaX', 'ක්‍ය': 'kya', 'ක්‍ර': 'kra',
    'ැ': 'a','ක්': 'k', 'කා': 'kaa', 'කැ': 'kA', 'කෑ': 'kAa','කි': 'ki', 'කී': 'kii', 'කු': 'ku', 'කූ': 'kuu', 'කෘ': 'kru', 'කෲ': 'kruu', 'කෙ': 'ke','කේ': 'kee', 'කෛ': 'kai', 'කො': 'ko', 'කෝ': 'koo', 'කෞ': 'kau', 'කඃ': 'kaH', 'කං': 'kax','කඞ': 'kaX', 'ක්‍ය': 'kya', 'ක්‍ර': 'kra',
}

def sinhala_to_english_translator(input_text):
    translated_words = []
    current_word = ''
    for char in input_text:
        translated_char = sinhala_to_english.get(char, char)
        if translated_char != ' ':
            current_word += translated_char
        else:
            translated_words.append(current_word)
            current_word = ''
    if current_word:
        translated_words.append(current_word)
    return ' '.join(translated_words)

# Example usage:
sinhala_text = 'මම සිංහලට පත්වූවා.'
english_translation = sinhala_to_english_translator(sinhala_text)
print(english_translation)  # Output: 'mama sinhalaata patawuwaa.'
