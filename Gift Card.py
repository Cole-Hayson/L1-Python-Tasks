gift_card_balance = 50

print("Your total gift card balance is ${}".format(gift_card_balance))

loot_box = input("\nWould you like to purchase 'Loot Box' for $20? Type YES to confirm purchase or NO to cancel.")
if loot_box.upper() == "YES":
    gift_card_balance -= 20
    print("\nLoot box purchased. Your current balance is now ${}.".format(gift_card_balance))
elif loot_box.upper() == "NO":
    print("\nPurchase canceled. Your balance remains at ${}.".format(gift_card_balance))
else:
    gift_card_balance -= 20
    print("\nYou were meant to type YES or NO but since you decided not too we are going to automatically confirm the purchase.\nUnlucky lol. Next time enter YES or NO.")
    print("Purchase successful. Your balance is now ${}.".format(gift_card_balance))

small_credits = input("\nWould you like to purchase 'Small Credits Pack' for $15. Type YES to confirm purchase or NO to cancel")
if small_credits.upper() == "YES":
    gift_card_balance -= 15
    print("\nSmall credits pack purchased. Your current balance is now ${}".format(gift_card_balance))
elif small_credits.upper() == "NO":
    print("\nPurchase canceled. Your balance remains at ${}".format(gift_card_balance))
else:
    gift_card_balance -= 15
    print("\nYou were meant to type YES or NO but since you decided not too we are going to automatically confirm the purchase.\nUnlucky lol. Next time enter YES or NO.")
    print("Purchase successful. Your balance is now ${}.".format(gift_card_balance))
