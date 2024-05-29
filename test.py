import numpy as np
from sklearn.metrics import accuracy_score
from ensemblePredict import opModel, model, modelEns
# Import preprocess functions and test data if necessary

# Load test data
test_data = np.load('ensemblePredict.npy')
true_labels = np.load('ensemblePredict.npy')

# Preprocess test data if necessary
# preprocessed_test_data = preprocess_test_data(test_data)

# Make predictions using each model
opModel_predictions = opModel.predict(test_data)
model_predictions = model.predict(test_data)
modelEns_predictions = modelEns.predict(test_data)

# Calculate accuracy for each model
opModel_accuracy = accuracy_score(true_labels, opModel_predictions)
model_accuracy = accuracy_score(true_labels, model_predictions)
modelEns_accuracy = accuracy_score(true_labels, modelEns_predictions)

# Print or visualize the accuracy metrics
print("Opcode Model Accuracy:", opModel_accuracy)
print("Strings as Greyscale Model Accuracy:", model_accuracy)
print("Ensemble Model Accuracy:", modelEns_accuracy)
