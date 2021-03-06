import numpy as np
import opfython.utils.logging as l
from opfython.core.sample import Sample

logger = l.get_logger(__name__)


class Dataset:
    """A dataset class to hold multiple instances of samples.

    Properties:
        n_samples (int): number of samples.
        n_classes (int): number of classes.
        n_features (int): number of features.
        samples (np.array): A list of samples.

    Methods:
        _create_samples(n_samples, n_features, verbose): A method that creates a list of samples.
        populate_samples(labels, features): Populates the samples property.

    """

    def __init__(self, n_samples=1, n_classes=1, n_features=10, verbose=0):
        """Initialization method.

        Args:
            n_samples (int): number of samples.
            n_classes (int): number of classes.
            n_features (int): number of features.
            verbose (int): Verbosity level.

        """

        logger.info('Creating class: Dataset.')

        # Number of samples
        self._n_samples = n_samples

        # Number of classes
        self._n_classes = n_classes

        # Number of features
        self._n_features = n_features

        # Creating the samples array
        self._samples = self._create_samples(n_samples, n_features, verbose)

        # We will log some important information
        logger.debug(
            f'Samples: {self._n_samples} | Classes: {self._n_classes} | Features: {self._n_features}.')

        logger.info('Class created.')

    @property
    def n_samples(self):
        """The amount of sampln_samples.
        """

        return self._n_samples

    @property
    def n_classes(self):
        """The amount of classes.
        """

        return self._n_classes

    @property
    def n_features(self):
        """The amount of features.
        """

        return self._n_features

    @property
    def samples(self):
        """A list of samples.
        """

        return self._samples

    @samples.setter
    def samples(self, samples):
        self._samples = samples

    def _create_samples(self, n_samples, n_features, verbose):
        """Creates a samples list.

        Args:
            n_samples (int): Amount of samples.
            n_features (int): Number of features.
            verbose (int): Verbosity level.

        Returns:
            A list of samples.

        """

        logger.debug('Running private method: _create_samples().')

        # Creating an agents list
        samples = []

        # Iterate through number of agents
        for _ in range(n_samples):
            # Appends new agent to list
            samples.append(
                Sample(n_features=n_features, verbose=verbose))

        return samples

    def populate_samples(self, labels, features):
        """Populates the samples property.

        Args:
            labels (list): A list of labels.
            features (list): A list of numpy arrays holding the features.

        """

        logger.debug('Running public method: populate_samples().')

        # We zip everything together and get one by one
        for sample, label, feature_array in zip(self.samples, labels, features):
            # We replace the label for the loaded one
            sample.label = label

            # Also replacing the features array
            sample.features = feature_array
