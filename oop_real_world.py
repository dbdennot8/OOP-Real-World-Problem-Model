"""Program to return ranges of prices of phones on an online-seller's website

The class Smartphone inherits from the parent class Phone """



class Phone(object):
  def __init__(self, manufacturer):
    self.manufacturer = manufacturer
    


class Smartphone(Phone):
  def __init__(self, storage, manufacturer):
    self.storage = storage
    super(Smartphone, self).__init__(manufacturer)


  def price(self):
    if self.manufacturer == "Apple":
      return "Price is in the range of 800 - 1100 USD."

    elif self.manufacturer == "Samsung" or self.manufacturer == "Sony" and self.storage >=32:
      return "Price is in the range of 500 - 800 USD."

    elif self.manufacturer == "Apple" or self.manufacturer == "Samsung" and self.storage <32 and self.storage >8:
      return "Price is in the range of 300 - 500 USD."

    elif self.manufacturer != "Apple" or self.manufacturer != "Samsung" or self.manufacturer != "Sony":
      return "Sorry. We only stock, Apple, Samsung and Sony smartphones."

    else:
      pass

  def colors_available(self):
    if self.manufacturer == "Apple":
      return "silver or rose gold"

    else:
      return"black, blue, red, grey or silver"
      

  def give_aways(self):
    if self.storage >= 16:
      return"Free screen protector and Free Flip Cover"
    elif self.storage >= 32:
      return "Free Dual Window cover and Corning screen protector"
    else:
      return "No give aways available for that option"

iPhone = Smartphone(8, "Apple")
print iPhone.give_aways()
