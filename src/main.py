"""
Title: Finding Fermats Theorem Near Misses
Filename: src/main.py
External files needed: None
External files created: None
Programmers: Laurynas Motuzis <mlauris2006@yahoo.com>, Kaushalkumar Dineshbhai Sharma <Kdsharma1706@gmail.com>
Course/Section: Software Engineering — PSC 60500, Section 1
Program completion date: 9/20/2025
Program submission date:9/20/2025
Resources used: Python documentation, assignment handout, Stack Overflow

Program summary:
Prompts the user for n (3-11) and k (≥10), iterates all x,y in [10..k] to find the smallest
relative “near miss” to x^n + y^n = z^n. Prints each new smallest miss found and at the end
prints the overall best result with labeled values (x, y, z, S, miss, relative miss).

"""

def main():
    # Step 1: Input handling ------------------------------------------
    # Ask the user for the power n (must be between 3 and 11, since 2 < n < 12)
    n = int(input("Enter power n (3–11): "))
    
    # Ask the user for the upper bound k (x and y will range from 10 to k)
    k = int(input("Enter maximum value k (>10): "))

    # Initialize tracking variables -----------------------------------
    # Store the smallest relative miss found so far (start with 1.0 = 100%)
    smallest_relative_miss = 1.0
    
    # Store the best result tuple (x, y, z, miss, relative_miss)
    best_result = None

    # Step 2: Double loops for x and y --------------------------------
    # Loop through all combinations of x and y in the given range
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            
            # Step 3: Compute x^n + y^n -------------------------------
            sum_val = x**n + y**n

            # Step 4: Find nearest z ---------------------------------
            # z should be close to the nth root of sum_val
            z = int(round(sum_val ** (1/n)))

            # Step 5: Compute miss -----------------------------------
            # Miss is the difference between sum_val and the nearest z^n
            miss1 = abs(sum_val - z**n)       # difference with z^n
            miss2 = abs((z + 1)**n - sum_val) # difference with (z+1)^n
            miss = min(miss1, miss2)          # take the smaller miss

            # Step 6: Compute relative miss --------------------------
            relative_miss = miss / sum_val

            # Step 7: Check if this is the best so far ---------------
            if relative_miss < smallest_relative_miss:
                # Update the best miss
                smallest_relative_miss = relative_miss
                best_result = (x, y, z, miss, relative_miss)

                # Print labeled output for clarity
                print("\nNew best near miss found:")
                print(f"  x = {x}, y = {y}, z = {z}")
                print(f"  Absolute miss = {miss}")
                print(f"  Relative miss = {relative_miss:.8f}")

    # Step 8: Final result --------------------------------------------
    print("\nFinal best near miss:")
    print(f"  x = {best_result[0]}, y = {best_result[1]}, z = {best_result[2]}")
    print(f"  Absolute miss = {best_result[3]}")
    print(f"  Relative miss = {best_result[4]:.8f}")

# Standard entry point
if __name__ == "__main__":
    main()