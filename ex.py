import bridge_principles as bp
from pgmpy.models import BayesianModel
from pgmpy.factors import TabularCPD
from pgmpy.inference import VariableElimination

wet_grass_1 = BayesianModel()
wet_grass_2 = BayesianModel()

propositions_1 = ['R','S','J','T']
propositions_2 = ['R','J','T']

wet_grass_1.add_nodes_from(propositions_1)
wet_grass_1.add_edges_from([('R','J'), ('R','T'), ('S','T')])

wet_grass_2.add_nodes_from(propositions_2)
wet_grass_2.add_edges_from([('R','J'), ('R','T')])

rained_cpd = TabularCPD('R',2,[[0.8],[0.2]])

sprinkler_cpd = TabularCPD('S',2,[[0.9],[0.1]])

jack_cpd = TabularCPD('J',2,
					[[0.8,0],
					[0.2,1]],
					evidence = ['R'],
					evidence_card = [2])

tracy_cpd_1 = TabularCPD('T',2,
					[[1,0.1,0,0],
					[0,0.9,1,1]],
					evidence = ['R','S'],
					evidence_card = [2,2])

tracy_cpd_2 = TabularCPD('T',2,
					[[0.91,0],
					[0.09,1]],
					evidence = ['R'],
					evidence_card = [2])

wet_grass_1.add_cpds(rained_cpd,sprinkler_cpd,jack_cpd,tracy_cpd_1)
wet_grass_2.add_cpds(rained_cpd,jack_cpd,tracy_cpd_2)

inference_1 = VariableElimination(wet_grass_1)
inference_2 = VariableElimination(wet_grass_2)

b1 = bp.possible_belief_sets(propositions_1, wet_grass_1, inference_1)
b2 = bp.possible_belief_sets(propositions_2, wet_grass_2, inference_2)

for belief_set in b1:
	print 'Live Possibilities: %s' % belief_set
	for w in belief_set:
		print '%s: %s' % (w,bp.possible_worlds(propositions_1, wet_grass_1, inference_1)[w])
	print '\n'

for belief_set in b2:
	print 'Live Possibilities: %s' % belief_set
	for w in belief_set:
		print '%s: %s' % (w,bp.possible_worlds(propositions_2, wet_grass_2, inference_2)[w])
	print '\n'
