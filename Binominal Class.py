"""
Binominal Class
===============
In this exercise, you'll extend the distributions package with a new class
called Binomial.
Inside the folder called `4a_binomial_package`, you'll find another folder and a
number of files. Here is a description of each
- distributions, which contains the code for the distributions package including
Gaussiandistribution.py and Generaldistribution.py code.
- setup.py a file needed for building python packages with pip
- test.py unit tests to help you debug your code
- numbers.txt and numbers_binomial.txt are data files used as part of the unit
tests
- Binomialdistribution.py and Binomialdistribution_challenge.py choose one of
these files for completing the exercise. Binomialdistribution.py includes more
of the code already set up for you. In Binomialdistribution_challenge.py, you'll
have to write all of the code from scratch. Both files contain instructions with
TODOS to fill out.
Out of all these files, you'll only need to change the following:
- __init__.py inside the distributions folder. You'll need to import the binomial package
- either Binomialdistribution.py or Binomialdistribution_challenge.py You'll also
need to put your Binomialdistribution.py file into the distributions folder.
When you're ready to test out your code, you'll want to pip install your
distributions package and then run the unit tests. In the terminal, assuming you
are in the 4a_binomial_package directory (if not type `cd 4a_binomial_package`),
type `pip install .` into the command line. Then run the unit tests by typing
`python -m unittest test`.
Modify the Binomialdistribution.py code until all the unit tests are passing.
Note that if you change the code in the distributions folder after pip installing
the package, Python will not know about the changes. You'll need to run
`pip install --upgrade .` when you make changes to the package files.
There is also a solution in the 4b_answer_binomial_package. Try not to look at
the solution until your code is passing all of the unit tests.
"""

#distributions/Binomialdistribution.py
import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
    TODO: Fill out all TODOs in the functions below
    """

    #       A binomial distribution is defined by two variables:
    #           the probability of getting a positive outcome
    #           the number of trials

    #       If you know these two values, you can calculate the mean and the standard deviation
    #
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))


    def __init__(self, prob=.5, size=20):

        # TODO: store the probability of the distribution in an instance variable p
        self.p = prob
        # TODO: store the size of the distribution in an instance variable n
        self.n = size

        # TODO: Now that you know p and n, you can calculate the mean and standard deviation
        #       Use the calculate_mean() and calculate_stdev() methods to calculate the
        #       distribution mean and standard deviation [done]
        #
        #       Then use the init function from the Distribution class to initialize the
        #       mean and the standard deviation of the distribution
        #
        #       Hint: You need to define the calculate_mean() and calculate_stdev() methods
        #               farther down in the code starting in line 55.
        #               The init function can get access to these methods via the self
        #               variable.
        mean = self.calculate_mean()
        stdev = self.calculate_stdev()

        super().__init__(mu=mean, sigma=stdev)

    def calculate_mean(self):

        """Function to calculate the mean from p and n
        Args:
            None
        Returns:
            float: mean of the data set
        """

        # TODO: calculate the mean of the Binomial distribution. Store the mean
        #       via the self variable and also return the new mean value

        return self.n * self.p



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        Args:
            None
        Returns:
            float: standard deviation of the data set
        """

        # TODO: calculate the standard deviation of the Binomial distribution. Store
        #       the result in the self standard deviation attribute. Return the value
        #       of the standard deviation.

        stdev =  math.sqrt( self.n * self.p * (1 - self.p) )

        self.stdev = stdev
        return stdev



    def replace_stats_with_data(self):

        """Function to calculate p and n from the data set
        Args:
            None
        Returns:
            float: the p value
            float: the n value
        """

        # TODO: The read_data_file() from the Generaldistribution class can read in a data
        #       file. Because the Binomaildistribution class inherits from the Generaldistribution class,
        #       you don't need to re-write this method. However,  the method
        #       doesn't update the mean or standard deviation of
        #       a distribution. Hence you are going to write a method that calculates n, p, mean and
        #       standard deviation from a data set and then updates the n, p, mean and stdev attributes.
        #       Assume that the data is a list of zeros and ones like [0 1 0 1 1 0 1].
        #
        #       Write code that:
        #           updates the n attribute of the binomial distribution
        #           updates the p value of the binomial distribution by calculating the
        #               number of positive trials divided by the total trials
        #           updates the mean attribute
        #           updates the standard deviation attribute
        #
        #       Hint: You can use the calculate_mean() and calculate_stdev() methods
        #           defined previously.

        self.n = len(self.data)
        self.p = sum(self.data) / self.n

        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n


    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.
        Args:
            None
        Returns:
            None
        """

        # TODO: Use the matplotlib package to plot a bar chart of the data
        #       The x-axis should have the value zero or one
        #       The y-axis should have the count of results for each case
        #
        #       For example, say you have a coin where heads = 1 and tails = 0.
        #       If you flipped a coin 35 times, and the coin landed on
        #       heads 20 times and tails 15 times, the bar chart would have two bars:
        #       0 on the x-axis and 15 on the y-axis
        #       1 on the x-axis and 20 on the y-axis

        #       Make sure to label the chart with a title, x-axis label and y-axis label

        x = self.data
        bins = 2

        n, bins, patches = plt.hist(x, bins)

        plt.xlabel('Sample')
        plt.ylabel('Probability')
        plt.title('Binomial distribution')
        plt.subplots_adjust(left=0.15)

        plt.show()


    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.
        Args:
            k (float): point for calculating the probability density function
        Returns:
            float: probability density function output
        """

        # TODO: Calculate the probability density function for a binomial distribution
        #  For a binomial distribution with n trials and probability p,
        #  the probability density function calculates the likelihood of getting
        #   k positive outcomes.
        #
        #   For example, if you flip a coin n = 60 times, with p = .5,
        #   what's the likelihood that the coin lands on heads 40 out of 60 times?
        binomial_coefficient = math.factorial(self.n)/ (math.factorial(k) * math.factorial(self.n - k))
        probability_density = binomial_coefficient * (self.p ** k) * (1 - self.p) ** (self.n - k)

        return probability_density

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        Args:
            None
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
        """

        # TODO: Use a bar chart to plot the probability density function from
        # k = 0 to k = n

        #   Hint: You'll need to use the pdf() method defined above to calculate the
        #   density function for every value of k.

        #   Be sure to label the bar chart with a title, x label and y label

        #   This method should also return the x and y values used to make the chart
        #   The x and y values should be stored in separate lists

        x = []
        y = []

        # calculate the x values to visualize
        for k in range(self.n):
            x.append(k)
            y.append(self.pdf(k))

        # make the plots
        plt.bar(x, y)
        plt.xlabel('k')
        plt.ylabel(r'$f(k, n, p)')
        plt.title('Binomial Distribution Chart, n {}, p {}'.format(self.n, self.p))
        plt.show()

        return x, y



    def __add__(self, other):

        """Function to add together two Binomial distributions with equal p
        Args:
            other (Binomial): Binomial instance
        Returns:
            Binomial: Binomial distribution
        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise ValueError('p values must be equal')

        # TODO: Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.

        # the try, except statement above will raise an exception if the p values are not equal

        # Hint: You need to instantiate a new binomial object with the correct n, p,
        #   mean and standard deviation values. The __add__ method should return this
        #   new binomial object.

        #   When adding two binomial distributions, the p value remains the same
        #   The new n value is the sum of the n values of the two distributions.

        size_new = self.n + other.n
        return Binomial(size=size_new, prob=self.p)


    def __repr__(self):

        """Function to output the characteristics of the Binomial instance
        Args:
            None
        Returns:
            string: characteristics of the Gaussian
        """

        # TODO: Define the representation method so that the output looks like
        #       mean 5, standard deviation 4.5, p .8, n 20
        #
        #       with the values replaced by whatever the actual distributions values are
        #       The method should return a string in the expected format

        return "mean {}, standard deviation {}, p {}, n {}".format()


