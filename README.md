# weap - wieferich primes easy as pie #

As part of a university class on distributed computing, we decided to start looking for wieferich primes.

For reasons of speed comparison we implemented the wieferich search algorithm in the following ways:
* non-threaded
* threaded (Python's GLI of course prevents this from actually working any faster)
* distributed using NVIDIA GPUs

We actually saw a pretty major performance increase, lowering the time it took to check 12.8 million numbers (our selected gpu block size) starting at 6.7*10^15 from 10 minutes, 41 seconds (single threaded) to 0.16 seconds.
