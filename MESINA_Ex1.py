#A Python program that prompts the user for his/her amount of money.
#It then reports how many Nintendo Wiis the person can afford.
#It will then show how much more money he/she will need to afford an additional Wii.
print("Exercse 1: Nintendo Wii");
print("Price of Wii is 30,000php");
print("Please Enter the amount of money the Customer have(No Decimal places): ");
Wii = 30000;
Money = input("Customers Money: ");
Afford = Money / Wii
print("The person can afford", Afford , "Wiis");
Change = Money - Wii
print("The Change of the customer: ", Change);
Needed = (Afford*Wii) - Money + Wii
print("The needed money for an additional Wii is:", Needed);
