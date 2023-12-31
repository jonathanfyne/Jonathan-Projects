from datetime import datetime
from csv import DictReader
from math import exp, log, sqrt

# Parameters For The File
train_file = 'train.csv'  # Path to the training file
test_file = 'test.csv'    # Path to the testing file

num_weights = 2 ** 20   # Number of weights used for learning
learning_rate = 0.1    # Learning rate for SGD optimization

def calculate_logloss(predicted_prob, true_label):
    predicted_prob = max(min(predicted_prob, 1.0 - 1e-12), 1e-12)
    return -log(predicted_prob) if true_label == 1 else -log(1.0 - predicted_prob)

def hash_csv_row(csv_row, max_index):
    indices = [0]  # 0 is the index of the bias term
    for key, value in csv_row.items():
        index = int(value + key[1:], 16) % max_index
        indices.append(index)
    return indices

def estimate_probability(features, weights):
    weighted_sum = 0.0
    for i in features:
        weighted_sum += weights[i] * 1.0
    return 1.0 / (1.0 + exp(-max(min(weighted_sum, 20.0), -20.0)))

def update_model(weights, counts, features, prediction, true_label):
    for i in features:
        adaptive_learning_rate = learning_rate / (sqrt(counts[i]) + 1)
        gradient = (prediction - true_label) * 1.0  # In our case, x[i] is always 1
        weights[i] -= gradient * adaptive_learning_rate
        counts[i] += 1
    return weights, counts

# Training and Testing

# Declared to Number and Count the Amount of Items
total_items = 0
total_data = 0.0

# Initializes the model
model_weights = [0.0] * num_weights
feature_counts = [0.0] * num_weights

# Trains a logistic regression model using one-pass SGD
total_loss = 0.0
for t, row in enumerate(DictReader(open(train_file))):
    true_label = 1.0 if row['Label'] == '1' else 0.0

    del row['Label']
    del row['Id']

    # Items Within The Rows of The Document
    num_items = len(row)

    # Calculate the Sum of Data in the Current Row
    row_data_sum = sum(float(value) for value in row.values())

    # Operation for counting items and data statistics
    total_items += num_items
    total_data += row_data_sum

    # Step 1: Gets features and line 67 does gets the predictions
    feature_indices = hash_csv_row(row, num_weights)
    prediction = estimate_probability(feature_indices, model_weights)

    # For progress validation
    total_loss += calculate_logloss(prediction, true_label)
    if t % 1000000 == 0 and t > 1:
        print('%s\tProcessed Information: %d\tCurrent Logloss: %f' % (
            datetime.now(), t, total_loss / t))

#Model weight and feature counts are inserted with updates from the code
    model_weights, feature_counts = update_model(model_weights, feature_counts, feature_indices, prediction, true_label)

# The statistics of the item and data are outputted
average_items_per_row = total_items / (t + 1)
average_data_per_row = total_data / (t + 1)
print(f'Average number of items per row: {average_items_per_row}')
print(f'Average data per row: {average_data_per_row}')

# Testing and Saving predictions
with open('TestPredictions.csv', 'w') as predictions_file:
    predictions_file.write('Id,Predicted\n')
    for t, row in enumerate(DictReader(open(test_file))):
        Id = row['Id']
        del row['Id']
        feature_indices = hash_csv_row(row, num_weights)
        prediction = estimate_probability(feature_indices, model_weights)
        predictions_file.write('%s,%f\n' % (Id, prediction))
