"""Classes for melon orders."""
class baseMelonOrder:
    
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5 

        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3
        return total

        

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

        
        
class DomesticMelonOrder(baseMelonOrder):
    """A melon order within the USA."""
    
    """Initialize melon order attributes."""

    
    order_type = "domestic"
    tax = 0.08

    def __init__(self,species, qty):
        super().__init__(species, qty)

    
    

class InternationalMelonOrder(baseMelonOrder):
    """An international (non-US) melon order."""
        
    order_type = "international"

    tax = 0.17

   

    def __init__(self,species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
       
     
    # Order_total = InternationalMelonOrder(baseMelonOrder) + 3

# 1. Check if Int order is less than 10 melons
# 2. If Int order < 10 melons, then total + $3

class GovernmentMelonOrder(baseMelonOrder):

    order_type = "government melon"


    def __init__(self, species, qty, passed_inspection = False):
        super().__init__(species, qty)

    

    def mark_inspection(passed):
            passed_inpections = True