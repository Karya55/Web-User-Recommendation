# -*- coding: utf-8 -*-
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

class RecommendationSystem:
    def __init__(self):
        # saving the example resources and their corresponding page url's
        self.resources = {
            "Admission – orientation info": "URL1",
            "Admission – F1 visa and I20 info": "URL2",
            "Admission": "URL3",
            "Online application - start": "URL4",
            "Online application – step 1": "URL5",
            "Online application – step 2": "URL6",
            "Online application - finish": "URL7",
            "Department main page": "URL8"
        }
        
    def preprocess_data(self, df):
        # Comverting user log's to specified data format 
        user_logs = df['Admission main page'].tolist()  # Assuming given column contains user logs
        transactions = [log.split("-")[-1].strip().split() for log in user_logs]
        return pd.DataFrame(transactions)
    
    def associate_resources(self, df, min_support=0.3, min_confidence=0.7): 
        # Association rule mining with user log's
        data = self.preprocess_data(df)
        frequent_itemsets = apriori(data, min_support=min_support, use_colnames=True)
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
        
        recommended_resources = set()
        for _, rule in rules.iterrows():
            antecedents = rule['antecedents'] # a set of items (items that occur together) in context of association rule mining
            for item in antecedents:
                if item in self.resources:
                    recommended_resources.add(self.resources[item])
        
        return list(recommended_resources)
    
# Load your dataset from a CSV file
dataset_path = 'C:/Users/ukary/OneDrive/Masaüstü/user_login/user_login.csv'  
df = pd.read_csv(dataset_path, encoding='windows-1254')

# Create a RecommendationSystem object
rec_system = RecommendationSystem()

# Used associate_resources method to perform association rule mining and make recommendations
recommended_resources = rec_system.associate_resources(df, min_support=0.2, min_confidence=0.5)

print("Recommended Sources:")
for resource in recommended_resources:
    print(resource)

