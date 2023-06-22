Task description
A local bank office often transports bags of money to and from their main office. They have asked you to develop a script that can help them know beforehand how many bags will fit in the truck transporting the money, and what the value of all the bags combined is.

The size of the truck transporting the money bags can vary in size from transport to transport so the size must be read from the user each time running the script. If the user enters a volume less than 100L they shall be asked again until they give a volume larger than 100L.

After having read the size of the truck, the script shall calculate how many money bags of each size fits in the specified truck and display it on the following format:

        4 big bags
        2 medium bags
        0 small bags

The banks internal policy documents dictate that they must only use bags in three sizes (20L, 50L, and 80L) and that they must always use as many of the bigger bags as possible. Here is an example to illustrate this:

Truck size = 220L

1. How many big bags (80L) can we fit in 220L? Answer is 2.
   We now have 60L left in truck.

2. How many medium bags (50L) can we fit in the remaining 60L? Answer is 1.
   There is still 10L left in the truck.

3. How many small bags (20L) can we fit in the remaining 10L? Answer is 0.
   There is 10L left in the truck that we can not fit any bag into.

There is a strict requirement that the number of bags of each type shall be calculated using three loops, one for finding out how many big bags can fit, one for how many medium bags can fit in the remaining space, and finally, one for calculating how many small bags fit after having stored as many big and medium bags as possible.

Having decided how many bags can be transported it is time to calculate how much the shipment is worth and display this information to the user. A small bag is worth 10.000kr, a medium bag 30.000kr, and a big bag is worth 60.000kr. The following format shall be used when printing the total value:

        Total value: 70000kr
