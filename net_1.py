from numpy import exp, array, random, dot
import numpy as np

class NeuralNetwork():
    def __init__(self):
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs.
        random.seed(1)

        # n-1 is no of features
        # We model a single neuron, with n-1 input connections and 1 output connection.
        # We assign random weights to a n-1 x 1 matrix, with values in the range -1 to 1
        # and mean 0.


        filename = "data.txt"

        file = open(filename, "r")
        for line in file:
            l = line.strip('\n')
            L = l.split(" ")
            n = len(L)

        self.synaptic_weights = 2 * random.random((n-1, 1)) - 1

    # The Sigmoid function, which describes an S shaped curve.
    # We pass the weighted sum of the inputs through this function to
    # normalise them between 0 and 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.

    def setTrainingInput(self):
        # The training set. We have 4 examples, each consisting of 3 input values
        # and 1 output value.
        filename = "data.txt"

        file = open(filename, "r")
        training_set_inputs = []

        for line in file:
            l = line.strip('\n')
            L = l.split(" ")
            n = len(L)
            featureVec = []
            for i in range(n - 1):
                featureVec.append(int(L[i]))

            training_set_inputs.append(featureVec)
        training_set_inputs = array(training_set_inputs)

        return training_set_inputs


    def setTrainingOutput(self):
        # The training set. We have 4 examples, each consisting of 3 input values
        # and 1 output value.
        training_set_outputs = []
        filename = "data.txt"

        file = open(filename, "r")

        outputVec = []
        for line in file:
            l = line.strip('\n')
            L = l.split(" ")
            n = len(L)
            outputVec.append(int(L[n - 1]))


        training_set_outputs.append(outputVec)
        training_set_outputs = array(training_set_outputs).T
        return training_set_outputs


    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            # Pass the training set through our neural network (a single neuron).
            output = self.think(training_set_inputs)

            # Calculate the error (The difference between the desired output
            # and the predicted output).
            error = training_set_outputs - output

            # Multiply the error by the input and again by the gradient of the Sigmoid curve.
            # This means less confident weights are adjusted more.
            # This means inputs, which are zero, do not cause changes to the weights.
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # Adjust the weights.
            self.synaptic_weights += adjustment

    # The neural network thinks.
    def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
        return self.__sigmoid(dot(inputs, self.synaptic_weights))




if __name__ == "__main__":

    #Intialise a single neuron neural network.
    neural_network = NeuralNetwork()

    print "Random starting synaptic weights: "
    print neural_network.synaptic_weights

    # The training set. We have 4 examples, each consisting of 3 input values
    # and 1 output value.

    # Train the neural network using a training set.
    # Do it 10,000 times and make small adjustments each time.

    neural_network.train(neural_network.setTrainingInput(), neural_network.setTrainingOutput(), 10000)

    print "New synaptic weights after training: "
    print neural_network.synaptic_weights

    # Test the neural network with a new situation.
    print "Considering new situation [0, 1, 1, 1] -> ?: "
    print round(neural_network.think(array([0, 1, 1, 1])))



