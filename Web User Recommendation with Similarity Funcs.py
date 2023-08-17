from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

class RecommendationSystem:
    def __init__(self):
        # Örnek kaynakları ve ilişkili sayfa verilerini sakla
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
    
    def associate_resources(self, user_logs, min_support=0.02, min_confidence=0.5):
        # Kullanıcının işlem kayıtlarına göre association rule mining ile kaynak önerisi yapma
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

# Kullanıcı işlem kayıtları örneği
user_logs = [
    "0 Admission – orientation info",
    "1 Admission – F1 visa and I20 info Admission",
    "0 Online application - start Admission",
    "1 Online application – step 1",
    "0 Online application – step 2",
    "1 Online application - finish",
    "0 Department main page"
]

# RecommendationSystem sınıfını kullanarak association rule mining ile öneri sistemi oluşturma ve kullanıcıya öneri yapma
rec_system = RecommendationSystem()
recommended_resources = rec_system.associate_resources(user_logs, min_support=0.01, min_confidence=0.2)

# Önerilen kaynakları yazdırma
print("Önerilen Kaynaklar:")
for resource in recommended_resources:
    print(resource)