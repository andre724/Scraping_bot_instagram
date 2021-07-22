Selenium project for practice purposes.
Description:
In this project my objective was to log in Instagram, search specific pages and scrape all their posts.
However I quickly realized that it was going to be way harder than I thought, because it constantly blocked my bot.
After multiple stages and versions, the bot initially logs into an account then asks which pages the user wants to scrape, After that it goes to the first page
and it begins to scroll down, as its scrolling it scrapes all the posts's links. After reaching the end of the page it goes to the next if it has one. 
The links are stored in a Dictionary in which the account's name is the key and the links list is the value.
This is where the problem starts if the user it's not hiding his IP. Since I'm using Selenium the bot goes to the links one by one scrapin the post (right now it can't scrape albuns or reels) after a while Instagram blocks the account, so I thought accessing the post while logged out, but Instagram asks you to log in after a while.
So it doesn't matter if you're logged in or not, your ip will be blocked.

To use the bot create a .env file with these text lines in it
INSTA_USER = 
INSTA_PASS = 
PATH_DRIVER = 

Which INSTA_USEr = the username, INSTA_PASS = password and PATH_DRIVER = the path which your chrome webdriver is located.
