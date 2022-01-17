import time
import random
from itertools import islice

list_common_words = ['the', 'you', 'that', 'he', 'was', 'for', 'on', 'are',
                     'with', 'as', 'I', 'his', 'they', 'be', 'at', 'one', 'have',
                     'this', 'from', 'or', 'had', 'by', 'not', 'word', 'but',
                     'what', 'some', 'we', 'can', 'out', 'other', 'were', 'all',
                     'there', 'when', 'up', 'use', 'your', 'how', 'said', 'an',
                     'each', 'she', 'which', 'do', 'their', 'time', 'if', 'will',
                     'way', 'about', 'many', 'then', 'them', 'write', 'would', 'like',
                     'so', 'these', 'her', 'long', 'make', 'thing', 'see', 'him',
                     'two', 'has', 'look', 'more', 'day', 'could', 'go', 'come', 'did',
                     'number', 'sound', 'no', 'most', 'people', 'my', 'over', 'know',
                     'water', 'than', 'call', 'first', 'who', 'may', 'down', 'side',
                     'been', 'now', 'find', 'any', 'new', 'work', 'part', 'take',
                     'get', 'place', 'made', 'live', 'where', 'after', 'back', 'little',
                     'only', 'round', 'man', 'year', 'came', 'show', 'every', 'good', 'me',
                     'give', 'our', 'under', 'name', 'very', 'through', 'just', 'form',
                     'sentence', 'great', 'think', 'say', 'help', 'low', 'line', 'differ',
                     'turn', 'cause', 'much', 'mean', 'before', 'move', 'right', 'boy', 'old',
                     'too', 'same', 'tell', 'does', 'set', 'three', 'want', 'air', 'well',
                     'also', 'play', 'small', 'end', 'put', 'home', 'read', 'hand', 'port',
                     'large', 'spell', 'add', 'even', 'land', 'here', 'must', 'big', 'high', 'such',
                     'follow', 'act', 'why', 'ask', 'men', 'change', 'went', 'light', 'kind', 'off',
                     'need', 'house', 'picture', 'try', 'us', 'again', 'animal', 'point', 'mother',
                     'world', 'near', 'build', 'self', 'earth', 'father', 'head', 'stand', 'own',
                     'page', 'should', 'country', 'found', 'answer', 'school', 'grow', 'study',
                     'still', 'learn', 'plant', 'cover', 'food', 'sun', 'four', 'between', 'state',
                     'keep', 'eye', 'never', 'last', 'let', 'thought', 'city', 'tree', 'cross',
                     'farm', 'hard', 'start', 'might', 'story', 'saw', 'far', 'sea', 'draw', 'left',
                     'late', 'run', "don't", 'while', 'press', 'close', 'night', 'real', 'life',
                     'few', 'north', 'open', 'seem', 'together', 'next', 'white', 'children', 'begin',
                     'got', 'walk', 'example', 'ease', 'paper', 'group', 'always', 'music', 'those',
                     'both', 'mark', 'often', 'letter', 'until', 'mile', 'river', 'car', 'feet',
                     'care', 'second', 'book', 'carry', 'took', 'science', 'eat', 'room', 'friend',
                     'began', 'idea', 'fish', 'mountain', 'stop', 'once', 'base', 'hear', 'horse',
                     'cut', 'sure', 'watch', 'color', 'face', 'wood', 'main', 'enough', 'plain',
                     'girl', 'usual', 'young', 'ready', 'above', 'ever', 'red', 'list', 'though',
                     'feel', 'talk', 'bird', 'soon', 'body', 'dog', 'family', 'direct', 'pose',
                     'leave', 'song', 'measure', 'door', 'product', 'black', 'short', 'numeral',
                     'class', 'wind', 'question', 'happen', 'complete', 'ship', 'area', 'half',
                     'rock', 'order', 'fire', 'south', 'problem', 'piece', 'told', 'knew', 'pass',
                     'since', 'top', 'whole', 'king', 'space', 'heard', 'best', 'hour', 'better',
                     'true', 'during', 'hundred', 'five', 'remember', 'step', 'early', 'hold', 'west',
                     'ground', 'interest', 'reach', 'fast', 'verb', 'sing', 'listen', 'six', 'table',
                     'travel', 'less', 'morning', 'ten', 'simple', 'several', 'vowel', 'toward', 'war',
                     'lay', 'against', 'pattern', 'slow', 'center', 'love', 'person', 'money', 'serve',
                     'appear', 'road', 'map', 'rain', 'rule', 'govern', 'pull', 'cold', 'notice',
                     'voice', 'unit', 'power', 'town', 'fine', 'certain', 'fly', 'fall', 'lead',
                     'cry', 'dark', 'machine', 'note', 'wait', 'plan', 'figure', 'star', 'box',
                     'noun', 'field', 'rest', 'correct', 'able', 'pound', 'done', 'beauty', 'drive',
                     'stood', 'contain', 'front', 'teach', 'week', 'final', 'gave', 'green', 'oh', 'quick',
                     'develop', 'ocean', 'warm', 'free', 'minute', 'strong', 'special', 'mind', 'behind',
                     'clear', 'tail', 'produce', 'fact', 'street', 'inch', 'multiply', 'nothing', 'course',
                     'stay', 'wheel', 'full', 'force', 'blue', 'object', 'decide', 'surface', 'deep', 'moon',
                     'island', 'foot', 'system', 'busy', 'test', 'record', 'boat', 'common', 'gold', 'possible',
                     'plane', 'stead', 'dry', 'wonder', 'laugh', 'thousand', 'ago', 'ran', 'check', 'game',
                     'shape', 'equate', 'hot', 'miss', 'brought', 'heat', 'snow', 'tire', 'bring', 'yes',
                     'distant', 'fill', 'east', 'paint', 'language', 'among', 'grand', 'ball', 'yet', 'wave',
                     'drop', 'heart', 'am', 'present', 'heavy', 'dance', 'engine', 'position', 'arm', 'wide',
                     'sail', 'material', 'size', 'vary', 'settle', 'speak', 'weight', 'general', 'ice', 'matter',
                     'circle', 'pair', 'include', 'divide', 'syllable', 'felt', 'perhaps', 'pick', 'sudden',
                     'count', 'square', 'reason', 'length', 'represent', 'art', 'subject', 'region', 'energy',
                     'hunt', 'probable', 'bed', 'brother', 'egg', 'ride', 'cell', 'believe', 'fraction',
                     'forest', 'sit', 'race', 'window', 'store', 'summer', 'train', 'sleep', 'prove', 'lone',
                     'leg', 'exercise', 'wall', 'catch', 'mount', 'wish', 'sky', 'board', 'joy', 'winter',
                     'sat', 'written', 'wild', 'instrument', 'kept', 'glass', 'grass', 'cow', 'job', 'edge',
                     'sign', 'visit', 'past', 'soft', 'fun', 'bright', 'gas', 'weather', 'month', 'million',
                     'bear', 'finish', 'happy', 'hope', 'flower', 'clothe', 'strange', 'gone', 'jump', 'baby',
                     'eight', 'village', 'meet', 'root', 'buy', 'raise', 'solve', 'metal', 'whether', 'push',
                     'seven', 'paragraph', 'third', 'shall', 'held', 'hair', 'describe', 'cook', 'floor',
                     'either', 'result', 'burn', 'hill', 'safe', 'cat', 'century', 'consider', 'type', 'law',
                     'bit', 'coast', 'copy', 'phrase', 'silent', 'tall', 'sand', 'soil', 'roll', 'temperature',
                     'finger', 'industry', 'value', 'fight', 'lie', 'beat', 'excite', 'natural', 'view', 'sense',
                     'ear', 'else', 'quite', 'broke', 'case', 'middle', 'kill', 'son', 'lake', 'moment', 'scale',
                     'loud', 'spring', 'observe', 'child', 'straight', 'consonant', 'nation', 'dictionary',
                     'milk', 'speed', 'method', 'organ', 'pay', 'age', 'section', 'dress', 'cloud', 'surprise',
                     'quiet', 'stone', 'tiny', 'climb', 'cool', 'design', 'poor', 'lot', 'experiment', 'bottom',
                     'key', 'iron', 'single', 'stick', 'flat', 'twenty', 'skin', 'smile', 'crease', 'hole',
                     'trade', 'melody', 'trip', 'office', 'receive', 'row', 'mouth', 'exact', 'symbol', 'die',
                     'least', 'trouble', 'shout', 'except', 'wrote', 'seed', 'tone', 'join', 'suggest', 'clean',
                     'break', 'lady', 'yard', 'rise', 'bad', 'blow', 'oil', 'blood', 'touch', 'grew', 'cent',
                     'mix', 'team', 'wire', 'cost', 'lost', 'brown', 'wear', 'garden', 'equal', 'sent', 'choose',
                     'fell', 'fit', 'flow', 'fair', 'bank', 'collect', 'save', 'control', 'decimal', 'gentle',
                     'woman', 'captain', 'practice', 'separate', 'difficult', 'doctor', 'please', 'protect',
                     'noon', 'whose', 'locate', 'ring', 'character', 'insect', 'caught', 'period', 'indicate',
                     'radio', 'spoke', 'atom', 'human', 'history', 'effect', 'electric', 'expect', 'crop',
                     'modern', 'element', 'hit', 'student', 'corner', 'party', 'supply', 'bone', 'rail',
                     'imagine', 'provide', 'agree', 'thus', 'capital', "won't", 'chair', 'danger', 'fruit',
                     'rich', 'thick', 'soldier', 'process', 'operate', 'guess', 'necessary', 'sharp', 'wing',
                     'create', 'neighbor', 'wash', 'bat', 'rather', 'crowd', 'corn', 'compare', 'poem', 'string',
                     'bell', 'depend', 'meat', 'rub', 'tube', 'famous', 'dollar', 'stream', 'fear', 'sight',
                     'thin', 'triangle', 'planet', 'hurry', 'chief', 'colony', 'clock', 'mine', 'tie', 'enter',
                     'major', 'fresh', 'search', 'send', 'yellow', 'gun', 'allow', 'print', 'dead', 'spot',
                     'desert', 'suit', 'current', 'lift', 'rose', 'continue', 'block', 'chart', 'hat', 'sell',
                     'success', 'company', 'subtract', 'event', 'particular', 'deal', 'swim', 'term', 'opposite', 'wife',
                     'shoe', 'shoulder', 'spread', 'arrange', 'camp', 'invent', 'cotton', 'born', 'determine', 'quart',
                     'nine', 'truck', 'noise', 'level', 'chance', 'gather', 'shop', 'stretch', 'throw', 'shine', 'property',
                     'column', 'molecule', 'select', 'wrong', 'gray', 'repeat', 'require', 'broad', 'prepare', 'salt', 'nose',
                     'plural', 'anger', 'claim', 'continent', 'oxygen', 'sugar', 'death', 'pretty', 'skill', 'women', 'season',
                     'solution', 'magnet', 'silver', 'thank', 'branch', 'match', 'suffix', 'especially', 'fig', 'afraid', 'huge',
                     'sister', 'steel', 'discuss', 'forward', 'similar', 'guide', 'experience', 'score', 'apple', 'bought', 'led',
                     'pitch', 'coat', 'mass', 'card', 'band', 'rope', 'slip', 'win', 'dream', 'evening', 'condition', 'feed', 'tool',
                     'total', 'basic', 'smell', 'valley', 'nor', 'double', 'seat', 'arrive', 'master', 'track', 'parent', 'shore',
                     'division', 'sheet', 'substance', 'favor', 'connect', 'post', 'spend', 'chord', 'fat', 'glad', 'original',
                     'share', 'station', 'dad', 'bread', 'charge', 'proper', 'bar', 'offer', 'segment', 'slave', 'duck', 'instant',
                     'market', 'degree', 'populate', 'chick', 'dear', 'enemy', 'reply', 'drink', 'occur', 'support', 'speech',
                     'nature', 'range', 'steam', 'motion', 'path', 'liquid', 'log', 'meant', 'quotient', 'teeth', 'shell', 'nec']
