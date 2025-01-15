from text_parser import TextParser
from textToTree import TreeConverter
from document import Document
from link import Link
from linknature import LinkNature
from node import Node
from tree import Tree


parser = TextParser()
#Uses a '. ' as the split at the moment, should be converted

text = '''Bali is predominantly a Hindu country. 
Bali is known for its elaborate, traditional dancing. 
The dancing is inspired by its Hindi beliefs. 
Most of the dancing portrays tales of good versus evil. 
To watch the dancing is a breathtaking experience. 
Lombok has some impressive points of interest - the majestic Gunung Rinjani is an active volcano. 
It is the second highest peak in Indonesia. 
Art is a Balinese passion. 
Batik paintings and carved statues make popular souvenirs. 
Artists can be seen whittling and painting on the streets, particularly in Ubud. 
It is easy to appreciate each island as an attractive tourist destination. 
Majestic scenery; rich culture; white sands and warm, azure waters draw visitors like magnets every year. 
Snorkelling and diving around the nearby Gili Islands is magnificent. 
Marine fish, starfish, turtles and coral reef are present in abundance. 
Bali and Lombok are part of the Indonesian archipelago. 
Bali has some spectacular temples. 
The most significant is the Mother Temple, Besakih. 
The inhabitants of Lombok are mostly Muslim with a Hindu minority. 
Lombok remains the most understated of the two islands. 
Lombok has several temples worthy of a visit, though they are less prolific. 
Bali and Lombok are neighbouring islands.
Bali and Lombok are neighbouring islands both are part of the Indonesian archipelago. 
It is easy to appreciate each island as an attractive tourist destination majestic scenery; rich culture; white sands and warm, azure waters draw visitors like magnets every year. 
Snorkelling and diving around the nearby Gili Islands is magnificent, with marine fish, starfish, turtles and coral reef present in abundance. 
Whereas Bali is predominantly a Hindu country, the inhabitants of Lombok are mostly Muslim with a Hindu minority. 
Bali is known for its elaborate, traditional dancing which is inspired by its Hindi beliefs. 
Most of the dancing portrays tales of good versus evil; to watch it is a breathtaking experience. 
Art is another Balinese passion batik paintings and carved statues make popular souvenirs. 
Artists can be seen whittling and painting on the streets, particularly in Ubud. 
The island is home to some spectacular temples, the most significant being the Mother Temple, Besakih. 
Lombok, too, has some impressive points of interest the majestic Gunung Rinjani is an active volcano and the second highest peak in Indonesia. 
Like Bali, Lombok has several temples worthy of a visit, though they are less prolific. 
Lombok remains the most understated of the two islands. '''


text = '''
In the far distant future, The sea levels have risen and humanity has hit an all time low. 
The United Kingdom has fallen apart, and England has now become New World England, separated into four districts. 
With the loss of most of the major cities , the new capital is located in NAME, in the north district. 
The living conditions have also decreased, with the sky nearly always covered by smog, And the ground always dirty. 
Despite originally seeming like an advancement, infrastructure has become an invasive force, with nearly the entire country now shadowed over by construction and artificial environments. 
There isn't a plant in sight, and the only source of food are artificially grown fruit & veg in overworked facilities, and the fish that can now be more easily caught due to the flooding, and now that the natural oxygen supply is low, and the average human lifespan has dropped significantly. 
This put a stress on humans as their competitors, a humanoid reptilian species known as vendrent, were able to survive in the harsh conditions.
In an attempt to perpetuate human survival, via either enhancing humans or modifying a descendant species to live on, several tests were made, with two groups making somewhat of a name for themselves. 
One focused on humans themselves, utilising vendrent DNA, and trying to modify that into human genetic coding, as the former of which are not too affected by the environment. 
This would be known as PROJECT HOMUNCULI. 
A separate facility also tried their own experiment, Trying to genetically modify a new species, one that they could custom develop, to have the desired strengths that humans were looking for. 
This project would further be known as PROJECT LYCAON. 
Homunculi was settled in the Northern district, Whereas Lycaon was settled in the far West.
After years of trial and error, project Lycaon began to see their success with the Accalian project, a furry humanoid creature, with human DNA, directly descended from humans, albeit with the resistances they desired, such as toxin immunity, weather resistance and X. 
A challenge however arised, when the human population brought into question the ethics of experimenting on humans. 
That being said, that wasn't what contributed towards lycaon's downfall. 
A combination of lack of funding, a decline in the project's success, and due to focusing on efficiency over safety, the power plant would suffer a failure, and mark the end of the project.  
The area was closed off, and the remains of the fallout were eventually left to what would eventually be to the outskirts. 
'''


