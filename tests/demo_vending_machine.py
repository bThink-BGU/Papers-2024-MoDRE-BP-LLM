prompt = """
The following is a system of a controller for a gate at a railway crossing - an intersection between a railway line and a road at the same level. 

Events: Approaching, Entering, Leaving, Lower, Raise

Requirements:

- When a train passes it requests to approach, enter, and then leave.
- The barriers are lowered when a train is approaching and then raised.
- A train may not enter while barriers are raised.
- The barriers may not be raised while a train is in the intersection zone, between its approaching and leaving.

The following is a system of a vending machine that sells products.

Events: "Coin Inserted", "Product Selected", "Product Dispensed", "Rejection", "Change Return", "Refill", "Maintenance",

Requirements List:

- Coins can be inserted into the vending machine at any time.
- Product Selection can only occur if at least one coin has been inserted.
- Product Dispensation can only occur if a product has been selected and two or more coins are inserted.
- Rejection can only occur if a product has been selected and less than two coins are inserted.
- If Product Dispensation occurs, Change Return should follow if more than two coins are inserted.
- Refill can only occur when the vending machine is not currently in use, i.e., not between coin insertion and rejection/dispention.
- Maintenance can only happen after Refill.
- Between any two occurrences of Refill, there should be no more than 2 occurrences of Maintenance.
- Between the occurrence of Refill and Event Maintenance, there should be no occurrences of Coin Insertion.


"""