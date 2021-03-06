
import json
from flask import Flask
import random 
import time
import string
from flask import request, render_template
import ast
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def user_id_processor(user_value):
    alphabet = (list(string.ascii_uppercase))
        
    picked_numbers = []
    try:
        f = open("user_id.txt","r")
        USER_ID_DICT = f.read()
        USER_ID_DICT = list(ast.literal_eval(USER_ID_DICT))
        for u in USER_ID_DICT:
            picked_numbers.append((list(u.keys())[0]))
        f.close()
    except:
        print('No Users have been inserted yet! ')
    if user_value!=None:
        
        if user_value in picked_numbers:
            dict_of_number = USER_ID_DICT[picked_numbers.index(user_value)]
            letters = dict_of_number[picked_numbers[picked_numbers.index(user_value)]]
        else:
            print('The number is a new one.')
            input_user = user_value
            name = random.choices(alphabet, k=6)
            letters = name[0]
            for l in name:
                letters = letters + l
            json_str = json.dumps({str(input_user):letters})
            f = open("user_id.txt", "a")
            f.write(json_str+',')
            f.close()
    return letters

start = time.time()
end = time.time()+600
app = Flask(__name__)

@app.route('/user_id=<userID>/login')
def InputMaker(userID):
    input_id = userID
    output = user_id_processor(input_id)
    write_json= json.dumps({"user":output})

    return '''
              <h1>{}</h1>'''.format(write_json)


@app.route('/level_id=<levelID>/sessionkey=<sessionkeyID>')
def my_form(levelID,sessionkeyID):
    return render_template('index.html')

@app.route('/level_id=<levelID>/sessionkey=<sessionkeyID>',methods=['POST'])

def LevelMaker(levelID,sessionkeyID):
    if start<end:
        pass
    else:
        exit()

   # write_json= json.dumps({levelID:sessionkeyID})
    score = request.form['variable']

    
    try:
        with open("levelID"+str(levelID)+'summary.txt','a') as f:
    
            f.write(sessionkeyID+',')
            f.write(score+'/')
    except:
        with open("levelID"+str(levelID)+'summary.txt','w') as f:
    
            f.write(sessionkeyID+',')
            f.write(score+'/')
    return ''

@app.route('/level_id=<levelID>/highscorelist')

def SummaryLevel(levelID):
    if start<end:
        pass
    else:
        exit()

    f = open('levelID'+str(levelID)+'summary.txt','r')
    
    summary_level = f.read().split('/')
    summary_scores = []
    summary_keys = []
    for s in range(len(summary_level)-1):
        summary_keys.append(summary_level[s].split(',')[0])
        summary_scores.append(int(summary_level[s].split(',')[1]))
    sorted_summ_scores = sorted(summary_scores)
    sorted_summ_keys = []
    INDICES = []
    for value in sorted(list(set(sorted_summ_scores))):
        INDICES.append([i for i, x in enumerate(summary_scores) if x == value])
    for i in INDICES:
        for j in i:
            #sorted_summ_keys.append(summary_keys[summary_scores.index(sorted_summ_scores[j])])
            sorted_summ_keys.append(summary_keys[j])
    f.close()
    cleaned_keys = sorted(list(set(sorted_summ_keys)))
    cleaned_scores = []
    
    for key in cleaned_keys:
        V=[]
        for i in range(len(sorted_summ_keys)):
            if key==sorted_summ_keys[i]:
                V.append(sorted_summ_scores[i])
        cleaned_scores.append(max(V))    
    
    cleaned_scores_sort = sorted(cleaned_scores)
    sort_index = [i[0] for i in sorted(enumerate(cleaned_scores), key=lambda x:x[1])]
    cleaned_keys_sort = []
    for index in sort_index:
        cleaned_keys_sort.append(cleaned_keys[index])
    
    last = len(cleaned_keys_sort)
    if len(cleaned_keys_sort)>15:
        cleaned_keys_sort = cleaned_keys_sort[last-1-15:last-1]
        cleaned_scores_sort = cleaned_scores_sort[last-1-15:last-1]
        
            
    
    final_dict = {"sessionkey":cleaned_keys_sort, "scores": cleaned_scores_sort}
    write_json = json.dumps(final_dict)

    return '''
              <h1>{}</h1>'''.format(write_json)
              
              
# @app.route('/<levelID>/<sessionkeyID>')
# def LevelMaker(levelID,sessionkeyID):
#     level_ID = levelID
#     sessionkeyID = sessionkeyID
#     write_json= json.dumps({levelID:sessionkeyID})
#     return '''
#               <h1>{}</h1>'''.format(write_json)


if __name__ == "__main__":

    app.run(host='localhost', port=8080)

    