text = '''
The most basic principle behind the fission reactor is to use neutrons to split atoms. 
When free neutrons are moving within a reactor, they may collide with an atom of fissile material and be absorbed. 
This makes the atom unstable and causes it to split into smaller atoms, releasing additional neutrons. 
The thermal energy released by each fission is used to evaporate water which drives a turbine and generates electricity. 
The amount of energy released is determined by the binding energies of the atom being split and its products. 
As can be seen from Figure 1, U-235 has a lower binding energy per nucleon than lighter elements closer to iron (around 1 MeV per nucleon less than its decay products). 
As such, splitting uranium into lighter elements causes a release of energy making it a viable power source. 
The neutrons released may collide with other uranium nuclei and cause more fission. 
This is essential if the reactor is to continue releasing energy. 
Ideally, the number of neutrons in the system will remain constant so the power output also remains constant. 
This means the neutrons released in fission must be sufficient to account for losses from leakage and capture. 
This is monitored in terms of the effective multiplication factor, which is the average number of neutrons produced by fission which go on to cause fission themselves. 
When exactly one, the system is self-sustaining when less than one, the number of fissions per unit time, and hence the power output, would decrease over time and tend towards zero. 
When greater than one, the rate of reactions would continually increase making the reactor highly dangerous. 
By tracking the motion and eventual outcome of a number of neutrons within a given reactor, an approximation of the kef f factor can be calculated. 
This is easily done with computational Monte Carlo methods, which are used in problems of random walks for many neutrons. 
This process can be refined in a number of ways and the reactor parameters varied to compare different designs. 
Neutrons may be emitted with a variety of energies and these will change as the neutron collides with the moderator and scatters. 
Most neutrons are emitted as fast neutrons and are slowed to thermal energies (hence the need for a moderator) but for simplicity, it is assumed that all neutrons are immediately thermal in this simulation. 
Despite this approximation, scattering is still relevant as the neutrons will still reflect off atoms within the moderator and fuel. 
Rather than causing a loss of energy or ending the walk, the neutron will instead take a new “step” upon scattering. 
A neutron in a reactor has a number of possible fates. 
It may be captured, either by the moderator or the fuel, or cause fission in the fuel. 
If a neutron causes fission, the number of neutrons released will vary depending on the daughter nuclei produced. 
The average number of emitted neutrons from U-235 fission is used, since when many neutrons are involved, the model tends towards the mean. 
The probability of fission given absorption, multiplied by the average number of neutrons emitted is denoted η. 
Also relevant is the fast fission factor. This represents the potential of a fast neutron causing fission before it is slowed to the thermal range. 
It is possible that the neutrons will be captured by the moderator. 
The probability of a neutron being absorbed by the fuel, given it is absorbed within the reactor, is known as the thermal utilisation factor, f. 
The product of these three terms, along with resonance escape probability, p, representing the probability of a neutron slowing to the thermal range without being absorbed, form the four factor formula. 
where kinf is the multiplication factor for a reactor of infinite size. In this project, p is not considered
and set to one.
This is assuming that all of the neutrons stay within the reactor which is not generally the case. 
For a finite reactor, there is a corresponding probability of neutrons escaping the reactor. 
This gives two leakage factors which lead to the six factor formula: where lf is the fast leakage factor and ls is the thermal leakage factor. 
The fast leakage factor will not be considered in the Monte Carlo simulation as no fast neutrons are modelled.
The probabilities of all these potential outcomes are found by considering the cross sections of all the
atoms within the reactor. 
A cross section is a measure of the effective size of an atom to an incoming neutron and directly correlates to the probability of the atom and neutron interacting in a given manner. 
As there are many atoms in the system, the macroscopic cross section per unit volume is calculated. 
These can be found by where ni is the number density of substance i within the reactor, i is the cross section of one atom of substance i and Σ is the total cross section per unit volume for the process. 
Σ is denoted as Σx where x describes the process (absorption, scattering or fission) taking place. 
In a homogeneous reactor, the moderator and fuel are evenly mixed, so the number densities used are the number density of the material throughout the whole reactor and not of the pure material. 
The cross sections are also dependent upon the energy of the incoming neutron but only one set is needed as this reactor uses exclusively thermal neutrons.
If the cross sections for fission, scattering and capture are known for both the moderator and fuel, probabilities and mean free paths for each event can be derived. 
A neutron in a reactor will take a number of exponentially distributed steps, with the characteristic length being the mean free path, as it is scattered and will eventually be absorbed. 
The mean free path is required as the step length of a neutron is exponentially distributed according to it. 
The direction of the step is determined separately following a uniform distribution. 
The mean free path (λ) is found from these cross sections by This is the mean free path for a single process. 
The fission probability, given neutron absorption, is found where f represents fission and a represents absorption. 
The core used in the following description consists of natural uranium and graphite in a ratio of 1:300. 
Using the values in table 1 for this composition, λa = 369 cm, λs = 2:33 cm and the fission the fission probability, given absorption, is 0.4659. 
Monte Carlo, Random Sampling and Statistical Methods. 
The Monte Carlo method is a statistical approach to solving mathematical problems and running simulations. 
The integral of a function f(x) over an interval can be written as which is the average value of that function over the interval, multiplied by the interval. 
This can then be approximated by finding the average of a number of points on the function inside the interval, as in equation 7.
While some methods suggest the use of points at set intervals, for many functions this may not work well. 
For example, a Sine function will be very badly approximated if the points happen to line up only with maxima. 
To counteract this, the Monte Carlo method requires repeated evaluation of points that are randomly distributed points over the interval, with the accuracy kept high by the use of many points. 
True randomness is difficult to achieve, but what is actually necessary here is a set of numbers that are unrelated to the function being approximated, so psuedo-random number generation is sufficient. 
This is where the set of numbers can be considered as random for most purposes and can be reproduced given one of the numbers and the function used. 
One example is the Linear Congruential Generator (LCG), given by and has a number of requirements for the values the parameters can take. 
A more modern version of this method is known as the Permuted Congruential Generator (PCG) and is implemented by the Python module NumPy. 
This module was used for the random number generation in this project. 
In order to ensure that generated step lengths were exponentially distributed, a uniformly distributed random variable was transformed to an exponential using the inverse CDF method. 
This method works by first taking the integral of the probability density function (PDF) being sampled. 
This integral is then inverted to find the cumulative distribution function (CDF). 
A uniformly distributed random variable (URV) is then passed into the CDF, resulting in a distribution following the PDF selected. 
A histogram of 100000 exponentially distributed random numbers generated using the inverse CDF method, along with a plot of ex can be seen in Figure 2. 
An important statistical principle used is the Ergodic principle, which is that.
"the time average value of an observable which of course is determined by the dynamics is equivalent to an ensemble average. 
This is of particular use here, since rather than following a single particle over a long timer period, through its daughter nuclei, their daughter nuclei and so on, which is difficult and computationally expensive, we can instead follow many particles for a single walk.
Method and Intermediate findings.
A single neutron walk is the basic building block for the rest of the model. 
A neutron is placed at a random position within the reactor. 
An exponentially distributed random step length is then calculated using the inverse CDF method as follows.
Figure 3 A threedimensional path of a single neutron as a succession of scattering events. 
This is an example of a neutron walk. where λ is the mean free path and u is a URV. 
This is calculated for scattering and absorption, using the respective mean free paths for both. 
Whichever path length is smaller is chosen, the direction of travel is generated in a similar way and the step is taken. 
If the neutron is absorbed the walk ends and a URV over the interval [0,1] is generated. 
If the URV is less than the fission probability, fission occurs. 
The walk will also end if the neutrons position after taking the step is outside the bounds of the reactor, this is known as leakage. 
A plot of a typical random walk can be seen in Figure 3. 
When a sample of neutrons was walked in a certain reactor the number of neutrons produced in fission is counted. 
This was done by adding 2.44 each time a neutron caused fission. 
Depending on the results desired, such as the average number of steps or final displacement from the starting position, other data was recorded as necessary. 
The keff value which was found using equation To check the predictions made by the Monte Carlo simulation, the multiplication factor for an infinite reactor can be compared to the analytically calculated values. 
Using a system of 100000000 neutrons, with leakage code removed, a value of k1 = 1.137 ± 0.001 was found which was the same as the analytic calculation to 4 significant fig. 
Figure 4 shows an example of uniformly distributed neutrons start positions and their new positions after one step. 
Figure 5 keff, the average number of neutrons produced by fission which go on to cause fission themselves, against generation number, where a generation is a set of neutrons being walked in the reactor and each generation starts at the fission points of the previous. 
It can be seen that the keff value settles after ten to twenty generations. 
This reactor could not reach a keff of 1, so would not be self-sustaining. 
In all prior cases, every neutron would begin its walk from a random position inside the reactor. 
However, it is clear that in reality walks would start from the positions where fission had occurred. 
With more neutrons starting walks closer to the edge of the reactor, it would be expected that more neutrons would escape and hence, keff would decrease. 
To make this correction the first set, or generation, of n neutrons began their walks from positions uniformly distributed across the system. 
The coordinates of those which caused fission were recorded in an array. 
The next generation of neutrons (equal in number to the first) would begin their walks from a position picked randomly from the array of fission coordinates. 
The array was then replaced with the coordinates of fission caused by the second generation. 
This was repeated until the value for keff became consistent over multiple generations. 
Once the neutron distribution had settled, the data from each subsequent generation was included in calculations. 
This is equivalent to increasing the number of neutrons used and thus decreases the error on any measurements. 
It was found that the distribution settled after around ten to twenty generations, so the contribution of the first twenty generations was removed before results were calculated. 
A plot demonstrating the settling of keff is shown in Figure 5. A cosine was fitted using chi-square minimisation to a histogram of neutron position along the z-axis, as seen in Figure 6. 
In this case, the flux was directly proportional to the number of neutrons, providing evidence that the model matched theory. 
However, since the sample was so large, the fractional errors were very small leading to a reduced chi-squared of 5.8. 
On the left of Figure 6 is a plot of neutron flux as a function of radius, overlaid with a ordinary Bessel function of zero order fitted using the same technique. 
The fit looks good by eye and the error bars are small, but the reduced chi-squared was 2.8. 
Figure 6 Left The neutron flux within a reactor against the radial distance from the z-axis in orange, with an ordinary Bessel function of zero order plotted in blue. 
Right Histogram of neutron density on z-axis in the reactor with a fitted cosine overlaid. 
The cylinder had a height of 500cm. 
The origin was at the centre of the cylinder The distribution which the neutron flux follows is given by the solution of the reactor equation where φ is the neutron flux and B2 is known as the buckling. 
For a reactor with cylindrical symmetry, φ can be split into a product of functions of height and radius. 
It has been shown that the function of radius is an ordinary Bessel function of zero order and the function of height should be a cosine, resembling a first harmonic.
From theory it was expected that the number of neutrons would not reach zero at the edges due to the extrapolation distance. 
The size of the reactor was increased such that this became a negligible error.
To reduce the error on the obtained keff values, a graph of the error against the number of input neutrons was plotted, shown in Figure 7. 
It was found that the error decrease plateaued after around 30000 neutrons, and a balance had to be found between error reduction and run-time. 
The trend in error with the number of generations of neutrons implemented was also found for the same purpose, as seen in Figure 7. 
500 generations for important calculations was adopted. 
CUDA Card Simulations. 
Python timers were used to find where time was being spent and it was found that even the random number generation, expected to be slowest, was very quick due to the use of PCG. 
However, when scaled up in number (due to neutrons, generations) such that the required accuracy was achieved, it became infeasible to find the minimum ratio. 
Setups with a large enough sample size such that statistical fluctuations were not significant took days to complete. 
Therefore, the code was rewritten with Numba wrappers, so it ran on a GPU rather than a CPU. 
Figure 7 Left: Error on keff against the number of input neutrons. 
20000 neutrons for important calculations was adopted as a balance between accuracy and run-time. 
Right Error on keff against the number of generations of neutrons. 
500 generations for important calculations was adopted as a balance between accuracy and run-time. 
Previously, a neutron would be walked, then another, and so on until the end of a generation. 
Then this was repeated for many generations in a single thread. 
Parallelising to a number of threads gave little improvement. 
After rewrite, calculations were done within matrices, which is known as vectorisation. 
Three arrays were produced, each with n columns. 
The first held a vector in three dimensional space for the starting positions of n neutrons. 
The second array held n exponentially distributed random step lengths, which were found by the minimum of two random lengths corresponding to absorption and scattering. 
The final array held n uniformly distributed directions in three dimensional space. 
Each core then used the latter two arrays to operate on the first, such that the position array then held n vectors representing the position of each neutron after taking a step. 
If a neutron caused fission, its position was recorded and removed from the array. 
The positions was also removed if a neutron leaked or captured. 
This was repeated until the array was empty and then a new set of walks began the next generation. 
Generations were evaluated sequentially because the output of the previous generation is the input for the next. 
The complexity was reduced from O(n*G) on the CPU to O(G) + O(n) on the GPU, where O(G) describes the sequential evaluation of generations, so the speed increase was substantial. 
Python timers were used to compared the speed of GPU vs CPU versions of sections throughout to determine which was faster, as sending work to the GPU takes a comparatively long time. 
Comparisons were made to ensure that the results were consistent between versions, and they were within one standard error. 
This maintained a high accuracy in a reasonable time. 
Minimising the Volume of a Critical System by Size Ratio Optimisation. 
To find the minimum required critical mass (the mass required for a self-sustaining reaction), the most efficient radius to height ratio for a cylindrical reactor was found, then the volume was increased while maintaining the ratio until the reactor reached keff = 1. 
The optimum ratio was found by increasing the radius until the reactor went critical for a large range of fixed heights. 
As points were found, the range of values which included the minimum volume also found. 
Values were found over increasingly smaller ranges until the statistical noise started to dominate the improvement. 
A plot was produced of reactor volume against the ratio and the its minimum corresponded to the optimum ratio. 
This is shown in Figure 8.
Once the optimal ratio was confirmed as matching theory, the system was fixed in this ratio. 
The height was varied with the radius changing in turn and values for keff were taken over a large range of heights. 
The interval between data points was steadily reduced as the range in which the minimum critical volume lay narrowed. 
This was repeated until the height corresponding to the critical volume 8was found to the nearest centimetre, requiring an increase in the number of neutrons and generations for higher precision keff values. 
From the height, the volume of the reactor and the critical mass of fuel was derived.
Figure 8 The optimum radius to height ratio for a cylindrical reactor was found by finding the minimum of a critical volume against hr graph. 
The ratio found was 0.55 to two significant figures, matching theory. 
All textbook values found were not useful for comparison due to significantly different assumptions or compositions. 
Therefore, theoretical values were calculated with the following method. 
First the diffusion length squared of thermal neutrons in the core was found using the equation where D¯ is the average thermal diffusion constant for neutrons in graphite and Σ¯a is the average, thermal macroscopic absorption cross section. 
These values are then used to find first the buckling B by where D¯ is the average thermal diffusion constant for neutrons in graphite and Σ¯a is the average, thermal macroscopic absorption cross section. 
These values are then used to find first the buckling B by where this final equation applies only to a cylindrical reactor.
The result obtained for the minimum volume of a cylindrical, graphite-natural uranium reactor with a moderator to fuel ratio of 1:300 was (19:5 ± 0:2) m3, assuming the height is accurate to one centimetre and propagating the error through r = 0:55h. 
This size reactor would require (2:06 ± 0:02) × 103 kg of natural uranium fuel, assuming a graphite density of 1.6 gcm−3 [9]. 
Heights greater than this gave greater keff values and shorter heights gave smaller keff values suggesting that this was not an anomaly. 
This check was performed for all minimisation results. The theoretical value calculated was 2:3 × 103 kg of uranium. 
9The errors given are derived from the standard deviation over generations. 
The sources of systematic errors were discussed in section 2.1, due to approximations inherent in the model, and will lead to errors larger than those stated, explaining why the computed and theoretical values are not consistent. 
Comparing the error to the delayed neutron fraction provides insight into the safety of the reactor. 
Delayed neutrons do not cause fission as quickly as prompt neutrons so provide a longer time period in which they may be controlled. 
Should the reactor exceed criticality with prompt neutrons alone, it would be uncontrollable and the number of neutrons would grow exponentially. 
Criticality with delayed neutrons would provide enough time to insert control rods (or implement other measures) to prevent this. 
By ensuring that the fractional error is less than the delayed neutron fraction, one can be confident that keff does not exceed one by so much that the reactor would be super-critical with no ability to control it using the delayed neutrons. 
When U-235 is the fissile material, the delayed neutron fraction is roughly 0.65%. 
The fractional error here is 0.06% which is considerably less than the delayed neutron fraction, hence this reactor should be safe and controllable.
Initially, a system using light water and natural uranium was constructed in a fuel to moderator ratio of 1:25. 
Leakage was then removed from the model to find a value for k1 using 10000 neutrons. 
This gave k1 = 0:427 ± 0:009 which is far from reaching criticality, and if a lower ratio was used then the dilute approximation becomes less valid and the model breaks down. 
This can be attributed to the high capture cross section of water, σc = 0:66 b, which is approximately 150 times greater than that of graphite. 
This meant that the majority of neutrons were captured by water molecules after travelling only a short distance. 
In order to allow for a higher chance of capture, enriched uranium was used instead. 
The uranium was enriched to 3% U-235 and the same fuel to moderator ratio was used. 
As U-235 is the isotope which is the fissile material within the fuel and natural uranium consists of only 0.72% U-235, enriched uranium has a greater fission cross section. 
After testing the system to ensure it could become critical, leakage and generations were reintroduced to find the smallest self-sustaining core possible using the same method as for the graphite reactor. 
With a series of samples using 20000 neutrons over 400 generations, a height of 39 cm gave keff = 1:0000 ± 0:0004. This is much smaller than the graphite reactor due to both the fuel and moderator having greater absorption cross sections, as well as the much lower moderator to fuel ratio.
The volume of this reactor was found to be (560000 ± 4000) cm3. 
Thus it was found that a mass of (29 ± 2) kg of uranium is required. 
These are consistent with the analytically calculated values of 500500 cm3 and 26:7 kg. 
This demonstrates that light water reactors can go critical at a practical size. 
Light water is also a readily available and cheap moderator. 
However, the fuel must be enriched for this to work which increases the cost and complexity of using light water reactors. 
Although the caveats on the error for the graphite reactor apply here as well, the fractional error using this method is much less than the delayed neutron fraction, meaning the reactor can be controlled safely. 
Heavy water has the smallest capture cross section of σc = 0:001 b which suggests natural uranium would be a practical fuel with it. 
Using the same 1:300 fuel to moderator ratio as the graphite reactor and the same method, the reactor reached criticality with keff = 1:0007 ± 0:0005 at a height of 328 cm. 
This core had a volume of (3:35 ± 0:03) × 107 cm3 which includes (1400 ± 100) kg of uranium. 
While this is somewhat similar to the predicted value of 3:63 × 107 cm3, it is not consistent. 
This is likely due to the rounding errors or differences in input parameters, such as cross sections, becoming a more dominant source of uncertainty than the random nature of the model. 
This system is similar to graphite in that the reactor can become critical with only natural uranium so does not require any enrichment. 
On the other hand, heavy water is hard to isolate in the volumes needed and very expensive. 
Any errors are similar in nature to those discussed in prior sections and again, the error on the keff is smaller than the delayed neutron fraction so the reactor should be controllable. 
The uranium sphere is a rather different system, not just because of the change in shape. 
It consists entirely of fuel and operates using exclusively fast neutrons. 
As such, any cross sections used in calculations were different. 
Finding the critical mass was simpler in this case as there was only one parameter to vary, the radius, which meant there was no need to find an optimal ratio. 
Following a similar approach, the radius was increased until keff = 1 then the increment was decreased to get a more precise value. 
With 20000 neutrons over 200 generations, keff = 1:0005 ± 0:0006 was found at r = 9:05 cm. 
This corresponds to a mass of (58:1 ± 0:2) kg for an error of 0:001 cm on the radius. 
This is close to the theoretical value of 56 kg although not consistent. 
This is likely down to factors not accounted for in this simplified model and differences in input values varying between sources. 
Once again, the dominant uncertainty came from the uncertainty in the inputs as opposed to the statistical variations. 
Also of potential interest is a comparison to a nuclear weapon. 
For example, the Little Boy bomb used 64 kg of U-235. 
It is to be expected that these values would differ due to differences in shape, reflective surfaces, impurities and the need for super-criticality to name a few factors. 
However, the numbers are still sufficiently similar to demonstrate the effectiveness of this method and provide some real world context to the numbers. 
Monte Carlo simulations provide a powerful tool for predicting parameters of reactors that cannot be easily found using analytical techniques, such as non-standard shapes, and can reach a very high precision provided sufficient computational resources and time. 
It has been shown that even with the approximations made, it produces values that are generally in agreement with theoretical predictions. 
An improvement on this model that would be relatively simple to implement is to convert it to a two-group model, which will include the production of fast neutrons and account for the distances required to thermalise them. 
This would be easier to compare to theoretical values as it is included in much literature. 
For the cylindrical reactors, the critical masses found were (2:06 ± 0:02) × 103 kg for a 1:300 graphitenatural uranium mixture, (29 ± 2) kg for a 1:25 light water-3% enriched uranium mixture and (1400 ± 100) kg for a 1:300 heavy water-natural uranium mixture. 
For a pure U-235 sphere, similar to the composition of traditional nuclear weapons, the mass obtained was (58:1 ± 0:2) kg.
'''