list_keyboard_letters_decimal = [113, 119, 101, 114, 116, 121, 117, 105,
                                 111, 112, 97, 115, 100, 102, 103, 104,
                                 106, 107, 108, 122, 120, 99, 118, 98,
                                 110, 109, 113, 119, 101, 114, 116, 121,
                                 117, 105, 111, 112, 97, 115, 100]
list_61k_common_words = []

file = open('my_pass_list.txt', 'w')
file1 = open('61kENGwords.txt', 'r')

def file_to_list(file):
    for i in file:
        if len(i) > 5:
            list_61k_common_words.append(i[:-1])
def str_to_list(str):
    list = []
    for i in str:
        list.append(i)
    return list
def just_word ():
    rand_word = random.randint(0, len(list_61k_common_words) - 1)
    password = list_61k_common_words[rand_word]
    return password
def real_unique_password():
    length_of_password = random.randint(8, 14)
    password = ""
    for i in range(length_of_password):
        rand_chr = chr(random.randint(48, 126))
        password += rand_chr
    return password
def random_numbers():
    password = ""
    for i in range(random.randint(0, 12)):
        rnd_num = random.randint(0, 9)
        password += str(rnd_num)
    return password
def mix_upped_lower_case(password_to_mix):
    temp_password = str_to_list(password_to_mix)
    length = len(temp_password)
    #for i in range(5):
        #temp_password.append(" ")
    for i in range(length):
        if random.randint(100, 10000) % 2 == 0:
            temp_letter = temp_password[i]
            if ord(temp_letter) >= 65 and ord(temp_letter) <= 90:
                temp_password.remove(temp_password[i])
                temp_password.insert(i, chr(ord(temp_letter) + 32))
            if ord(temp_letter) >= 97 and ord(temp_letter) <= 122:
                temp_password.remove(temp_password[i])
                temp_password.insert(i, chr(ord(temp_letter) - 32))
    return "".join([str(elem) for elem in temp_password])
