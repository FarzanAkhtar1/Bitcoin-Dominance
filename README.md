# Bitcoin-Dominance
Caculuates Bitcoin Dominance using Coingecko's API and writes it to a CSV along with the date.
The dominance is calculated out of 100 by comparing the market cap of Bitcoin to the market cap of all other cryptocurrencies.
Dominance is used to measure the growth of alt coins compared to Bitcoin:
- Falling dominanace over time -> Alt coins could be growing more than Bitcoin
- Rising dominance over time -> Bitcoin could be growing more than alt coins

Requirements:
- Requests Library

Once requirements are installed, this can be run directly.

Configuartion:
By default, the date is in the format dd-mm-yyyy
To add a timestamp, comment out Line 15, and uncomment Line 16. This will write the date in the format dd-mm-yyyy HH:MM:SS


Implementation:
I execute this code through a once daily cron job at 23:59 to get a value for the day close. This code is suited to different timeframes such as hourly, weekly, and so on.
Once I have gained sufficient data through daily cron jobs, I use the CSV to calculate moving average values for the dominance which I then use as logic control for other programs. 