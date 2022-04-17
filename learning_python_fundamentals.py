'''
Created on Apr 15, 2022

@author: marklagatuz
'''
import pandas as pd
import numpy as np

def learning_python_1():

    this_is_a_list = []
    print(type(this_is_a_list))
    print(this_is_a_list)
    
    this_is_a_panda_series = pd.Series([87, 100, 94])
    print(type(this_is_a_panda_series))
    print(this_is_a_panda_series)
    
    #this_is_a_numpy_array = 
    
    this_is_an_integer = 101
    print(type(this_is_an_integer))
    print(this_is_an_integer)
    
    #this_is_a_numpy_array = 
    
    print(this_is_a_panda_series[1])
    print(this_is_a_panda_series.describe())
    
    this_is_a_panda_series = pd.Series([87, 100, 94], index=['Java', 'Python', 'CPlusPlus'])
    print(type(this_is_a_panda_series))
    print(this_is_a_panda_series)
    
    this_is_a_dictionary = {'Java':87, 'Python':100, 'CPlusPlus':94}
    print(type(this_is_a_dictionary))
    print(this_is_a_dictionary)
    
    this_is_a_panda_series1 = pd.Series(this_is_a_dictionary)
    print(type(this_is_a_panda_series1))
    print(this_is_a_panda_series1)
    
    print('')
    print(type(this_is_a_panda_series1.Python))
    print(this_is_a_panda_series1.Python)
    print(type(this_is_a_panda_series1.values))
    print(this_is_a_panda_series1.values)
    
    print('')
    computer_languages = pd.Series(['Python', 'Java', 'CPlusPlus'])
    print(type(computer_languages))
    print(computer_languages)
    print(computer_languages.str.contains('on'))
    
def learning_python_2():

    my_list = [2,3,5,7,9,11]
    this_is_an_np_array = np.array(my_list)
    print(type(my_list))
    print(my_list)
    print(type(this_is_an_np_array))
    print(this_is_an_np_array)
    
    this_is_a_list_1 = [1,2,3]
    this_is_a_list_2 = [4,5,6]
    print(this_is_a_list_1)
    print(this_is_a_list_2)
    np_array_2d = np.array([this_is_a_list_1,this_is_a_list_2])
    print(type(np_array_2d))
    print(np_array_2d)
    
    print(np_array_2d.dtype)
    list_floats = [0.0,0.1,0.2,0.3,0.4]
    print(np_array_2d.ndim)
    print(np_array_2d.shape)
    np_array_floats = np.array(list_floats)
    print(np_array_floats.ndim)
    print(np_array_floats.shape)
    print(np_array_floats.dtype)
    print(np_array_2d.size)
    print(np_array_floats.size)
    print(np_array_floats.itemsize)
    
    all_ones = np.ones((2,4), dtype=int) #dtype optional
    print(all_ones)
    all_zeros = np.zeros(5)
    print(all_zeros)
    full_array = np.full((3,5), 1300, dtype=float)
    print(full_array)
    
    my_np_range = np.arange(5, dtype=float)
    print(my_np_range)
    my_np_range_1 = np.arange(10, 1, -2)
    print(my_np_range_1)
    my_np_linspace = np.linspace(0.0, 1.0, num=20)
    print(my_np_linspace)
    my_np_reshape = np.arange(1, 21).reshape(5,4)
    print(my_np_reshape)
    
    list_of_numbers1 = np.arange(1, 7) * 10
    print(list_of_numbers1)
    list_of_numbers2 = list_of_numbers1.reshape(2, 3)
    print(list_of_numbers2)
    list_of_numbers3 = np.array([2,4,6])
    print(list_of_numbers3)
    print(list_of_numbers2 * list_of_numbers3)
    
learning_python_1()
learning_python_2()