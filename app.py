# from chefboost import Chefboost as chef
# import pandas as pd
# import pickle
# import joblib

# df = pd.read_csv("Cleaned-Data.csv")
# config={'enableRandomForest': True, 'num_of_trees': 10}
# model = chef.fit(df,config)
# chef.save_model(model, "model.pkl")

# cols = ['Fever', 'Tiredness', 'Dry-Cough', 'Difficulty-in-Breathing', 'Sore-Throat',
#         'Pains', 'Nasal-Congestion', 'Runny-Nose', 'Diarrhea', 'Smell and taste loss']
# joblib.dump(cols, 'model_cols.pkl')
from nltk.stem.isri import ISRIStemmer
st = ISRIStemmer()
import xlrd
import nltk
nltk.download('punkt')
import pyarabic.araby as ar
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import pandas as pd
from nltk.tokenize import TreebankWordTokenizer
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import sklearn
import numpy
import pickle
# import traceback
import joblib
import numpy as np
import pandas as pd
from chefboost import Chefboost as chef
from flask import Flask, jsonify, request
app = Flask(__name__)

chatIteration = 0
previous = 'حمي'
negations = ["بدون","لا"]
stopWords = [ "صباح","مساءا","ليل","كثير","قليلا","امس","غدا","أمس","اليوم","قليل","كثيرا","ب","أبدا","ابدا","حاد","شديدة","شكرا","عفوا","انا","أنا", "و", "شعور", "لدي", "احيانا", "دائما", "عندى", "نعم", "لا", "فى", "في","حاسة" ,"اشعر","من" , "إلى" , "حتى" , "خلا" , "حاشا" , "عدا", "في" , "عن" , "على" , "مذ" , "منذ", "اعانى"]
wb = xlrd.open_workbook('Symptoms.xls')
sh = wb.sheet_by_index(0)
key = ""
symptomKeywordsDictionary = {}

for i in range(sh.ncols):   
    value = sh.cell(0, i).value  
    for r in range(1, sh.nrows):  
        symptomKeywordsDictionary.update({sh.cell(r, i).value: value})

visited = {}
diagnosed = {}

for i in symptomKeywordsDictionary.values():
    visited[i] = False
    diagnosed[i] = False


@app.route("/", methods=['GET'])
def hello():
    return "hey"