#distributions/Generaldistribution.py
class Distribution:

	def __init__(self, mu=0, sigma=1):

		""" Generic distribution class for calculating and
		visualizing a probability distribution.
		Attributes:
			mean (float) representing the mean value of the distribution
			stdev (float) representing the standard deviation of the distribution
			data_list (list of floats) a list of floats extracted from the data file
			"""

		self.mean = mu
		self.stdev = sigma
		self.data = []


	def read_data_file(self, file_name):

		"""Function to read in data from a txt file. The txt file should have
		one number (float) per line. The numbers are stored in the data attribute.
		Args:
			file_name (string): name of a file to read from
		Returns:
			None
		"""

		with open(file_name) as file:
			data_list = []
			line = file.readline()
			while line:
				data_list.append(int(line))
				line = file.readline()
		file.close()

		self.data = data_list


#distribution/__init__.py
from .Gaussiandistribution import Gaussian
from .Binomialdistribution import Binomial


#######
# TESTS
#######
import unittest

from distributions import Gaussian
from distributions import Binomial

class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(25, 2)
        self.gaussian.read_data_file('numbers.txt')

    def test_initialization(self):
        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')
        self.assertEqual(self.gaussian.stdev, 2, 'incorrect standard deviation')

    def test_readdata(self):
        self.assertEqual(self.gaussian.data,\
         [1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31], 'data not read in correctly')

    def test_meancalculation(self):
        self.assertEqual(self.gaussian.calculate_mean(),\
         sum(self.gaussian.data) / float(len(self.gaussian.data)), 'calculated mean not as expected')

    def test_stdevcalculation(self):
        self.assertEqual(round(self.gaussian.calculate_stdev(), 2), 92.87, 'sample standard deviation incorrect')
        self.assertEqual(round(self.gaussian.calculate_stdev(0), 2), 88.55, 'population standard deviation incorrect')

    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.19947,\
         'pdf function does not give expected result')
        self.gaussian.calculate_mean()
        self.gaussian.calculate_stdev()
        self.assertEqual(round(self.gaussian.pdf(75), 5), 0.00429,\
        'pdf function after calculating mean and stdev does not give expected result')

    def test_add(self):
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two

        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)

class TestBinomialClass(unittest.TestCase):
    def setUp(self):
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_data_file('numbers_binomial.txt')

    def test_initialization(self):
        self.assertEqual(self.binomial.p, 0.4, 'p value incorrect')
        self.assertEqual(self.binomial.n, 20, 'n value incorrect')

    def test_readdata(self):
        self.assertEqual(self.binomial.data,\
         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0], 'data not read in correctly')

    def test_calculatemean(self):
        mean = self.binomial.calculate_mean()
        self.assertEqual(mean, 8)

    def test_calculatestdev(self):
        stdev = self.binomial.calculate_stdev()
        self.assertEqual(round(stdev,2), 2.19)

    def test_replace_stats_with_data(self):
        p, n = self.binomial.replace_stats_with_data()
        self.assertEqual(round(p,3), .615)
        self.assertEqual(n, 13)

    def test_pdf(self):
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.07465)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.01235)

        self.binomial.replace_stats_with_data()
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.05439)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.00472)

    def test_add(self):
        binomial_one = Binomial(.4, 20)
        binomial_two = Binomial(.4, 60)
        binomial_sum = binomial_one + binomial_two

        self.assertEqual(binomial_sum.p, .4)
        self.assertEqual(binomial_sum.n, 80)


if __name__ == '__main__':
    unittest.main()
