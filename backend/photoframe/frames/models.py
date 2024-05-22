from django.db import models

class Frame(models.Model):
    # Title of the photo frame
    title = models.CharField(max_length=100)
    
    # Image of the photo frame, stored in 'frames/' directory within media root
    image = models.ImageField(upload_to='frames/')
    
    # Original price of the photo frame, with up to 10 digits and 2 decimal places
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Discounted offer price of the photo frame, with up to 10 digits and 2 decimal places
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Boolean field to mark if the frame is a top sale item
    top_sales = models.BooleanField(default=False)

    # String representation of the model, returning the title of the frame
    def __str__(self):
        return self.title
