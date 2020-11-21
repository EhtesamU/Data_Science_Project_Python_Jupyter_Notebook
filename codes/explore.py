import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pylab as plt
from sklearn.feature_selection import RFE
import pandas as pd
from matplotlib.pyplot import figure

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def store_scores_all_models(rmse_list, r2_list, y_expect, y_pred):
    rmse = np.sqrt(mean_squared_error(y_expect, y_pred))
    rmse_list.append(rmse)
    r2 = r2_score(y_expect, y_pred)
    r2_list.append(r2)

def store_scores_one_model(rmse_list, r2_list, mae_list, mape_list, y_expect, y_pred):
    rmse = np.sqrt(mean_squared_error(y_expect, y_pred))
    rmse_list.append(rmse)
    r2 = r2_score(y_expect, y_pred)
    r2_list.append(r2)
    mae = mean_absolute_error(y_expect, y_pred)
    mae_list.append(mae)
    mape = mean_absolute_percentage_error(y_expect, y_pred)
    mape_list.append(mape)

def plot_compare_one_model (rmse_list, r2_list, mae_list, mape_list,heading,names):
    #set width of bar
    barWidth = 0.15
    # Set position of bar on X axis
    bar1 = np.arange(len(rmse_list))
    bar2 = [x + barWidth for x in bar1]
    bar3 = [x + barWidth for x in bar2]
    #bar4 = [x + barWidth for x in bar3]
    figure(figsize=(14, 6))
    # Make the plot
    plt.bar(bar1, rmse_list, color='turquoise', width = barWidth, label='RMSE score')
    plt.bar(bar2, r2_list, color='coral', width = barWidth, label='R2 score')
    plt.bar(bar3, mae_list, color='blue', width = barWidth, label='MAE score')
    #plt.bar(bar4, train_mape_list, color='green', width = barWidth, label='Optimized Model')
    
    # Add xticks on the middle of the group bars
    plt.xlabel(heading, fontweight='bold', fontsize=15)
    plt.ylabel('Score', fontsize=12)
    plt.xticks([r + barWidth for r in range(len(rmse_list))], names, fontsize=12)
    # Create legend & Show graphic
    plt.legend(bbox_to_anchor=(1.15, 1.0), loc='upper right')
    plt.show()

def print_model_score(y_expect, y_pred):
    print("RMSE: ", np.sqrt(mean_squared_error(y_expect, y_pred)))
    print("R2-score: ", r2_score(y_expect, y_pred))
    print("MAE: ", mean_absolute_error(y_expect, y_pred))
    print("MAPE: ", mean_absolute_percentage_error(y_expect, y_pred))
    print()

def plot_compare_features(r2_scores,label_r2, rmse_scores,label_rmse,n_features):
    plt.figure(figsize = (10,5))
    plt.grid()
    plt.xlabel('No. of features selected')
    plt.ylabel('Scores on the test set')
    plt.title('RMSE and R2 score on test set using RFE and CV', fontsize = 18, fontweight = 'bold')
    plt.xticks(np.arange(1, n_features+1, step=1))
    plt.plot(range(1,n_features+1), rmse_scores, marker = 'o', color = 'lightblue', markeredgewidth = 1, markeredgecolor = 'DarkBlue', markerfacecolor = 'None',label=label_rmse)
    plt.plot(range(1,n_features+1), r2_scores, marker = 'o', color = 'red', markeredgewidth = 1, markeredgecolor = 'DarkBlue', markerfacecolor = 'None',label=label_r2)
    plt.legend(loc="best")
    plt.figure(figsize=(12, 6))
    plt.show()

def find_best_combination_index(r2_scores, rmse_scores):
    best_r2_index = r2_scores.index (max(r2_scores))+1
    best_rmse_index = rmse_scores.index(min(rmse_scores))+1
    return best_r2_index, best_rmse_index

def features_ranking(model,n_features, X, y):
    selector = RFE(model, n_features_to_select=n_features, step=1)
    selector = selector.fit(X, y)
    selected_features = pd.DataFrame({'Feature': list(X.columns),'Ranking':selector.ranking_})
    selected_features = selected_features.sort_values(by='Ranking')
    return selected_features