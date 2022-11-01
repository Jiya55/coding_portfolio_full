'''
planning-

intents-
checking if a product is in stock
payment
price of a product
add cart
don't add cart
remove cart
shop tour

regex for intent-
checking products-((...? you (have|find).*)|(is .* (available|in stock).*)|(....? I need.*))
do you have ___?   (.. you have .* ?)(.*have.*)
can you find ___? (... you find .* ?)(.*find.*)
is this available? (is .* available)(.*available.*)
is .* in stock ( is .* in stock )(.*in stock.*)

add cart-
yes, can you add ___ in cart(.*cart.*)
i want to put this in cart(.*cart.*)

don't add in cart

remove item

shop tour

payment






'''
import re

pulses = ['tata sumpan yellow dal', 'tata sumpan black dal', 'kidney beans']
beverages=['tata red label tea', 'nestle gold coffee', 'teatley green tea']
vegetables=['carrots','beans', 'potatoes', 'onions', 'tomatoes']
inventory={
    'tata sumpan yellow dal':[40, 100],
    'tata sumpan black dal':[50, 100],
    'kidney beans':[35, 40],
    'tata red label tea':[50, 120],
    'nestle gold coffee':[60, 150],
    'teatley green tea':[50, 50],
    'carrots':[60, 10],
    'beans':[50, 15],
    'potatoes':[60, 5],
    'onions':[40, 20],
    'tomatoes':[60, 10]
    }
#catagories={pulses, beverages, vegetables}
# , fruits, snacks, sugar, spices, flour, rice, pasta, jam, condiments


Inventory = {'teatley green tea':[10, 100], 'tata gold coffee':[5, 40]}
class Shop_assistent:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry", 'nopes')
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    intents={
        'check_product': r'.*(have|need|want|available|in stock|buy).*',
          'add_cart': r'.*cart.*',
        'remove_item':r'.*(remove|deduct|minus).*',
        'shop_tour':r'.*shop.*',
        'payment': r'.*pay.*'}
    def __init__(self, inventory):
        self.inventory = inventory
        self.cart = {}
    def greet(self):
        print('Hello, Welcome to our shop')
        self.help()
    def exit(self, response):
        for ec in self.exit_commands:
            if ec in response:
                return True
    def negetive(self, response):
        for nr in self.negative_responses:
            if nr in response:
                return True
    ''''def catagorise(self, sentence):
        product=''
        for i in sentence.split(' '):
            if i in ['pulses', 'dal', 'legumes', 'rajma', 'kidney']:
                print('pulse')
                product+='pulse'
            elif i in ['tea', 'beverage', 'coffee']:
                print('beverage')
                product+='beverage'
            elif i in ['carrots', 'beans', ' vegetables','tomato', 'carrot', 'tomatoes', 'bean', 'onion', 'onions', 'potato', 'potatoes']:
                print('vegetable')
                product+= 'vegetable'
            else:
                print('undifined')
    i '''
def help(self):
        will_help = input('how may I help you? ')
        while not(self.exit(will_help)):
            for intent, regex in self.intents.items():
                if re.match(regex, will_help):
                    if intent == 'check_product' and not('cart' in will_help) and not('shop' in will_help) and not('payment' in will_help):
                        self.check_product()
                        
                    elif intent == 'add_cart' and not(self.negetive(will_help)):
                        self.add_cart()
                    elif intent == 'add_cart' and self.negetive(will_help):
                        print('ok')
                    elif intent == 'remove_item':
                        self.remove_item()
                    elif intent == 'shop_tour':
                        print(self.inventory)
                    elif intent == 'payment':
                        self.payment()
                    else:
                        print('sorry, I didn\'t understand you, if you are having trouble, here are the commands for all possible functions- checking availibilty of a  product(available, in stock), adding items(cart), removing items(remove), shop tour(shop), paying(pay)')
                    will_help = input('how may I help you? ')
            
            
    def check_product(self):
        product = input('what is the product name? ')
        message=''
        for key, value in self.inventory.items():
            if key == product.lower():
                if value[0] != 0:
                    message = 'yes it is in stock'
                    print(message)
                    return product
                else:
                    message = 'no it is out of stock'
                    print(message)
                    
            else:
                message = 'sorry i couldn\'t find the product'
                print(message)
       
        
    def add_cart(self):
        product= self.check_product()
        if product != None:
            if product in self.cart:
                self.cart[product][1]+=1
            else:
                prdct= self.inventory[product]
                price = prdct[1]
                self.cart[product] = [price, 1]
                self.inventory[product][0] -=1
                print(self.cart)
        else:
            print('sorry')
    def remove_item(self):
         product= self.check_product()
         if product != None:
             if product in self.cart:
                    self.cart.pop(product)
                    self.inventory[product][0] +=1
         else:
            print('sorry')
    def payment(self):
        tc=0
        if self.cart != {}:
            for key, value in self.cart.items():
                price= value[0]
                quantity = value[1]
                tc += price*quantity
                print(key, price*quantity)
            print(f'the total bill is {tc} rs')
            print('you can Paytm us on this number- 9871053537')
        else:
            print('no items in cart')
            
            
        
SA = Shop_assistent(Inventory)
SA.greet()
    