@app.route('/predict', methods=['POST'])
def predict():
    lr = chef.load_model("model.pkl")
    if lr:
        try:
            json = request.get_json()
            # model_columns = chef.load("model_cols.pkl")
            temp = json[0]['values']
            still = False
            inp = temp
            global chatIteration
            global diagnosed
            global visited
            global previous
            global symptomKeywordsDictionary
            cleanedText = nltk.word_tokenize(inp)
            print('previous ' + previous, flush=True)

            if chatIteration > 0:
                if inp == "نعم":
                    diagnosed[previous] = True
                    visited[previous] = True
                    print(visited, flush=True)
                elif inp == "لا":
                    diagnosed[previous] = False
                    visited[previous] = True
                chatIteration = chatIteration + 1     

            if(visited[previous]==False):
                chatIteration = chatIteration + 1     
                ##########
                last = " "
                last2 = " "
                wrongWord=""
                ####
                def remove_prefix_al(text):
                    if text.startswith('ال'):
                        return text[2:]
                    return text
                
                i=0
                while i in range(len(cleanedText)):                             #----------
                    if cleanedText[i] in stopWords:
                        del cleanedText[i]
                        i-=1
                    i+=1

                    #Light Stemming                                                         #####################################
                    j=0
                    for text in cleanedText:
                        # Rule1
                        if len(text) == 5 and text[1] != 'و' and text[3] == 'ئ' and text[2] == 'ا':
                            if text[4] != 'ي' or text[4] != 'ه':
                                textL = list(text)
                                textL[2] = "ي"
                                textL.pop(3)
                                textL.append('ة')
                                new_text = ""
                                for x in textL:
                                    new_text += x
                                if new_text in symptomKeywordsDictionary.keys():
                                    cleanedText[j] = new_text
                                new_text = new_text[-1]
                                if new_text in symptomKeywordsDictionary.keys():
                                    cleanedText[j]=new_text

                        # Rule 2
                        elif len(text) == 5 and text[1] == 'و' and text[3] == 'ئ' and text[2] == 'ا':
                            if text[4] != 'ي' or text[4] != 'ه':
                                textL = list(text)
                                textL.pop(1)
                                textL.append('ة')
                                new_text = ""
                                for x in textL:
                                    new_text += x
                                if new_text in symptomKeywordsDictionary.keys():
                                    cleanedText[j] = new_text
                                new_text = new_text[-1]
                                if new_text in symptomKeywordsDictionary.keys():
                                    cleanedText[j] = new_text

                        # Rule 5
                        elif len(text) == 4 and text[2] == 'و' and text[-1] != 'ه':
                            textL = list(text)
                            textL.pop(2)
                            new_text = ""

                            for x in textL:
                                new_text += x
                            if new_text in symptomKeywordsDictionary.keys():
                                cleanedText[j] = new_text

                        # Rule 6
                        elif len(text) == 5 and text[2] == 'ا':
                            textL = list(text)
                            textL.pop(2)
                            new_text = ""
                            for x in textL:
                                new_text += x
                            if new_text in symptomKeywordsDictionary.keys():
                                cleanedText[j] = new_text

                        # Rule 7
                        elif len(text) == 4 and text[0] == 'ا':
                            textL = list(text)
                            textL.pop(0)
                            new_text = ""
                            for x in textL:
                                new_text += x
                            if new_text in symptomKeywordsDictionary.keys():
                                cleanedText[j] = new_text

                        # Rule 8
                        elif len(text) == 5 and text[0] == 'ا' and text[4] == 'ة':
                            textL = list(text)
                            textL.pop(0)
                            textL.pop(3)

                            new_text = ""
                            i = 0
                            for x in textL:
                                if i == 2:
                                    new_text += 'ا'
                                new_text += x
                                i += 1
                            if new_text in symptomKeywordsDictionary.keys():
                                cleanedText[j] = new_text

                        # Rule 9
                        elif len(text) == 5 and text[0] == 'ا' and text[3] == 'ا' and text[1] != 'ي':
                            textL = list(text)
                            textL.pop(0)
                            textL.pop(2)

                            new_text = ""
                            for x in textL:
                                new_text += x
                            if new_text in symptomKeywordsDictionary.keys():
                                cleanedText[j] = new_text

                        # Rule 3
                        elif len(text) > 3:
                            textL = list(text)
                            x = len(textL)
                            if textL[x - 1] == 'ا' and textL[x - 2] == 'ي' and textL[x - 3] == 'ا':
                                textL.pop(x - 1)
                                textL.pop(x - 2)
                                textL.pop(x - 3)
                                textL.append('ي')
                                textL.append('ة')
                                new_text = ""
                                for x in textL:
                                    new_text += x
                                if new_text in symptomKeywordsDictionary.keys():
                                    cleanedText[j] = new_text
                        j+=1

                for i, item in enumerate (cleanedText):
                    cleanedText[i]=remove_prefix_al(cleanedText[i])
                    cleanedText[i] = cleanedText[i].replace("أ","ا")
                    cleanedText[i] = cleanedText[i].replace("إ","ا")
                    cleanedText[i] = cleanedText[i].replace("لأ","لا")
                    cleanedText[i] = cleanedText[i].replace("ة", "ه")                   
                    if cleanedText[i][0] =='ب':
                        cleanedText[i] = cleanedText[i][1:]    
                    if cleanedText[i][-1] == "ي":
                        cleanedText[i] =  cleanedText[i][:-1] + "ى"

                    cleanedText[i]=ar.strip_tashkeel(cleanedText[i])
                
                ####
                splitted=cleanedText
                done = False
                i=0
                while(i <= len(splitted)-1 ):                                   #----------
                    done = False
                    item =splitted[i]
                    wrongWord=item
                    if item not in negations:
                        if item in symptomKeywordsDictionary.keys():
                            done =True
                            if visited[symptomKeywordsDictionary[item]] == True:
                                i+=1
                                continue
                            visited[symptomKeywordsDictionary[item]] = True
                            if i >= 1:
                                last = splitted[i-1]
                                if i > 1:
                                    last2 = splitted[i-2]
                                if last in negations or last2 in negations:
                                    diagnosed[symptomKeywordsDictionary[item]] = False
                                else:

                                    diagnosed[symptomKeywordsDictionary[item]] = True
                            else:
                                diagnosed[symptomKeywordsDictionary[item]] = True
                            i+=1
                            print(visited, flush=True)
                            continue
                        if i < len(splitted)-1 and done != True:
                            temp = item+" "+splitted[i+1]
                            wrongWord=temp
                            if temp in symptomKeywordsDictionary.keys():
                                i+=1                                    #-- in case of composite function doesn't take the next word
                                done = True

                                if visited[symptomKeywordsDictionary[temp]] == True:
                                    i += 2
                                    continue
                                visited[symptomKeywordsDictionary[temp]] = True

                                if i >= 1:
                                    last = splitted[i - 1]
                                    if i > 1:
                                        last2 = splitted[i - 2]
                                    if last in negations or last2 in negations:
                                        diagnosed[symptomKeywordsDictionary[temp]] = False
                                    else:
                                        diagnosed[symptomKeywordsDictionary[temp]] = True
                                else:
                                    diagnosed[symptomKeywordsDictionary[temp]] = True
                                i+=1
                                print(visited, flush=True)
                                continue

                        if i < len(splitted)-2 and done != True:
                            temp2 = item+" "+splitted[i+1]+" "+splitted[i+2]
                            wrongWord=temp2
                            if temp2 in symptomKeywordsDictionary.keys():
                                i+=2                                                        #-- //
                                done = True

                                if visited[symptomKeywordsDictionary[temp2]] == True:
                                    i += 3
                                    continue

                                visited[symptomKeywordsDictionary[temp2]] = True
                                if i >= 1:
                                    last = splitted[i - 1]
                                    if i > 1:
                                        last2 = splitted[i - 2]
                                    if last in negations or last2 in negations:
                                        diagnosed[symptomKeywordsDictionary[temp2]] = False
                                    else:
                                        diagnosed[symptomKeywordsDictionary[temp2]] = True
                                else:
                                    diagnosed[symptomKeywordsDictionary[temp2]] = True
                                i = i + 2
                                continue

                        if(done==False):
                            distance = 10
                            rightWord=""
                            finalWord = ""
                            for x in symptomKeywordsDictionary.keys():
                                d = nltk.edit_distance(word, x)
                                if d < distance:
                                    distance = d
                                    rightWord = x

                            if distance < 2 :
                                visited[symptomKeywordsDictionary[rightWord]] = True
                                finalWord = rightWord
                            else:
                                finalWord = 'x'

                            compositeCheck= finalWord.split()
                            if(len(compositeCheck)==2):                                  #------- //
                                i+=1
                            elif(len(compositeCheck)==3):
                                i+=2
                            print(finalWord)
                            if finalWord != "x":
                                if i >= 1:
                                    last = splitted[i - 1]
                                    if i > 1:
                                        last2 = splitted[i - 2]
                                    if last in negations or last2 in negations:
                                        diagnosed[symptomKeywordsDictionary[finalWord]] = False
                                    else:
                                        diagnosed[symptomKeywordsDictionary[finalWord]] = True
                                else:
                                    diagnosed[symptomKeywordsDictionary[finalWord]] = True
                            i += 1
                    else:
                        i+=1
                    #########
                # txtProcess(inp, symptomKeywordsDictionary, visited, diagnosed)

            for i in symptomKeywordsDictionary.values():
                if visited[i] == False:    
                    previous = i
                    return jsonify({'prediction': str("هل تشعر ب" + i)})

            prediction = chef.predict(lr, [diagnosed['حمي'], diagnosed['إرهاق'], diagnosed['سعال'], diagnosed['ضيق تنفس'], diagnosed['احتقان حلق'], diagnosed['آلام'], diagnosed['احتقان انف'], diagnosed['سيلان انف'], diagnosed['اسهال'],diagnosed['فقدان حاسة الشم و التذوق']])

            if prediction == "yes":
                # diagnosed.clear()
                # visited.clear()
                return jsonify({'prediction': "تم تشخيصك بفيروس كورونا المستجد." , 'dict': diagnosed})
            else:
                return jsonify({'prediction': "لم يتم تشخيصك بفيروس كورونا المستجد." , 'dict': diagnosed})

            print("here:", prediction , flush=True)
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        return jsonify({'trace': 'Couldnt find model'})

@app.route('/updatePrediction', methods=['POST'])
def updatePrediction():
    lr = chef.load_model("model.pkl")
    if lr:
        try:
            json = request.get_json()
            # model_columns = chef.load("model_cols.pkl")
            temp = json[0]['values']
            print(temp, flush=True)
            
            prediction = chef.predict(lr, temp)
            if prediction == "yes":
                return jsonify({'prediction': "yes"})
            else:
                return jsonify({'prediction': "no"})

            print("here:", prediction , flush=True)
        except:
            return jsonify({'trace': 'error'})
    else:
        return ('No model here to use')

@app.route('/resetData', methods=['POST'])
def resetData():
    try:
        global diagnosed
        global visited
        global symptomKeywordsDictionary
        global chatIteration
        global previous
        chatIteration = 0
        previous = 'حمي'
        for i in symptomKeywordsDictionary.values():
            visited[i] = False
            diagnosed[i] = False
        return jsonify({'done': "yes"})
    except:
        return jsonify({'trace': 'error'})
           
if __name__ == '__main__':
    app.run(debug=True)