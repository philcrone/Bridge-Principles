import itertools
import copy
import pandas as pd
import numpy as np
from pgmpy.models import BayesianModel
from pgmpy.factors import TabularCPD
from pgmpy.inference import VariableElimination

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def is_consistent(b, inf):
	poset = powerset(b.keys())
	for s in poset:
		if s != () and s != tuple(b.keys()):
			diff = list(set(b.keys()) - set(s))
			evidence = {}
			for p in s:
				evidence[p] = b[p]
			phi_query = inf.query(variables = diff, evidence = evidence)
			for p in phi_query:
				if not phi_query[p].values[b[p]] > 0.:
					return False
	return True

def joint_prob (truth_values, mod, inf):
	if len(truth_values.keys()) == 1:
		p = truth_values.keys()[0]
		phi_query = inf.query(variables = [p],evidence=None)
		return phi_query[p].values[truth_values[p]]
	else:
		variable = truth_values.keys()[0]
		evidence = {}
		for p in set(truth_values.keys()) - set([variable]):
			evidence[p] = truth_values[p]
		phi_query = inf.query(variables = [variable],evidence=evidence)
		return phi_query[variable].values[truth_values[variable]] * joint_prob(evidence, mod, inf)

def possible_worlds (propositions, mod, inf):
	worlds = {}
	truth_values = itertools.product([0,1],repeat = len(propositions))
	i = 1
	for value in truth_values:
		world_name = 'w%s' % i
		prop_set = dict(zip(propositions,value))
		if is_consistent(prop_set, inf):
			worlds[world_name] = prop_set
			worlds[world_name]['prob'] = joint_prob(prop_set, mod, inf)
			i += 1
	return worlds

def sort(array):
    """Quicksort implementation"""
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0][1]
        for x in array:
            if x[1] < pivot:
                less.append(x)
            if x[1] == pivot:
                equal.append(x)
            if x[1] > pivot:
                greater.append(x)
        return sort(greater)+equal+sort(less)
    else:
        return array

def possible_belief_sets (propositions, mod, inf):
	worlds = possible_worlds(propositions, mod, inf)
	world_probs = []
	for w in worlds:
		world_probs.append((w,worlds[w]['prob']))
	world_probs = sort(world_probs)

	belief_sets = []
	temp_set = []
	for w in world_probs:
		temp_set.append(w[0])
		if w[1] > sum([v[1] for v in world_probs[world_probs.index(w) + 1:]]):
			belief_sets.append(copy.copy(temp_set))
	return belief_sets
