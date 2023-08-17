# Web-User-Recommendation
Task-Oriented Web User Modeling for Recommendation with Association Rule Mining

Paper searching and analysing about the given subject.
Literature search for datasets (which was not easy as they were few and too large for memory sadly).
Looked for different methods and models to see which one is best to use.

At the end, I couldn't find any dataset to work with as most of them had security issues.

So, I customize my own dataset from the "Task-Oriented Web User Modeling for Recommendation" paper. 
Took the data that was given there and made my own .csv file. 

Turkish work flow:
İşlem kayıtları: user log
İşlem kayıtları alınır/kaydedilir>belli bir süre içerisinde yapılmış işlemler içinden kesitler alınır> kullanıcı işlemine geçmişten en yakını bulunur>öneri yapılır

IMPORTANT: 
Used Sypder ID.

2 methods have been used.
1.	Using Similarity algorithms
Similarity matrix is used.
Used mlxtend
pip install mlxtend

2.	Using Association Rule Mining : Better for this case, because it lookes for past cases
Used mlxtend
pip install mlxtend

Used Apriori
Choose one from the following for installation:
Install with pip pip install apyori.
Put apyori.py into your project.
Run python setup.py install.

Antecedent: This is the set of items that are present in the data and form the basis of the rule. It's the "if" part of the rule.
Consequent: This is the set of items that are predicted to occur if the antecedent is present. It's the "then" part of the rule.
