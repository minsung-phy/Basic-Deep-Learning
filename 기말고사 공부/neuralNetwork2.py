import numpy as np
import math

class neuralNetwork:
    bih = 0.30
    bho = 0.60
    eta = 0.50

    def __init__(self, wih, who):
        self.wih = wih
        self.who = who
        self.sig = lambda x: 1 / (1 + pow(math.e, -x))
        self.sigp = lambda x: pow(math.e, -x) / (1 + pow(math.e, -x)) ** 2
        pass

    def train(self, inputs_list, targets_list):
        inputs = np.array(inputs_list, ndmin = 2).T
        targets = np.array(targets_list, ndmin = 2).T
        hidden_inputs = np.dot(self.wih, inputs) + self.bih * np.ones((2, 1))
        hidden_outputs = self.sig(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_outputs) + self.bho * np.ones((2, 1))
        final_outputs = self.sig(final_inputs)

        output_errors = final_outputs - targets
        a = np.dot((output_errors * self.sigp(final_inputs)).T, self.who).T
        dEdw_ih = a * self.sigp(hidden_inputs) * inputs.T
        dEdw_ho = output_errors * self.sigp(final_inputs) * hidden_outputs.T

        self.wih -= self.eta * dEdw_ih
        self.who -= self.eta * dEdw_ho

        pass

    def query(self, inputs_list):
        inputs = np.array(inputs_list, ndmin = 2).T
        hidden_inputs = np.dot(self.wih, inputs) + self.bih * np.ones((2, 1))
        hidden_outputs = self.sig(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_outputs) + self.bho * np.ones((2, 1))
        final_outputs = self.sig(final_inputs)
        return final_outputs

wih = np.array([[0.15, 0.20], [0.25, 0.30]])
who = np.array([[0.40, 0.45], [0.50, 0.55]])
n = neuralNetwork(wih, who)
inputs_list = [0.05, 0.10]
targets_list = [0.01, 0.99]

i = 0
while i < 10000:
    n.train(inputs_list, targets_list)
    i += 1

outputs = n.query(inputs_list)
print(outputs)