#Loading in a test file

with open("reed_ny_post.txt") as f:
    contents = f.read()

contents = text
#Parser is given the text to read


parser.set_text(contents)

#Text is parsed, converting into a dict of paragraphs (\n\n) which contains the array of trees for each sentence.
parser.process_text()


print(parser.get_paragraphs())

print("######")

print(parser.get_sentences())


#Getting the paragraph dictionary back out from the parser
para_dict = parser.get_para_dict()

print(para_dict)


bali_text = para_dict[0]

noun_sentences = []
for sentence in bali_text:
    noun_sentences.append(parser.extract_nouns(sentence))


def nouns_to_tree(noun_sentences):
    reduced_sentences = []
    tree_convert = TreeConverter()
    for sentence in noun_sentences:
        reduced_sentences.append([x[0] for x in sentence])

    total_trees = []
    for reduced in reduced_sentences:
        reduced_tree = tree_convert.convert_sentence(reduced)
        if reduced_tree:
            nodes = reduced_tree.traverse_tree(tranversal_type="dfs")[0]
            print(nodes)
            node_sentence = [x.contents for x in nodes]
            print(node_sentence)
            total_trees.append(reduced_tree)

    return total_trees



total_trees = nouns_to_tree(noun_sentences)
test_document = Document()
test_document.set_trees(total_trees)
print(test_document.trees_to_strings("dfs"))
output, node_dict = test_document.trees_reordering()





