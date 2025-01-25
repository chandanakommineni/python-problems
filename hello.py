import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import matplotlib.pyplot as plt

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the dataset (scale pixel values to 0-1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build a simple neural network model
model = Sequential([
    Flatten(input_shape=(28, 28)),      # Convert 2D images to 1D vectors
    Dense(128, activation='relu'),      # Hidden layer with 128 neurons
    Dense(10, activation='softmax')     # Output layer with 10 neurons (one for each digit)
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_accuracy:.4f}")

# Make predictions on the test set
predictions = model.predict(x_test)

# Visualize some example results
for i in range(5):  # Show 5 test images and their predictions
    plt.imshow(x_test[i], cmap='gray')  # Display the image in grayscale
    plt.title(f"Actual: {y_test[i]}, Predicted: {predictions[i].argmax()}")
    plt.axis('off')  # Hide axes
    plt.show()