def combine_words_from_file():
    password_length = random.randint(5, 8)
    password = ""
    while (len(password) <= password_length):
        temp = random.randint(0, 950)
        password += list_common_words[temp]
    return password
def replace_letter_with_symbol(password):
    upd_password = ""
    for i in password:
        temp = i
        if ord(i) == 105:
            temp = "1"
        if ord(i) == 111:
            temp = "0"
        upd_password += temp
    return upd_password
def add_numbers(password_to_update):
    option = random.randint(1, 3)
    front = ""
    end = ""
    password = ""
    if option == 1:
        number_numbers = random.randint(1, 8)
        for i in range(1, number_numbers):
            front += str(i)
    if option == 2:
        number_numbers = random.randint(1, 8)
        for i in range(1, number_numbers):
            end += str(i)
    if option == 3:
        number_numbers_front = random.randint(1, 5)
        number_numbers_end = random.randint(1, 5)
        for i in range(1, number_numbers_front):
            front += str(i)
        for i in range(1, number_numbers_end):
            end += str(i)
    password = front + password_to_update + end
    return password
def sequences_letters():
    guess = random.randint(0, 26)
    number = random.randint(6, 9)
    password = ""
    for i in range(number):
        password += chr(list_keyboard_letters_decimal[guess + i])
    return password


