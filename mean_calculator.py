from multiprocessing.sharedctypes import Value
import numpy as np

def calculate (list):
    # If list is less than 9 numbers than will return Error value
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    else:
        nums = {}
        x = np.array([list[0:3], list[3:6], list[6:9]])
    
        # Adding mean values to dictionary(Axis 0 first, axis 1 second, flattened third)
        nums['mean'] = []
        nums['mean'].append(np.mean(x,axis=0).tolist())
        nums['mean'].append(np.mean(x,axis=1).tolist())
        nums['mean'].append(np.mean(x))

        # Adding variance values to dictionary(Axis 0 first, axis 1 second, flattened third)
        nums['variance'] = []
        nums['variance'].append(np.var(x,axis=0).tolist())
        nums['variance'].append(np.var(x,axis=1).tolist())
        nums['variance'].append(np.var(x))

        # Adding standard deviation values to dictionary(Axis 0 first, axis 1 second, flattened third)
        nums['standard deviation'] = []
        nums['standard deviation'].append(np.std(x,axis=0).tolist())
        nums['standard deviation'].append(np.std(x,axis=1).tolist())
        nums['standard deviation'].append(np.std(x))

        # Adding max values to dictionary(Axis 0 first, axis 1 second, flattened third)
        nums['max'] = []
        nums['max'].append(np.max(x,axis=0).tolist())
        nums['max'].append(np.max(x,axis=1).tolist())
        nums['max'].append(np.max(x))

        # Adding min values to dictionary(Axis 0 first, axis 1 second, flattened third)
        nums['min'] = []
        nums['min'].append(np.min(x,axis=0).tolist())
        nums['min'].append(np.min(x,axis=1).tolist())
        nums['min'].append(np.min(x))

        # Adding sum values to dictionary(Axis 0 first, axis 1 second, flattened third)
        nums['sum'] = []
        nums['sum'].append(np.sum(x,axis=0).tolist())
        nums['sum'].append(np.sum(x,axis=1).tolist())
        nums['sum'].append(np.sum(x))

        return nums
    
print(calculate([0,1,2,3,4,5,6,7,8]))