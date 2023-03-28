Market Status

Websites links: "https://coinmarketcap.com/currencies", "https://www.tgju.org/profile"

Features: OOP, counter.txt, Continuous program, Error Handling, NoSQL(MongoDB), REST API, PyQt5

Languages: Python, CSS

Version.1: This program is based on reading data from web and importing their details to database. (does not support jalali date time)

Version.2: This program is based on reading data from web and importing their details to database and an application which user will use to see the results.

There are two targets: Crypto Currency and Iran Local Market. If user chooses crypto market option, they can either choose between bitcoin, ethereum and binance coin (top 3 market's coins) prices.
If user chooses Iran local market option, they either choose between 18-karat gold, gold coin, US dollar prices and Total Index of Iran Stock Exchange Amount.
Both versions support an interactive loop able program which is not indestructible (specially version.1 which is not an actual application), with invalid inputs such as strings, float numbers or unrelated Integer ones in options.

'Version.1' also comes with back option, through menus and a quit option.

Beside 'version.2' PyQt5 feature, The only difference between two versions is that 'version.1' will automatically insert results into database each time user chooses an option (for example bitcoin price).

while 'version.2' will ask the user each time they choose an option to see the results. if they accept database insertion message, results will be saved into database, if not, application will continue running.

Last thing is about run counts. in 'version.1' run count is basically a counter which works every time user chooses a specific option like US Dollar price result.
Basically everytime that user chooses this specific option, run count for this option (US Dollar for example) will be increased by one. but in 'version.2' run count will be increased only when user decides to save the results into database.

Although there is alot more to explain, I'm pretty sure that you will have a better understanding of this program by looking more closely at the codes and the comments on each part.

Note: Codes documentation and descriptions is more obvious in comments among the codes on each file.