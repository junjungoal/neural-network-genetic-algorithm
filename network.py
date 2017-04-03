"""Class that represents the network to be evolved."""
import random
from train import train_and_score

class Network():
    """Represent a network and let us operate on it.

    Currently only works for an MLP.
    """

    def __init__(self, nn_param_choices):
        """Initialize our network.

        Args:
            nn_param_choices (dict): Parameters for the network, includes:
                neuron_choices (list): [64, 128, 256]
                max_layers (list): [1, 2, 3, 4]
                activation (list): ['relu', 'elu']
                optimizer (list): ['rmsprop', 'adam']
        """
        self.accuracy = 0.
        self.nn_param_choices = nn_param_choices
        self.network = {}  # (dic): represents MLP network parameters

    def create_random(self):
        """Create a random network."""
        for key in self.nn_param_choices:
            self.network[key] = random.choice(self.nn_param_choices[key])

    def create_set(self, network):
        """Set network properties.

        Args:
            network (list): List of neurons per layer.

        """
        self.network = network

    def train(self):
        """Train the network and record the accuracy."""
        if self.accuracy == 0.:
            self.accuracy = train_and_score(self.network)

    def print(self):
        """Print out a network."""
        print(self.network)
        print("Network accuracy: %.2f%%" % (self.accuracy * 100))