def writing_file():
    for i in range(30000):
        for k in range(0, 25):
            guess = random.randint(1, 10)
            if guess == 1:
                password = mix_upped_lower_case(just_word())
                file.write(password + '\n')
            if guess == 2:
                password = replace_letter_with_symbol(just_word())
                file.write(password + '\n')
            if guess == 3:
                password = sequences_letters()
                file.write(password + '\n')
            if guess == 4:
                password = just_word()
                file.write(password + '\n')
            if guess == 5:
                password = add_numbers(sequences_letters())
                file.write(password + '\n')
            if guess == 6:
                password = add_numbers(just_word())
                file.write(password + '\n')
            if guess == 7:
                password = mix_upped_lower_case(sequences_letters())
                file.write(password + '\n')
            if guess == 8:
                password = just_word()
                file.write(password + '\n')
            if guess == 9:
                password = just_word()
                file.write(password + '\n')
            if guess == 10:
                password = just_word()
                file.write(password + '\n')
        file.write(real_unique_password() + '\n')

file_to_list(file1)
writing_file()
#file_to_list(file1)
#print(list_61k_common_words)




#pas = real_unique_password()
#print("real unique password: ", pas)
#print("mixed password: ", mix_upped_lower_case(pas))
#mixed_words = combine_words_from_file()
#print("mixed words: ", mixed_words)
#replaced_symbols = replace_letter_with_symbol(mixed_words)
#print("replaced symbols: ", replaced_symbols)
#with_add_numbers = add_numbers(replaced_symbols)
#print("with add numbers: ", with_add_numbers)
#sequances = sequences_letters()
#print("sequances: ", sequances)
