import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.0020

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.0800
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] =  False
    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    

    answers['(c) Weight update'] = 0.5 * math.log((1 - p) / p)

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.526 #1.528
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = "ensemble methods allows multiple methods to improve the performance but each method need to be trained on relevant data(past) but here alna using random selection which doent supports that"
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = "iii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = "i"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = "ii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = "iv"
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] =  "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = "no"

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "Both classifiers perform as random guessing where TPR is equal to FPR. Increasing the probability of predicting the + class does not make C2 better, as it increases both TPR and FPR equally, maintaining performance equivalent to random chance."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) explain'] = "TPR and FPR take into account both the positive predictions and their impact on the overall performance in the context of both classes. Since C1 and C2 have equal TPR and FPR, they perform the same according to the random guess baseline in an ROC curve. Precision and recall do not consider true negatives and are thus less informative for comparing classifiers that output random predictions on imbalanced classes."

    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = "C2"

    # type: explain_string
    answers['(i) Best classifier, explain'] = "C2 has a significantly higher TPR (50%) compared to C1 (10%), which means it is better at identifying positive cases. Both have the same precision, but C2 is more effective overall."


    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = "precision-recall-F1-Measure"

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "The precision, recall, and F1-measure give a more complete picture of a classifier’s performance, especially in the context of imbalanced datasets. These metrics consider both the ability to identify positive cases correctly and the avoidance of misclassifying negative cases as positive."


    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = "C2" #c3

    # type: explain_string
    answers['(iii) best classifier, explain'] = "C2 achieves the best balance between precision and recall, indicated by the highest F1-measure (50%) among the classifiers. It suggests that C2 is more reliable for correctly identifying positive cases while maintaining a reasonable level of precision."
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = (p*100)/(p*1000)

    # type: eval_float
    answers['(a) recall for C0'] = P

    # type: eval_float
    answers['(b) F-measure of C0'] = (0.2 * p) / (0.1 + p)

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no' 

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.1000#0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] =  {
    'recall': 0.5333,
    'precision': 0.6154,
    'F-measure': 0.5689,
    'accuracy': 0.8800
}

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure' #precision

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy' #accuracy

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = 'Accuracy is the best indicator since it accounts for all correct predictions (both true positives and true negatives) over the total number of samples. Precision is the worst in this context because it does not take into account the correct predictions of the majority class, which can be misleading for imbalanced datasets.'
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = "T1"

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = "T2"

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = 'The F1 score is preferred in medical testing scenarios because it provides a balance between precision and recall, which is critical in ensuring that cases are correctly identified while minimizing false negatives, which could be life-threatening in the case of cancer detection.'

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = 'In a scenario where the cost of false positives is very high, such as when follow-up procedures are invasive, expensive, or carry significant risks, the TPR/FPR ratio might be preferred to minimize the risk of false alarms while maintaining an acceptable detection rate of true positives.'
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