def parse_list(list, depth):
    if type(list) == type({}):
        for key in list:
            print(">"*depth + f"|{depth}|{key} - {list[key]}")
    else:
        depth += 1
        for item in list: 
            parse_list(item, depth)


for key in output:
    print(f"------\n#{key}#\n-------")
    parse_list(output[key], 0)


print(node_dict)



prior_node = None
new_link = None
link_count = 1
first_node = None
contents_to_id = {}
for node in node_dict:
    contents_to_id[node_dict[node].contents] = node

for key in output:
    current_node = node_dict[contents_to_id[key]]
    if prior_node:
        new_link.set_end(current_node)
        new_link = Link(current_node, link_count, LinkNature.CHILD)
        current_node.add_link(new_link)
        link_count += 1
        prior_node = current_node
    else:
        new_link = Link(current_node, link_count, LinkNature.CHILD)
        current_node.add_link(new_link)
        link_count += 1
        prior_node = current_node
        first_node = current_node

visited_ids = set()

visited_contents = set()

total_node_tree = test_document.recurse_node(node_dict[1], visited_ids, visited_contents, 0)[0]

print("###########\n\n\n##########")
visited_ids = set()
visited_contents = set()

parse_list(test_document.recurse_node(node_dict[1], visited_ids, visited_contents, 0), 0)


