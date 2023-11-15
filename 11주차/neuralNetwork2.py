import numpy
import math

# neural network class definition
class neuralNetwork:
    # weight of bias
    bih = 0.35
    bho = 0.60
    
    # learning rate
    eta = 0.5

    # initialise the neural network
    def __init__(self, wih, who):
        # link weights
        self.wih = wih
        self.who = who
        
        # sigmoid function
        self.sig = lambda x: 1/(1+pow(math.e,-x))

        # derivative of sigmoid function
        self.sigp = lambda x: pow(math.e,-x) / (1 + pop(math.e, -x)) ** 2

        pass

    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs) + self.bih * numpy.ones((2, 1))

        # calculate the signals emerging form hidden layer
        hidden_outputs = selg.sig(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs) + self.bho * numpy.ones((2, 1))

        # calculate the signals emerging form final output layer
        final_outputs = self.sig(final_inputs)

        # partial derivative of E with respect to weight
        output_errors = final_outputs - targets
        a = np.dot((output_errors*self.sigp(final_inputs)).T,self.who).T
        dEdw_ih = a*self.sigp(hidden_inputs)*inputs.T
        dEdw_ho = output_errors*self.sigp(final_inputs)*hidden_outputs.T

        # update the weights for the links between the hidden and output layers
        self.wih -= self.eta*dEdw_ih

        # update the weights for the links between the input and hidden layers
        self.who -= self.eta*dEdw_ho

        pass

    def query(self,inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        hidden_inputs = np.dot(self.wih, inputs)+self.bih*np.ones((2,1))
        hidden_outputs = self.sig(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_outputs)+self.bho*np.ones((2,1))
        final_outputs = self.sig(final_inputs)

        return final_outputs

wih = numpy.array([[0.15,0.20],[0.25,0.30]])
who = numpy.array([[0.40,0.45],[0.50,0.55]])
n = neuralNetwork(wih, who)
inputs_list = [0.05,0.10]
targets_list = [0.01,0.99]

#train
i = 0

while i<10000:
  n.train(inputs_list,targets_list)
  i += 1

outputs = n.query(inputs_list)

print(outputs)
