# Bridge-Principles

The purpose of `bridge_principles.py` is to provide tools for moving from a probabilistic notion of belief to a notion of outright belief. In other words, suppose we know that Mary assigns proposition _p_ probability 0.6 or that Mary's degree of belief in _p_ is 0.6 and want to answer the question, "Does Mary believe _p_?" This script provides one way to do so, based on the proposals in Leitgeb (2013) and Leitgeb (2015).

Probabilistic beliefs are represented here through a [Bayesian Network](https://en.wikipedia.org/wiki/Bayesian_network). All you need to do is set up a Bayesian network to represent an agent's belief state and `possible_belief_sets` will tell you which states of affairs (i.e. which possible worlds) the agent in question can believe are possible according to Leitgeb's proposal.

See `ex.py` for an example. `Example.pdf` provides an explanation of what is illustrated by `ex.py`.

## Dependencies

Here some Python libraries you'll need to have installed to make `bridge_principles.py` work:
* [pandas](http://pandas.pydata.org)
* [numpy](http://www.numpy.org/)
* [pgmpy](http://pgmpy.org)

It will probably be necessary to read through the `pgmpy` documentation to get a handle on how to write Bayesian networks with `pgmpy`. Or just take a look at `ex.py` and modify where necessary.

## References

Leitgeb, Hannes (2013). [Reducing belief simpliciter to degrees of belief](http://www.sciencedirect.com/science/article/pii/S0168007213000845). _Annals of Pure and Applied Logic_, 164(12):1338–1389.

Leitgeb, Hannes (2015). [The Humean thesis on belief](https://www.aristoteliansociety.org.uk/the-joint-session/the-2015-joint-session/hannes-leitgeb-richard-pettigrew/). _Proceedings of the Aristotelian Society Supplementary Volume_, 89(1): 143-185.
