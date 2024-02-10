import re


def sinhala_to_latin(text):
    vowelsUni = ['ඌ', 'ඕ', 'ඕ', 'ආ', 'ආ', 'ඈ', 'ඈ', 'ඈ', 'ඊ', 'ඊ', 'ඊ', 'ඊ', 'ඒ', 'ඒ', 'ඒ', 'ඌ', 'ඌ', 'ඖ', 'ඇ', 'අ', 'ඇ', 'ඉ', 'එ', 'උ', 'ඔ', 'ඓ']
    vowels = ['oo', 'o\\)', 'oe', 'aa', 'a\\)', 'Aa', 'A\\)', 'ae', 'ii', 'i\\)', 'ie', 'ee', 'ea', 'e\\)', 'ei', 'uu', 'u\\)', 'au', '/\\a', 'a', 'A', 'i', 'e', 'u', 'o', 'I']

    specialConsonantsUni = ['ං', 'ඃ', 'ඞ', 'ඍ', 'ර්'+'\u200D', 'ර්'+'\u200D']
    specialConsonants = ['\\n', '\\h', '\\N', '\\R', 'R', '\\r']

    consonantsUni = ['ඬ', 'ඳ', 'ඟ', 'ථ', 'ධ', 'ඝ', 'ඡ', 'ඵ', 'භ', 'ශ', 'ෂ', 'ඥ', 'ඤ', 'ළු', 'ද', 'ච', 'ඛ', 'ත', 'ට', 'ක', 'ඩ', 'න', 'ප', 'බ', 'ම', '‍ය', '‍ය', 'ය', 'ජ', 'ල', 'ව', 'ව', 'ස', 'හ', 'ණ', 'ළ', 'ඛ', 'ඝ', 'ඨ', 'ඪ', 'ඵ', 'ඹ', 'ෆ', 'ඣ', 'ග', 'ර']
    consonants = ['nnd', 'nndh', 'nng', 'Th', 'Dh', 'gh', 'Ch', 'ph', 'bh', 'sh', 'Sh', 'GN', 'KN', 'Lu', 'dh', 'ch', 'kh', 'th', 't', 'k', 'd', 'n', 'p', 'b', 'm', '\\\\' + 'y', 'Y', 'y', 'j', 'l', 'v', 'w', 's', 'h', 'N', 'L', 'K', 'G', 'T', 'D', 'P', 'B', 'f', 'q', 'g', 'r']

    vowelModifiersUni = ['ූ', 'ෝ', 'ෝ', 'ා', 'ා', 'ෑ', 'ෑ', 'ෑ', 'ී', 'ී', 'ී', 'ී', 'ේ', 'ේ', 'ේ', 'ූ', 'ූ', 'ෞ', 'ැ']
    vowelModifiers = ['uu', 'oo', 'oo', 'aa', 'aa', 'ae', 'ae', 'ae', 'ii', 'ii', 'ii', 'ii', 'ea', 'ea', 'ea', 'uu', 'uu', 'au', 'a']

    specialCharUni = ['ෲ', 'ෘ']
    specialChar = ['ruu', 'ru']

    for i in range(len(specialConsonants)):
        text = re.sub(re.escape(specialConsonants[i]), specialConsonantsUni[i], text)

    for i in range(len(specialChar)):
        for j in range(len(consonants)):
            s = consonants[j] + specialChar[i]
            v = consonantsUni[j] + specialCharUni[i]
            text = re.sub(re.escape(s), v, text)

    for i in range(len(vowelsUni)):
        text = re.sub(re.escape(vowelsUni[i]), vowels[i], text)
    
    for i in range(len(vowelModifiersUni)):
        text = re.sub(re.escape(vowelModifiersUni[i]), vowelModifiers[i], text)

    for i in range(len(consonantsUni)):
        text = re.sub(re.escape(consonantsUni[i]), consonants[i], text)

    for i in range(len(specialCharUni)):
        text = re.sub(re.escape(specialCharUni[i]), specialChar[i], text)

    return text

input_text = "අන්තර්ජාලයේ දියුණුවට දායක වූ ප්‍රසිද්ධ විද්‍යාඥයෙක් නම් කරන්න."
output_text = sinhala_to_latin(input_text)
print(output_text)