# print(total_node_tree)


def read_tree(node_tree):
    if type(node_tree) == type(list()):
        output = {}
        link_count = 1
        for x in node_tree:
            output[link_count] = read_tree(x)
            link_count += 1
        return output
    else:
        output = {}
        for x in node_tree:
            output[x] = node_tree[x]
        # print(output)
        return output

output = read_tree(total_node_tree)

# for x in output:
#     print(output[x])
        
# print(type(total_node_tree))
    




def recurse_list(tree, visited_nodes, depth, prior_depth, node_positions):
    # print(prior_depth, depth)
    #print(node_positions)
    if len(node_positions) < depth+1:
        node_positions.append([])   


    print(depth, prior_depth, node_positions[depth])
    print("#####")
    prior_depth = depth
    depth += 1

    # if depth 

    first_id = next(iter(tree.keys()))
    if first_id == 1:
        items = len(tree.keys())
        total_nodes = []
        for i in range(1, items+1):
            next_node = recurse_list(tree[i],visited_nodes,depth, prior_depth, node_positions)
            if next_node:
                node_positions[depth-1].append(next_node)
                total_nodes.append(next_node)
        
        # if total_nodes:
        #     print(total_nodes)
            # print(next_node)
        # recurse_list(tree[1], visited_nodes, depth)
        # print(first_list)
    else:
        return tree



    # print(tree)
    # print(depth*" " + "recursing")
    # if isinstance(tree, dict):


    #     first_id = next(iter(tree.keys()))
    #     if first_id == 1:
    #         first_value = tree[1]
    #         depth += 1
    #         print(1)
    #         first_node = recurse_list(first_value, visited_nodes, depth)
    #         child_nodes = []
    #         for i in range(2, len(tree.keys())+1):
    #             print(i)
    #             child_nodes.append(recurse_list(tree[i], visited_nodes, depth))
    #         print("-----")
    #         if first_node:
    #             print(first_node)
    #             print("#####")
    #         if child_nodes:
    #             print(child_nodes)
    #             print("#####")
    #         print(" "*depth + "returning")
    #         # print(tree)
    #         # remaining_values = list(tree.items())[1:]
    #         # if remaining_values:
    #         #     for x in remaining_values:
    #         #         print(" "*depth + str(x))


    #     else:
    #         node_id = next(iter(tree.keys()))
    #         value = tree[node_id]
    #         new_node = Node(node_id, value, value)
    #         print(depth*" " + "returning")
    #         return new_node
            #print(new_node)
        # tree_iter = iter(tree.values())
        # depth += 1
        # first_item = recurse_list(next(tree_iter),visited_nodes, depth)
        # if first_item:
        #     print(first_item, first_item.content)
        # print(tree.keys())





    #     if 1 in tree.keys() and first_item.id not in visited_nodes:
    #         items_len = len(list(tree.keys()))
    #         if items_len:
    #             child_nodes = []
    #             for i in range(1, items_len+1):
    #                 child_node = recurse_list(tree[i], visited_nodes, depth)
    #                 print(child_node)
    #                 if isinstance(child_node, str):
    #                     print(tree)
    #                 visited_nodes.add(child_node.id)
    #                 if child_node:
    #                     child_nodes.append(child_node)
    #             if(child_nodes):
    #                 print(" "*depth + child_nodes[0].content)
    #     else:
    #         node_id = next(iter(tree.keys()))
    #         visited_nodes.add(node_id)
    #         node_contents = tree[node_id]
    #         new_node = Node(node_id, "SPAN", node_contents)
    #         return new_node
    # else:
    #     if isinstance(tree, str):
    #         return tree
    #     print(tree)



    # output_dict = {}
    # if 1 in tree.keys():
    #     print("+")
    #     next = recurse_list(tree[1])
    #     items = []
    #     print(next)
    #     for x in list(tree.keys())[1:]:
    #         item = recurse_list(tree[x], visited_nodes)
    #         if item:
    #             items.append(item)
    #     # print(next)
    #     #output_dict = {}        
    #     if type(next) == type({}): 
    #         if "FOLLOWED_BY" not in next.keys():        
    #             for key in next:
    #                 output_dict[next[key]] = Node(key, "SPAN", next[key])
    #             if output_dict:
    #                 return {"FOLLOWED_BY":output_dict}
    #             else:
    #                 return output_dict
    #         else:
    #             if items:
    #                 # output_dict["FOLLOWED_BY"] = next["FOLLOWED_BY"]
    #                 for x in items:
    #                     working_dict = x
    #                     id = list(x.keys())[0]
    #                     print(tree)
    #                     if id != "FOLLOWED_BY" and isinstance(x, str):
    #                         text = x[id]
    #                         new_node = Node(id, "SPAN", text)
    #                         output_dict[text] = new_node
    #                 return output_dict
    #             else:
    #                 return tree
    # else:
    #     if tree:
    #         print(f"##{tree}##")
    #         print(output_dict)
    #     return tree

                           # print(output_dict)
                        # if isinstance(x, int):
                        #     key = list(x.keys())[0]
                        #     val = x[key]
                        #     new_node = Node(key, "SPAN", x[key])
                        #     output_dict[val] = new_node
                 
                    # print(items)
                #print(key, next[key])
            #print()
        # for iterator in tree.keys():
        #     return recurse_list(tree[iterator]) 
    
    # if len(tree.keys()) == 1:
    #     if list(tree.keys())[0] == 1:
    #         # print(tree)
    #         recurse_list(tree[1])
        # else:
            # print(tree)
    # else:
    #     for x in tree:
    #         print(x, tree[x])
    #         recurse_list(tree[x])
            # print(tree[x])
    
