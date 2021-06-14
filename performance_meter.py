import numpy as np
import libs.emetrics as emetrics
from utils import save_metrics
from data_loader import binarize_score
from data_loader import DATASETS_TO_PREPROCESS
from sklearn.metrics import mean_squared_error as sk_mse

def calc_accuracy(y_test, predictions):
    counter = 0
    for i in range(y_test.shape[0]):
        if y_test[i] == predictions[i]:
            counter += 1
    return round(counter * 100 / y_test.shape[0], 3), counter

def calc_mean_squared_error(y_test, predictions):
    sum = 0
    for i in range(y_test.shape[0]):
        sum += pow((y_test[i] - predictions[i]), 2)
    return round(sum / y_test.shape[0], 3)

def finalize_results(y_test, predictions):
    temp_y_test = []
    temp_predictions = []
    for i in range(y_test.shape[0]):
        temp_predictions.append(np.argmax(predictions[i]))
        temp_y_test.append(np.argmax(y_test[i]))
    return np.array(temp_y_test), np.array(temp_predictions)

def binarize_results(dataset_name, Y):
    threshold = 7.0 if dataset_name in DATASETS_TO_PREPROCESS else 12.1
    return np.array([binarize_score(y, threshold) for y in Y])

def measure_and_print_performance(model_name, dataset_name, y_test, predictions):
    print('Measuring performance...')
    binary_y_test = binarize_results(dataset_name, y_test)
    binary_predictions = binarize_results(dataset_name, predictions)

    print('Calculating CI...')
    ci_em = round(emetrics.get_cindex(y_test, predictions), 3)
    print('Calculating R2M...')
    r2m_em = round(emetrics.get_rm2(y_test, predictions), 3)
    print('Calculating AUPR...')
    aupr_em = round(emetrics.get_aupr(binary_y_test, binary_predictions), 3)
    print('Calculating MSE...')
    mse_sk = round(sk_mse(y_test, predictions), 3)

    metrics = { 'ci': ci_em, 'r2m': r2m_em, 'aupr': aupr_em, 'mse': mse_sk }
    save_metrics(model_name, dataset_name, metrics)

    print(f'{model_name} ({dataset_name} dataset):')
    print(f'\tConcordance Index: {ci_em}')
    print(f'\tMean Squared Error: {mse_sk}')
    print(f'\tr2m: {r2m_em}')
    print(f'\tAUPR: {aupr_em}')
