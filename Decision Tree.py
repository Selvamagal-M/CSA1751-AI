import subprocess
import sys

# Step 1: Force Install dependencies
try:
    from sklearn.tree import DecisionTreeClassifier, export_text
    import pandas as pd
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scikit-learn", "pandas"])
    from sklearn.tree import DecisionTreeClassifier, export_text
    import pandas as pd

# Step 2: Data
data = {
    'Outlook': [0, 0, 1, 2, 2, 2, 1, 0, 0, 2, 0, 1, 1, 2],
    'Temp': [0, 0, 0, 1, 2, 2, 2, 1, 2, 1, 1, 1, 0, 1],
    'Play': [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]
}

df = pd.DataFrame(data)
X = df[['Outlook', 'Temp']]
y = df['Play']

# Step 3: Logic
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)

# Step 4: Display Output
print("\n--- RESULTS ---")
print(export_text(clf, feature_names=['Outlook', 'Temp']))
print("\n--- DONE ---")

# Step 5: Keep window alive
input("Press Enter to close this window...")