visited_nodes = set()
added_links = []
added_nodes = []
node_positions = []


result = recurse_list(output, visited_nodes, 0, 0, node_positions)


print(node_positions)
print("---------------------------")
for x in node_positions:
    print(x)

print(total_node_tree)
print(node_dict)
prior_node = None
expected_nodes = set()
root_nodes = []
links = []
total_nodes = []
parent_nodes = {}

def link_nodes(node_1, node_2, id):
    new_link = Link(node_1, id, LinkNature.CHILD)
    new_link.set_end(node_2)
    return new_link

link_id = 1

for level in range(0, len(node_positions)-1):
    nodes = node_positions[level]
    print(nodes)
    # nodes_to_object = [node_dict[contents_to_id[x[list(x.keys())[0]]]] for x in nodes]
    node_objs = []
    for node in nodes:
        node_id = list(node.keys())[0]
        node_contents = node[node_id]
        if node_id in node_dict:
            node_object = node_dict[node_id]
            node_objs.append(node_object)
            total_nodes.append(node_object)
        else:
            node_dict[node_id] = Node(node_id, "Noun", node_contents)
            total_nodes.append(node_dict[node_id])

        if node_contents in expected_nodes:
            print("EXPECTED", node_contents)
            print(prior_node, node)
            link = None
            if node_contents in parent_nodes:
                if node_id in node_dict:
                    link = link_nodes(parent_nodes[node_contents], node_dict[node_id], link_id)
                    from_node_link = link_nodes(node_dict[node_id], parent_nodes[node_contents], link_id+1)
                    
                    #node_dict[node_id].add_link(link)
                    links.append(link)
                # else:
                #     link = link_nodes(parent_nodes[node_contents], total_node_tree[node_id], link_id)
                    link_id += 2
                print(node_contents, parent_nodes[node_contents], link)



            prior_node = node
        else:
            root_nodes.append(node)

            prior_node = node
            print("UNEXEPECTED", node)

            # print(node_id)

    node_children = {x.contents:x.get_children() for x in node_objs}

    for node in node_objs:
        for child in node.get_children():
            if child:
                parent_nodes[child.contents] = node

    children_contents = {}


    for child in node_children:
        related_nodes = node_children[child]



        children_contents[child] = [x.contents for x in related_nodes if x]
    #children_content = [node_children[x] for x in node_children]
    if children_contents:
        total_vals = []
        print(children_contents)
        items = []
        child_content = [children_contents[x] for x in children_contents.keys()]
        for x in child_content:
            total_vals += x
        for x in total_vals:
            expected_nodes.add(x)
        #expected_nodes.add(x for x in total_vals)
        # print(total_vals)
        # for x in children_contents:

        # print(children_contents)
