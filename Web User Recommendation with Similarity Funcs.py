from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

class RecommendationSystem:
    def __init__(self):
        # Store sample resources and associated page data
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
    def preprocess_data(self, user_logs):
        transactions = [log.split(".")[0].strip() for log in user_logs]
        return pd.DataFrame(transactions)
    
    def associate_resources(self, user_logs, min_support=0.14, min_confidence=0.5): 
        #Let's suppose that we want rules for only those sites that logins are at least 1 times a week, so 1/7 = 0,14, since my dataset is for a one-week time period.
        # Making resource suggestions with association rule mining according to the user's transaction records
        data = self.preprocess_data(user_logs)
        
        # Create transactions with multiple items
        transactions = [log.split(".")[0].strip().split() for log in user_logs]

        # Convert transactions to a pandas DataFrame
        transactions_df = pd.DataFrame(transactions) 

        frequent_itemsets = apriori(transactions_df, min_support=min_support, use_colnames=True)
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
            
        recommended_resources = set()
        for _, rule in rules.iterrows():
            antecedents = rule['antecedents']
            for item in antecedents:
                if item in self.resources:
                    recommended_resources.add(self.resources[item])
        return list(recommended_resources)

# user_log examples
user_logs = [
    "0. Admission – orientation info",
    "1. Admission – F1 visa and I20 info Admission",
    "0. Online application - start Admission",
    "1. Online application – step 1",
    "0. Online application – step 2",
    "1. Online application - finish",
    "0. Department main page"
]

# Created a recommendation system with association rule mining using the RecommendationSystem class and making recommendations to the user
rec_system = RecommendationSystem()
recommended_resources = rec_system.associate_resources(user_logs, min_support=0.01, min_confidence=0.2)

print("Önerilen Kaynaklar:")
for resource in recommended_resources:
    print(resource)
