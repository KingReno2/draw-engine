"""
Create pickled model files
Run this ONCE to initialize models
"""
import pickle
import numpy as np
import os

# Create models directory
os.makedirs('models', exist_ok=True)

# Simple mock model that mimics sklearn interface
class DrawPredictor:
    def predict_proba(self, X):
        # X shape: (n_samples, 6) - [team_draw, opp_draw, league_str, past_5_norm, opp_past_5_norm, home_adv]
        n_samples = X.shape[0]
        results = []
        
        for i in range(n_samples):
            team_draw = X[i][0]
            opp_draw = X[i][1]
            league_str = X[i][2]
            past_form = X[i][3]
            opp_form = X[i][4]
            home_adv = X[i][5]
            
            # Calculate draw probability
            base = 0.24
            draw_prob = (base + 
                        (team_draw + opp_draw) * 0.15 +
                        (past_form + opp_form) / 2 * 0.1 +
                        (league_str - 0.85) * 0.15 +
                        home_adv * 0.1)
            
            draw_prob = max(0.05, min(0.45, draw_prob))
            results.append([1 - draw_prob, draw_prob])
        
        return np.array(results)

class SimpleScaler:
    def transform(self, X):
        # Simple normalization
        return (X - np.array([0.25, 0.25, 0.87, 0.4, 0.4, 0.0])) / np.array([0.08, 0.08, 0.03, 0.2, 0.2, 0.1])

# Save models
try:
    model = DrawPredictor()
    scaler = SimpleScaler()
    
    with open('models/draw_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    with open('models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    print("✅ Models saved successfully!")
except Exception as e:
    print(f"Error saving models: {e}")