print(parent_nodes)
print(expected_nodes)
print(root_nodes)
print(links)
print(total_nodes)

spanning_tree = Tree(total_nodes[0], total_nodes[1], links[0], 1)

for node in total_nodes[2:]:
    spanning_tree.add_node(node)

for link in links[1:]:
    spanning_tree.add_link(link)

output = spanning_tree.tree_to_string()


span_links = output[0]
depth_nodes = output[1]
total_contents = output[2]

print(span_links)
print(depth_nodes)
print(total_contents)
depth = 0
output_string = ""
for x in depth_nodes:
    print(depth)
    output_string += f"{depth}: "
    depth += 1
    for node in x:
        node_id = node.id
        if node_id in node_dict:
            node_from_dict = node_dict[node_id]
            children = node_from_dict.get_children()
            children_in_total = [x.content for x in children if x.content in total_contents]
            output_string += "\t"*depth + f"{node.content}->{', '.join(children_in_total)} "
    output_string += "\n"

print(output_string)

    # print(node_children)
        # print(total_node_tree[node_id])
        # print(total_node_tree[list(node.keys())[0]])
    # print(nodes_to_object)


    # node_children = [x.get_children() for x in nodes_to_object]
    # child_contents = [x.contents for x in node_children]
    # next_node = node_positions[level+1]
    # print([x.contents for x in nodes_to_object])
    # print(node_children)
    # print(child_contents)
    # print(next_node)
    # print("-------")


# print (node_dict[contents_to_id["coronavirus"]].get_children()[0].contents)
# print(result)