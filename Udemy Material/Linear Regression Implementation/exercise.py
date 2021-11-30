#YOU CAN ONLY ADD IMPORTS THAT HELP WITH HANDLING READING IN OF DATA
import numpy as np

def read_profit_data():
    """
    This function should read the data from "profit_dataset.txt"
    into two numpy arrays (one numpy array for the population and one numpy array for 
    the corresponding profit)
    
    """
    
    ### YOUR CODE HERE #########
    raise NotImplementedError("Did not implement read_profit_data() function")
    ############################

def build_linear_regression_profit():
    """
    Now that you are able to read in the profit dataset, 
    build a linear regression model to predict profit given the population
    
    Form of linear regression: y = a + bx
    
    Hint: we want to find the least squares fit (ie: minimize the sum of squared error between predicted output and 
    ground truth output). You should be able to use numpy to build a linear system to solve for the coefficients
    a and b
    
    Your function should return the coefficients a and b in that order!
    """
    
    ### YOUR CODE HERE #########
    raise NotImplementedError("Did not implement build_linear_regression_profit()")
    ############################

def build_polynomial_regression_profit(degree):
    """
    It seems like our linear regression model might be a bit too simplistic.
    Let's add a bit of complexity by building a polynomial regression model of degree d
    
    Form: y = a_1 + a_2x + a_3x^2 + ... a_dx^{d-1} + a_{d+1}x^{d}
    
    Hint: similar approach to build_linear_regression_profit() function. You need to find a way to 
    turn the the polynomial regression problem into a linear system. Solve for the coefficients 
    a_1, a_2, ... a_{d}, a_{d+1}
    
    Your function should return the coefficients a_{1}, a_{2}, ... a_{d}, a_{d+1} in that order
    """
    ### YOUR CODE HERE #########
    raise NotImplementedError("Did not implement the build_polynomial_regression_profit() function")
    ############################

def get_predictions_linear_regresssion_profit():
    """
    Given that you can get linear regression model coefficients, 
    return a vector of the predicted profit
    """
    ### YOUR CODE HERE #########
    raise NotImplementedError("Did not implement the get_predictions_linear_regression_profit() function")
    ############################
    
def get_predictions_polynomial_regression_profit(degree):
    """
    Given that you can get polynomial regression model coefficients (degree d), 
    return a vector of the predicted profits corresponding to each input population
    """
    ### YOUR CODE HERE #########
    raise NotImplementedError("Did not implement get_predictions_polynomial_regression_profit() function")
    ############################
def calculate_mean_squared_error_linear_regression():
    """
    Now that you are able to get your predicted_values from linear regression,
    calculate the mean squared error between the predicted value for profit and ground truth profit
    
    """
    
    ### YOUR CODE HERE #########
    raise NotImplementedError("Did not implement calculate_mean_squared_error_linear_regression() function")
    ############################
    
def calculate_mean_squared_error_polynomial_regression(degree):
    """
    Now that you are able to get your predicted_values from polynomial regression (degree d),
    calculate the mean squared error between the predicted value for profit and ground truth profit
    
    """
    
    ### YOUR CODE HERE #########
    raise NotImplementedError("Did not implement calculate_mean_squared_error_polynomial_regression() function")
    ############################


def gradient_descent_linear_regression(num_iterations, population, profit, learning_rate):
    """
    An iterative way to find the coefficients a,b for y = a + bx linear regression model
    is through a technique called gradient descent. 
    
    Gradient descent for linear regression uses the Mean Squared Error (MSE) function to update the values for a, b coefficients
    over n iterations in order to minimize the Mean Squared Error. 
    
    Your job is to implement gradient descent for linear regression. Return format should be in a numpy array
    
    Hint: MSE = 1/n * sum((truth - predicted)^2). You sum across all rows of the dataset
    
    Good starting point: How do you calculate "predicted" in the case of the y = a + bx linear regression model. 
    
    Learning Rate: How drastic do you update the coefficients a, b in the model (this ties in with convergence rate to the 
    optimal values)
    """
    
    ###### YOUR CODE HERE ######
    raise NotImplementedError("Need to implement gradient_descent_linear_regression() function")
    ############################

def mse_below_five_k():
    """
    OPTIONAL PROBLEM:
    -----------------
    Your goal is to train either a linear regression or polynomial regression model
    and have the mean squared error below $5000 dollars. You as the CEO somehow can tolerate
    being off by $5000 when trying to expand your restaurant chain.
    
    Hint: your profit is reported in $10000s, so  what should your target/threshold mean
    squared error be?
    
    return the mean squared error you acheive
    
    """
    
    ############# YOUR CODE HERE ##########
    raise NotImplementedError("Need to implement mse_below_five_k() function")
    #######################################
    
